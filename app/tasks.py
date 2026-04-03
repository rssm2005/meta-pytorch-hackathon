def easy_task(pred, actual):
    return 1.0 if pred == actual else 0.0

def medium_task(pred, actual):
    if pred == actual:
        return 1.0
    elif pred == "normal":
        return 0.5
    return 0.0

def hard_task(pred, actual, action):
    if pred == actual and action in ["reply", "escalate"]:
        return 1.0
    return 0.0