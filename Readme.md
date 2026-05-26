# 🎯 XAI Manufacturing Inspector Pro
### *Explainable AI for Real-Time Industrial Quality Control*

## 🚀 Project Overview
The **XAI Manufacturing Inspector Pro** is a full-stack, research-oriented platform designed to solve the "Black Box" problem in industrial AI. While standard models can predict a machine failure, they rarely explain **why**. 

Our platform uses **Explainable AI (SHAP)** to provide factory engineers with transparent, mathematically validated reasons for every prediction, visualized through an interactive 3D dashboard.

---

## 🏗️ The Hybrid Architecture
We utilize a **Microservices Approach**, splitting the "Intelligence" from the "Interface" to ensure maximum performance and scalability.



### 1. The Brain (Python / FastAPI)
* **Why Python?** It is the industry standard for Machine Learning. Libraries like `XGBoost` for prediction and `SHAP` for explainability are native to this ecosystem.
* **Why FastAPI?** It is the fastest Python web framework, allowing us to serve AI predictions with near-zero latency.

### 2. The Body (Node.js / Express / EJS)
* **Why Node.js?** Exceptional at handling asynchronous requests. It acts as the "Orchestrator," managing user sessions and calling the AI Brain.
* **Why EJS?** Provides a lightweight way to render dynamic data (like SHAP scores) directly into HTML without the overhead of complex frontend frameworks.

---

## 🔄 Data Flow: How it Works
1.  **Input:** A user enters sensor data (Temperature, Vibration, Pressure) via the **Node.js** dashboard.
2.  **Request:** Node.js sends this data to the **Python API** using `Axios`.
3.  **Inference:** Python runs the data through an **XGBoost** model to predict failure risk.
4.  **Explanation:** The **SHAP Engine** calculates exactly which sensor contributed most to that risk.
5.  **Validation:** The **Validation Layer** checks if the AI's logic matches physical ground-truth formulas.
6.  **Response:** Node.js receives the JSON results and renders them into **Chart.js** graphs and a **3D Three.js** factory model.



---

## 🎯 Project Goals
* **Interpretability:** Convert complex tensors into human-readable insights (e.g., "Failure risk is 80% due to 20% increase in Vibration").
* **Validation:** Use "Faithfulness Metrics" to prove the XAI isn't just guessing.
* **Interaction:** Allow engineers to perform **"What-If" analysis** using real-time sliders to see how changing variables prevents failure.

---

## 🛠️ Tech Stack
| Layer | Technologies |
| :--- | :--- |
| **Backend (AI)** | Python, FastAPI, XGBoost, SHAP, Pandas |
| **Backend (Web)** | Node.js, Express, Axios |
| **Frontend** | EJS (Templating), Tailwind CSS, Chart.js, Three.js |
| **Deployment** | Docker (Optional), GitHub Actions |

---

## 📂 Repository Structure
```text
├── ai_engine/           # Python Machine Learning Microservice
│   ├── main.py          # API Gateway (FastAPI)
│   ├── models/          # Trained Model Binaries
│   └── explainer.py     # SHAP Logic
├── web_dashboard/       # Node.js Application
│   ├── server.js        # Express Server logic
│   ├── views/           # EJS Dashboard Templates
│   └── public/          # Client-side Visuals (JS/CSS)
└── research/            # Methodology & Validation Reports