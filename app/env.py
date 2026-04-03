import random
from app.models import Observation, Action, Reward
from app.data import EMAILS

class EmailEnv:
    def __init__(self):
        self.current_email = None

    def reset(self):
        self.current_email = random.choice(EMAILS)
        return Observation(email_text=self.current_email["text"])

    def step(self, action: Action):
        correct_label = self.current_email["label"]

        score = 0.0

        # correct prediction
        if action.label == correct_label:
            score = 1.0

        # partial (safe guess)
        elif action.label == "normal":
            score = 0.5

        # penalty cases
        elif correct_label == "urgent" and action.label != "urgent":
            score = -1.0  # missed critical issue

        elif action.label == "urgent" and correct_label != "urgent":
            score = -0.5  # false alarm

        else:
            score = 0.0

        done = True

        return Observation(email_text="done"), Reward(score=score), done, {}

    def state(self):
        return self.current_email