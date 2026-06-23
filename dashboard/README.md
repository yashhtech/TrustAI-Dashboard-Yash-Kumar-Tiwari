# 🚀 TrustAI — Intelligent AI Triage System

An AI-powered system that processes messy customer messages and converts them into structured decisions.

Built for the **Frontline One-Day AI Challenge**

---

## 🎯 Problem

Companies receive thousands of messy customer messages:

- complaints
- support requests
- random questions
- abusive / adversarial inputs

👉 Goal: Automatically convert them into:

- category
- priority (P0–P3)
- summary
- suggested action
- confidence
- needs_human

---

## 🧠 Features

### ✅ AI Triage Pipeline
- Preprocessing (cleaning text)
- Code detection
- AI classification (Ollama)
- Rule Engine override (security)
- Confidence scoring
- Sentiment analysis

---

### 🔐 Security Engine
Detects critical threats like:

- hack / fraud
- kill / attack
- breach / stolen

➡️ Automatically sets:
- category = `security`
- priority = `P0`
- needs_human = `true`

---

### 🤖 Confidence Engine
- Boosts confidence based on category/priority
- Flags low-confidence for human review

---

### 👨‍💻 Human Review System
- Review queue for uncertain cases
- Approve / Override decisions
- Improves reliability

---

### 📊 Analytics Dashboard (React)
- Category distribution (Pie Chart)
- Priority distribution (Bar Chart)
- History table
- Review queue UI

---

### 💾 Persistence
- Messages stored in DB
- Triage results tracked
- Audit logs available

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- React
- Axios
- Recharts

---

## 📂 Project Structure
