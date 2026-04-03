from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str

class Action(BaseModel):
    label: str
    action: str

class Reward(BaseModel):
    score: float