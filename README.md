# 🤖 Natasha AI

Natasha AI is a conversational AI assistant built using LangGraph,Groq,Streamlit and ChromaDB. 
It supports natural conversations as well as Retrieval-Augmented Generation (RAG) over uploaded PDF documents.

---


<img width="1438" height="677" alt="Screenshot 2026-07-06 at 9 03 21 PM" src="https://github.com/user-attachments/assets/6a709501-092d-40d7-a8dd-75a53915c2cf" />





## Features

* 💬 Conversational AI
* 📄 PDF document upload
* 🔍 Retrieval-Augmented Generation (RAG)
* 🧠 ChromaDB vector database
* ⚡ Groq LLM integration
* 🌊 Streaming responses
* 🗂 Multiple chat sessions
* ✨ AI-generated chat titles
* 🔀 LangGraph workflow

---

## Tech Stack

* Python
* Streamlit
* LangGraph
* LangChain
* Groq API
* ChromaDB
* Sentence Transformers

---

## Prerequisites

Before running the project, ensure you have:

* Python 3.11 or later
* Git
* A Groq API Key

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Natasha-AI.git
cd Natasha-AI
```

Create a virtual environment:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```text
GROQ_API_KEY=your_groq_api_key_here
```

---

## Run the Application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```
http://localhost:8501
```

---

## Project Structure

```
Natasha-AI/
│
├── app.py
├── requirements.txt
├── config/
├── core/
├── documents/
├── graph/
├── services/
├── ui/
└── README.md
```

---

## Current Capabilities

* Conversational AI
* PDF Upload
* Document Indexing
* Semantic Search
* Retrieval-Augmented Generation (RAG)
* LangGraph-based workflow
* AI-generated chat titles
* Streaming responses

---

## Roadmap

* Tool Calling
* Web Search
* Persistent Memory
* Agentic Workflows
* Multi-modal Support
* Authentication
* Database-backed chat history

---

## License

This project is intended for learning and experimentation.
