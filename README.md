# 🎓 AI Career Counselor

An intelligent, personalized career guidance platform built with **Streamlit**, **LangChain**, **Ollama**, and local **LLMs like Gemma 2B**. This app provides career suggestions, college recommendations, learning roadmaps, and a conversational chatbot assistant – all offline and open-source.

---

## 💡 Features

- 🧠 **Career Quiz**: Determines your best-fit career based on interests and preferences.
- 📚 **College Recommender**: Suggests top colleges mapped to your chosen career.
- 🗺 **Personalized Roadmaps**: Step-by-step guides with curated YouTube tutorials.
- 💬 **Conversational Chatbot**: A friendly, empathetic assistant using **Gemma 2B + Wikipedia**, capable of answering:
  - College details (fees, placements, exams, etc.)
  - Career alternatives (e.g., after failing JEE/NEET)
  - Personal/emotional doubts
- 🧠 **Hybrid Logic**:
  - Uses **LLM directly** for emotional and generic queries
  - Triggers **Wikipedia Search Tool** only for facts about colleges/exams

---

## 🏗️ Tech Stack

| Layer         | Tech                     |
|---------------|---------------------------|
| 💬 LLM        | Ollama + Gemma 2B (local) |
| 🧠 Agent      | LangChain                 |
| 🔎 Tooling    | WikipediaAPIWrapper       |
| 🎨 Frontend   | Streamlit                 |
| 💾 Memory     | `st.session_state`        |

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-career-counselor
cd ai-career-counselor
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
conda create -n career_counselor python=3.10
conda activate career_counselor
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Make sure to install and run Ollama:

bash
Copy
Edit
# Install Ollama (if not installed)
https://ollama.com/download

# Pull Gemma
ollama pull gemma:2b

# Start the Ollama server
ollama serve
4. Run the App
bash
Copy
Edit
streamlit run app.py
📁 Folder Structure
graphql
Copy
Edit
📂 Career_Counselor/
│
├── app.py                          # Streamlit main page
├── chatbot_logic.py                # Gemma + Wikipedia chatbot backend
├── roadmaps.py                     # Roadmap data + rendering logic
├── youtube_fetcher.py              # YouTube course search (optional)
├── requirements.txt
│
├── 📁 pages/
│   ├── 1_Career_Quiz.py
│   ├── 2_Career_Roadmaps.py
│   ├── 3_College_Recommendations.py
│   └── 4_Career_Chatbot.py
🧠 How It Works
Career Quiz → Career → Colleges + Roadmap + Chatbot
You can use this end-to-end or jump directly to the chatbot!

All career steps include curated video tutorials (with fallbacks).

Chatbot answers career or college-related queries intelligently.

📸 Demo



🙋🏻‍♀️ Author
Arpita Sethi
LinkedIn | GitHub

🪄 Future Work
🌐 Add real-time college data from APIs like Shiksha or NIRF.

🗣️ Integrate voice input with Whisper.

🧠 Add emotional fatigue detection for better chatbot empathy.

🧬 Support AR/VR for career simulations (Phase II)
