# 🚀 TrustAI — Production-Grade AI Triage System

## 📌 Overview

TrustAI is an intelligent AI-powered system designed to process unstructured, messy, and potentially adversarial customer messages and convert them into structured, actionable decisions.

It simulates a real-world enterprise support pipeline by combining AI intelligence with deterministic rules and human oversight.

---

## 🎯 Problem Statement

Modern companies receive a massive volume of customer messages including support requests, complaints, security threats, and random queries. These inputs are often noisy, inconsistent, and sometimes malicious.

TrustAI transforms such raw input into structured decisions containing category, priority, summary, suggested action, confidence, and human escalation signals.

---

## 🧠 System Architecture

The system follows a multi-stage pipeline:

User Input → Preprocessing → Code Detection → AI Classification → Validation → Rule Engine → Security Engine → Confidence Engine → Sentiment Analysis → Database Storage → Human Review → Dashboard

Each stage ensures reliability, safety, and structured output generation.

---

## ⚙️ Core Components

### Preprocessing Layer

Handles noisy input, removes unwanted characters, and prepares text for AI processing.

### AI Classification

Uses a language model to classify messages into categories and priorities, and generate summaries and suggested actions.

### Validation Layer

Ensures all AI outputs are valid, consistent, and within expected ranges.

### Rule Engine

Overrides AI decisions when predefined patterns are detected to ensure deterministic behavior.

### Security Engine

Detects high-risk messages such as threats, fraud, and breaches. It forcefully escalates these cases by assigning highest priority and requiring human intervention.

### Confidence Engine

Adjusts confidence scores dynamically and flags uncertain predictions.

### Sentiment Engine

Analyzes emotional tone of the message to assist in escalation and prioritization.

### Persistence Layer

Stores all data including raw messages, processed results, audit logs, and review queue entries.

### Human Review System

Low-confidence or ambiguous cases are routed to a review queue where decisions can be approved or overridden.

### Analytics Dashboard

Provides visual insights including category distribution, priority distribution, history tracking, and review queue management.

---

## 🏗️ Technology Stack

Backend is built using FastAPI and SQLAlchemy with SQLite as the database.
Frontend is built using React with Axios for API communication and Recharts for visualization.
The AI layer uses Ollama-based LLM integration.

---

## 📂 Project Structure

The project is divided into backend and frontend layers.

The backend contains API routes, services, models, validators, and database configuration.

The frontend dashboard handles visualization, user interaction, and real-time updates.

---

## 🚀 Setup Instructions

### Backend Setup

Navigate to the backend folder and install dependencies. Then start the server using Uvicorn. The backend runs locally on port 8000.

### Frontend Setup

Navigate to the dashboard folder, install dependencies, and start the React application. The frontend runs locally on port 3000.

---

## 📡 API Overview

The system exposes endpoints for triaging messages, retrieving history, managing the review queue, approving decisions, overriding decisions, and fetching analytics data.

---

## 🧪 Example

Input message:
"I will kill you"

Output:
The system classifies this as a high-risk security issue, assigns top priority, sets confidence to maximum, and flags it for human review.

---

## 🛡️ Reliability and Safety

The system is designed to handle messy, adversarial, and ambiguous inputs. It ensures no unsafe outputs are generated and always escalates critical scenarios.

Security-related messages are always overridden by deterministic rules to avoid reliance on AI uncertainty.

---

## 📈 Evaluation Coverage

The system successfully operates end-to-end, processes real-world noisy data, integrates AI with rule-based logic, supports human intervention, and provides a functional dashboard for monitoring and control.

---

## ⚡ Production Readiness

The architecture is modular and scalable. Components can be extended or replaced independently.

The system can be upgraded with production-grade tools such as PostgreSQL, Redis caching, message queues, authentication layers, and containerization.

---

## 🧠 Design Principles

The system is built on reliability, safety, and explainability. AI decisions are always backed by rules when necessary, and human oversight is always available.

---

## 👨‍💻 Author

Yash Kumar

---

## 🏁 Conclusion

TrustAI demonstrates a practical implementation of an AI-powered triage system that is reliable, secure, and production-oriented.

It combines machine intelligence with deterministic safeguards and human validation to ensure trustworthy decision-making in real-world scenarios.
