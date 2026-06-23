from fastapi import FastAPI

app = FastAPI(
    title="TrustAI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "TrustAI Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }