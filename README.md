# 🧠 LLM Microservice Hub

A production-grade **FastAPI + AsyncIO** microservice designed for Large Language Model (LLM) integrations.  
This service provides API endpoints for **chat completions**, **embeddings**, and includes an extendable structure for future AI workflows such as async pipelines, rate-limited LLM calls, and background processing.

This project demonstrates clean backend engineering practices, modular design, and async-first architectures used in modern AI applications.

---

## 🚀 Features

- **FastAPI-based architecture** with modular routing  
- **LLM chat endpoint** (`/chat`) for conversational responses  
- **Embeddings endpoint** (`/embeddings`) returning vector encodings  
- **AsyncIO-powered architecture** for non-blocking performance  
- **Service-layer wrappers** prepared for OpenAI or any LLM provider  
- **Clean folder structure** for scalability  
- **Pydantic validation models** for clear API contracts  
- Ready for future additions: caching, retries, rate limiting, and model routing  

---

## 📂 Project Structure

```
llm-microservice-hub/
│
├── app/                     # FastAPI entrypoint, router mounting
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── chat.py          # Chat completion endpoint
│   │   └── embeddings.py    # Embeddings endpoint
│   │
│   ├── models/
│   │   └── schemas.py       # Shared Pydantic schemas
│   │
│   └── services/
│       └── llm_client.py    # Placeholder LLM service client
│
└── README.md
```

---

## ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

---

## 🔌 API Endpoints

---

### **1. POST /chat**

#### Request  
```json
{
  "message": "Hello!"
}
```

#### Example Response  
```json
{
  "reply": "Hi! How can I assist you today?"
}
```

---

### **2. POST /embeddings**

#### Request  
```json
{
  "text": "Machine learning is powerful."
}
```

#### Example Response  
```json
{
  "embedding": [0.123, 0.552, 0.982, 0.441]
}
```

---

## 🧩 Extending With a Real LLM Provider

Modify `services/llm_client.py` to integrate:

- **OpenAI API**
- **Anthropic Claude**
- **Groq LLM**
- **Custom / self-hosted models**

The architecture is intentionally designed so developers can easily replace the placeholder implementation with a real LLM backend.

---

## 🛠 Tech Stack

- Python 3.10+  
- FastAPI  
- AsyncIO  
- Uvicorn  
- Pydantic  

---

## 📌 Status

This project is part of an LLM engineering portfolio demonstrating production-grade backend practices, async patterns, and AI integration workflows.
