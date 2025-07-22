# 🧠 AI Career Counselor

An intelligent and interactive AI-powered career guidance assistant built using **Streamlit** and **LLMs (via Ollama)**. The app analyzes user input (goals, interests, education level) and provides personalized career advice, learning paths, and job role recommendations.

---

## 🚀 Features

- 🔍 Analyze user's academic/professional interests.
- 💼 Recommend relevant tech and non-tech careers.
- 📚 Suggest courses and certifications to pursue.
- 🧭 Help plan career roadmap based on goals.
- 🧠 Powered by lightweight, local LLMs via Ollama.
- 🎨 Built with Streamlit for a fast, interactive UI.

---

## 📦 Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** Ollama LLM (e.g., `gemma:2b`)
- **Language Model:** Local Gemma / TinyLlama via Ollama
- **Environment:** Python 3.10+

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-career-counselor
cd ai-career-counselor
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
conda create -n career_counselor python=3.10
conda activate career_counselor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Run Ollama (if not already installed)

```bash
# Download Ollama from https://ollama.com/download
# Then run the following in terminal:
ollama pull gemma:2b
ollama serve
```

### 5. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Type in your interests, skills, or career goal (e.g., "I want to become a data scientist").
2. The agent will respond with suitable career options, suggested learning paths, and tools.
3. Modify or refine your input to get more personalized advice.

---

## 🗂️ Folder Structure

```
ai-career-counselor/
├── assets/
│   └── [images, icons, etc.]
├── app.py
├── requirements.txt
├── README.md
└── utils/
    └── [helper modules if any]
```

---

## 📸 Screenshots

### 🏠 Home Screen

![Home Screen](assets/home.png)

### 📊 Career Suggestions

![Career Suggestions](assets/output.png)



## 🤝 Acknowledgements

- 💡 [Ollama](https://ollama.com) – For local LLM execution
- 🧠 [Gemma](https://ai.google.dev/gemma) – Lightweight open-source LLM
- ⚡ [Streamlit](https://streamlit.io) – For the frontend UI

---


