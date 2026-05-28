# 🤖 Multi-Agent Research Assistant (GenAI System)

An AI-powered **multi-agent research system** built using Streamlit that autonomously performs web research, content extraction, report generation, and critique using an LLM-driven pipeline.

---

## 🚀 Features

- 🔎 **Search Agent** – Fetches relevant web results for the given topic  
- 📄 **Reader Agent** – Extracts and processes useful content from sources  
- ✍️ **Writer Agent** – Generates structured research reports using LLMs  
- 🧠 **Critic Agent** – Evaluates and improves report quality via feedback loop  
- 📊 Live agent execution logs  
- 📁 PDF export of final research report  
- 🕘 Session-based research history tracking  
- 🎨 Interactive Streamlit UI with dark theme  

---

## 🧠 System Architecture

The project follows a **multi-agent LLM pipeline inspired by RAG (Retrieval-Augmented Generation)**:

1. **User Query Input**
2. **Search Agent → Web Retrieval**
3. **Reader Agent → Context Extraction**
4. **Writer Agent → Report Generation (LLM-based)**
5. **Critic Agent → Output Evaluation & Feedback**
6. **Final Structured Report Output**

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Large Language Models (LLMs)  
- Prompt Engineering  
- Multi-Agent Architecture  
- Web Scraping (BeautifulSoup / Requests / Selenium)  
- FPDF (PDF generation)  
- Tempfile, Datetime (system utilities)  

---

## 📂 Project Structure
├── app.py # Streamlit frontend
├── pipeline.py # Multi-agent orchestration logic
├── agents/ # Search, Reader, Writer, Critic agents
├── utils/ # Helper functions (scraping, formatting, etc.)
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ How It Works

1. User enters a research topic in the Streamlit UI  
2. System triggers a multi-agent pipeline:
   - Search Agent collects relevant data
   - Reader Agent extracts meaningful content
   - Writer Agent generates structured report using LLM
   - Critic Agent reviews and improves output  
3. Results are displayed in real time with logs  
4. Final report can be downloaded as a **PDF file**

---
