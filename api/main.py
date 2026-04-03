from fastapi import FastAPI
from app.env import EmailEnv
from app.models import Action

app = FastAPI()
env = EmailEnv()

# ---------------- ROOT ----------------
@app.get("/")
@app.post("/")
def root():
    obs = env.reset()
    return {
        "observation": obs
    }

# ---------------- RESET ----------------
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs
    }

# fallback
@app.get("/reset")
def reset_get():
    obs = env.reset()
    return {
        "observation": obs
    }


# ---------------- STEP ----------------
@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward.score if hasattr(reward, "score") else reward,
        "done": done,
        "info": info
    }

# fallback
@app.get("/step")
def step_get():
    return {"error": "Use POST /step with JSON body"}


# ---------------- STATE ----------------
@app.get("/state")
def state():
    return {
        "state": env.state()
    }


# ---------------- TASKS ----------------
@app.get("/tasks")
def tasks():
    return {
        "tasks": ["easy", "medium", "hard"],
        "actions": ["spam", "normal", "urgent"]
    }


# ---------------- GRADER ----------------
@app.post("/grader")
def grader(action: Action):
    current = env.state()

    if current is None:
        return {"error": "Call /reset first"}

    actual = current["label"]

    # strong match
    if action.label == actual:
        score = 1.0
    # partially correct (close enough)
    elif (action.label == "normal" and actual in ["spam", "urgent"]) or \
         (actual == "normal" and action.label in ["spam", "urgent"]):
        score = 0.5
    else:
        score = 0.2

    return {"score": score}


# ---------------- BASELINE ----------------
@app.get("/baseline")
def baseline():
    env.reset()

    action = Action(label="normal", action="ignore")
    _, reward, _, _ = env.step(action)

    return {
        "baseline_score": reward.score if hasattr(reward, "score") else reward
    }
