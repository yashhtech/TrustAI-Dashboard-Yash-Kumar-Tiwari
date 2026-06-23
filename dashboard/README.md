# 🚀 TrustAI — Production-Grade AI Triage System

## 📌 Overview

TrustAI is an intelligent AI-powered triage system designed to process unstructured, noisy, and potentially adversarial customer messages and convert them into structured, actionable decisions.

It combines Large Language Model (LLM) capabilities with deterministic rule-based systems and human-in-the-loop validation to ensure reliable, safe, and explainable outcomes.

---

## 🎯 Problem Statement

Modern organizations receive high volumes of customer messages including:

* Support requests
* Complaints
* Billing issues
* Security threats
* Multilingual queries
* Adversarial or abusive inputs

These messages are often inconsistent, messy, and ambiguous.

TrustAI transforms raw input into structured decisions containing:

* Category
* Priority (P0–P3)
* Summary
* Suggested Action
* Confidence Score
* Risk Level
* Sentiment
* Human Escalation Flag

---

## 🧠 System Architecture

TrustAI follows a modular multi-stage pipeline:

User Input
→ Preprocessing
→ Language Detection
→ Translation (if non-English)
→ AI Classification (LLM via Ollama)
→ Validation Layer
→ Rule Engine
→ Security Engine
→ Confidence Engine
→ Sentiment Analysis
→ Persistence Layer
→ Human Review Queue
→ Analytics Dashboard

This architecture ensures robustness, interpretability, and production readiness.

---

## 🌍 Multi-Language Support

TrustAI supports multilingual inputs using:

* Automatic language detection (langdetect)
* Translation to English (deep-translator)

Workflow:

* Detect input language
* Translate non-English text to English
* Process using AI + rules
* Preserve original message

Supported capabilities:

* Hindi, English, Hinglish
* Mixed-language inputs
* Noisy or partially translated text

---

## 🤖 AI Classification Layer

The system integrates an Ollama-based LLM to:

* Classify category and priority
* Generate summaries
* Suggest actions

This is combined with rule-based overrides to ensure deterministic correctness in critical scenarios.

---

## ⚙️ Core Components

### Preprocessing Layer

* Cleans noisy text
* Normalizes spacing
* Handles malformed input

### Validation Layer

* Ensures structured JSON output
* Enforces schema consistency
* Prevents invalid predictions

### Rule Engine

* Applies deterministic overrides
* Handles edge cases and known patterns

### Security Engine

* Detects high-risk inputs (threats, fraud, abuse)
* Forces:

  * Category → security
  * Priority → P0
  * needs_human → true

### Confidence Engine

* Adjusts confidence dynamically
* Flags low-confidence predictions
* Routes uncertain cases to human review

### Sentiment Engine

* Detects emotional tone
* Helps prioritize escalation

### Persistence Layer

* Stores:

  * Raw messages
  * AI outputs
  * Review states
  * Audit logs

### Human Review System

* Handles low-confidence or ambiguous cases
* Allows:

  * Approval
  * Override

### Analytics Dashboard

* Category distribution
* Priority distribution
* Message history
* Review queue

---

## 📊 Evaluation System

TrustAI includes a built-in evaluation pipeline:

* Predefined test dataset
* Automated classification using AI model
* Accuracy computation

### Metrics:

* Accuracy
* Total test cases
* Correct predictions

This ensures measurable performance and supports continuous improvement.

---

## 📡 API Endpoints

Key endpoints include:

* `/triage` → Process new message
* `/history` → Retrieve processed messages
* `/review-queue` → Get pending reviews
* `/review/approve` → Approve decision
* `/review/override` → Override decision
* `/analytics` → Dashboard metrics
* `/analytics/categories` → Category distribution
* `/analytics/priorities` → Priority distribution
* `/evaluation` → Run evaluation pipeline

---

## 🏗️ Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* React
* Axios
* Recharts

### AI Layer

* Ollama LLM

### NLP Tools

* langdetect (language detection)
* deep-translator (translation)

---

## 📂 Project Structure

```
backend/
  ├── api/
  ├── services/
  ├── models/
  ├── validators/
  ├── database/

frontend/
  ├── dashboard/
  ├── components/
```

---

## 🚀 Setup Instructions

### Backend

* Install dependencies
* Run FastAPI server using Uvicorn
* Default port: 8000

### Frontend

* Install dependencies
* Start React app
* Default port: 3000

---

## 🧪 Example

**Input:**
"I will kill you"

**Output:**

* Category: security
* Priority: P0
* Risk Level: CRITICAL
* needs_human: true
* Confidence: high

---

## 🛡️ Reliability and Safety

TrustAI is designed to:

* Handle adversarial inputs
* Prevent unsafe outputs
* Always escalate critical threats
* Maintain deterministic overrides for security cases

---

## ⚡ Production Readiness

The system is modular and extensible.

Possible production upgrades:

* PostgreSQL instead of SQLite
* Redis caching
* Queue systems (Kafka / RabbitMQ)
* Authentication & authorization
* Containerization (Docker)
* Cloud deployment

---

## 🧠 Design Principles

* Reliability-first
* Human-in-the-loop
* Explainable AI decisions
* Safety over automation
* Modular architecture

---

## 👨‍💻 Author

Yash Kumar

---

## 🏁 Conclusion

TrustAI demonstrates a production-oriented AI triage system that combines:

* LLM intelligence
* Rule-based safeguards
* Multilingual support
* Evaluation pipeline
* Human oversight

It provides a scalable and reliable solution for real-world customer message processing.
