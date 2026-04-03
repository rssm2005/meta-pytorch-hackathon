import gradio as gr
from fastapi import FastAPI
from app.env import EmailEnv
from app.models import Action

# ---------------- INIT ----------------
env = EmailEnv()
fastapi_app = FastAPI()

# ---------------- FASTAPI ROUTES ----------------
@fastapi_app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}


@fastapi_app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward.score if hasattr(reward, "score") else reward,
        "done": done,
        "info": info
    }


@fastapi_app.get("/state")
def state():
    return {"state": env.state()}


@fastapi_app.post("/grader")
def grader(action: Action):
    current = env.state()

    if current is None:
        return {"error": "Call /reset first"}

    actual = current["label"]

    if action.label == actual:
        score = 1.0
    elif (action.label == "normal" and actual in ["spam", "urgent"]) or \
         (actual == "normal" and action.label in ["spam", "urgent"]):
        score = 0.5
    else:
        score = 0.2

    return {"score": score}


@fastapi_app.get("/baseline")
def baseline():
    env.reset()
    action = Action(label="normal", action="ignore")
    _, reward, _, _ = env.step(action)

    return {
        "baseline_score": reward.score if hasattr(reward, "score") else reward
    }


# ---------------- GRADIO UI ----------------
def reset_env():
    return env.reset()


def get_state():
    return env.state()


def take_action(label, action):
    return env.step(Action(label=label, action=action))


def grade_action(label, action):
    current = env.state()

    if current is None:
        return {"error": "Call reset first"}

    actual = current["label"]

    if label == actual:
        score = 1.0
    elif (label == "normal" and actual in ["spam", "urgent"]) or \
         (actual == "normal" and label in ["spam", "urgent"]):
        score = 0.5
    else:
        score = 0.2

    return {"score": score}


def get_baseline():
    env.reset()
    action = Action(label="normal", action="ignore")
    _, reward, _, _ = env.step(action)
    return {"baseline_score": reward.score if hasattr(reward, "score") else reward}


with gr.Blocks() as demo:
    gr.Markdown("# 🚀 OpenEnv Dashboard")

    gr.Markdown("""
    ## 📘 How to Use
    🔄 Reset → Initialize environment  
    📊 State → View current state  
    ⚡ Execute → Take action  
    🧠 Grade → Evaluate correctness  
    📈 Baseline → Compare performance  
    🎯 Goal: Maximize score by correct actions
    """)

    gr.Markdown("---")

    with gr.Row():
        reset_btn = gr.Button("🔄 Reset")
        state_btn = gr.Button("📊 State")
        baseline_btn = gr.Button("📈 Baseline")

    output = gr.JSON(label="Output")

    reset_btn.click(reset_env, outputs=output)
    state_btn.click(get_state, outputs=output)
    baseline_btn.click(get_baseline, outputs=output)

    gr.Markdown("## ⚡ Take Action")

    with gr.Row():
        label = gr.Dropdown(
            ["spam", "normal", "urgent"],
            label="Label",
            value="normal"
        )

        action = gr.Dropdown(
            ["ignore", "process"],
            label="Action",
            value="ignore"
        )

    with gr.Row():
        exec_btn = gr.Button("🚀 Execute")
        grade_btn = gr.Button("🧠 Grade")

    exec_btn.click(take_action, inputs=[label, action], outputs=output)
    grade_btn.click(grade_action, inputs=[label, action], outputs=output)


app = gr.mount_gradio_app(fastapi_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
