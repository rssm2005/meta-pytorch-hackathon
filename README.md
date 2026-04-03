# 🚀 Meta PyTorch Hackathon – OpenEnv RL Environment

An interactive **Reinforcement Learning environment** built using **OpenEnv**, with a **FastAPI backend** and a **Gradio-based UI dashboard**, deployed on Hugging Face Spaces.

---

## 🧠 What This Project Does

This project simulates an **email/task classification environment** where an agent must:

* Interpret incoming tasks (spam / normal / urgent)
* Take correct actions (ignore / process)
* Maximize reward through correct decisions

It provides both:

* 🔌 API access for automation
* 🎛️ Interactive UI for manual experimentation

---

## ⚡ Key Features

* 🧠 Custom RL Environment (`EmailEnv`)
* ⚡ FastAPI endpoints for agent interaction
* 🎛️ Gradio UI dashboard (dark theme)
* 📊 Real-time state + reward tracking
* 📈 Baseline scoring system
* 🚀 Hugging Face deployment ready

---

## 🏗️ Project Structure

```
.
├── api/
│   └── main.py          # FastAPI endpoints
│
├── app/
│   ├── env.py           # RL Environment logic
│   ├── models.py        # Action schema
│   └── utils.py
│
├── server/
│   └── app.py           # Entry point for deployment
│
├── app.py               # Gradio UI
├── pyproject.toml       # Package config
├── uv.lock              # Dependency lock
├── requirements.txt
└── README.md
```

---

## 🌐 Live Demo

👉 **Hugging Face Space:**
https://sparkgen0markvi-meta-pytorch-hackathon.hf.space

---

## 📡 API Endpoints

| Endpoint    | Method | Description             |
| ----------- | ------ | ----------------------- |
| `/reset`    | POST   | Reset environment       |
| `/step`     | POST   | Take action             |
| `/state`    | GET    | Get current state       |
| `/tasks`    | GET    | Available tasks/actions |
| `/grader`   | POST   | Evaluate action         |
| `/baseline` | GET    | Baseline performance    |

---

## 🧪 Example Usage

### Reset Environment

```
POST /reset
```

### Take Action

```json
POST /step
{
  "label": "spam",
  "action": "ignore"
}
```

### Grade Action

```json
POST /grader
{
  "label": "urgent",
  "action": "process"
}
```

---

## 🎛️ UI Dashboard

The Gradio interface provides:

* 🔄 Reset environment
* 📊 View current state
* ⚡ Execute actions
* 🧠 Grade performance
* 📈 Compare baseline

---

## ⚙️ Local Setup

```
git clone https://github.com/Spark1805/meta-pytorch-hackathon.git
cd meta-pytorch-hackathon
pip install -r requirements.txt
```

Run API:

```
uvicorn api.main:app --reload
```

Run UI:

```
python app.py
```

---

## 🧠 Tech Stack

* Python
* FastAPI
* Gradio
* OpenEnv
* PyTorch (conceptual alignment)

---

## 🎯 Hackathon Context

Built for the **Meta x PyTorch OpenEnv Hackathon**

Focus areas:

* Reinforcement learning environments
* Agent decision systems
* Scalable API + UI integration

---

## 🏁 Summary

This project demonstrates:

* Environment design for RL
* API-driven agent interaction
* UI-based experimentation
* Production-ready deployment

---

## ⚠️ Note

This project is intended for **demonstration and evaluation purposes**.
"# meta-pytorch-hackathon" 
