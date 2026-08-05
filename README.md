# 🧠 TetraAgent Synthesizer

An autonomous multi agent research system built with **LangChain**, **Google Gemini**, **Tavily Search**, and **Streamlit**.

TetraAgent Synthesizer uses four specialized AI agents that work together to perform web research, extract relevant information, generate a structured research report, and review the final output for quality.

---

## ✨ Features

- 🔎 Search the web using Tavily Search
- 📖 Read and extract content from webpages
- ✍️ Generate professional research reports
- ⭐ Review reports with an AI Critic Agent
- 🧠 Multi Agent workflow powered by LangChain
- 🌐 Simple Streamlit web interface

---

## 🤖 AI Agents

### 🔎 Search Agent
Searches trusted web sources and gathers relevant information about the research topic.

### 📖 Reader Agent
Scrapes and extracts useful content from the most relevant webpages using BeautifulSoup.

### ✍️ Writer Agent
Creates a well structured research report from the collected information.

### ⭐ Critic Agent
Reviews the generated report, evaluates its quality, and provides constructive feedback.

---

## ⚙️ Workflow

```text
User Topic
     │
     ▼
Search Agent
     │
     ▼
Reader Agent
     │
     ▼
Writer Agent
     │
     ▼
Critic Agent
     │
     ▼
Final Research Report
```

---

## 🛠 Tech Stack

### Frameworks

- LangChain
- Streamlit

### AI Model

- Google Gemini 3.6 Flash

### Search

- Tavily Search API

### Web Scraping

- BeautifulSoup
- Requests

### Language

- Python 3

---

## 📂 Project Structure

```text
Multi-Agent-Research-System/
│
├── app.py                 # Streamlit UI
├── pipeline.py            # Multi Agent workflow
├── agents.py              # AI Agents
├── tools.py               # Search and scraping tools
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/muhammadsohaib796/Multi-Agent-Research-System.git

cd Multi-Agent-Research-System
```

---

### Create a virtual environment

```bash
python -m venv lang_env
```

Activate it

**Windows**

```bash
lang_env\Scripts\activate
```

**Linux / macOS**

```bash
source lang_env/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
├── home.png
├── research_report.png
└── critic_review.png
```

---

## 📈 Future Improvements

- Export reports as PDF
- Research history
- Multiple search providers
- Live agent progress tracking
- Source credibility scoring
- Better report formatting
- Dark and Light themes

---

## 👨‍💻 Author

**Sohaib Shakeel**

Backend & AI Developer

GitHub:
https://github.com/muhammadsohaib796

LinkedIn:
(Add your LinkedIn profile here)

---

## 📄 License

This project is intended for educational and learning purposes.