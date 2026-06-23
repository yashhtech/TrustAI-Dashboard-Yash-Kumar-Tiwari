from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.health import router as health_router

from app.database.database import Base
from app.database.database import engine

from app.models.message import Message
from app.models.triage_result import TriageResult
from app.models.audit_log import AuditLog

from app.core.config import settings
from app.core.logger import logger
from app.api.v1.preprocessing import router as preprocessing_router
from app.api.v1.triage import router as triage_router
from app.api.v1.history import router as history_router
from app.models.review_queue import ReviewQueue
from app.api.v1.review import router as review_router
from app.api.v1.evaluation import router as evaluation_router
from app.api.v1.analytics import (router as analytics_router)



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React (localhost:3000)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    preprocessing_router,
    prefix="/api/v1",
    tags=["Preprocessing"]
)

app.include_router(
    triage_router,
    prefix="/api/v1",
    tags=["AI Triage"]
)

app.include_router(
    history_router,
    prefix="/api/v1",
    tags=["History"]
)

app.include_router(
    review_router,
    prefix="/api/v1",
    tags=["Human Review"]
)

app.include_router(
    analytics_router,
    prefix="/api/v1",
    tags=["Analytics"]
)

app.include_router(
    evaluation_router,
    prefix="/api/v1",
    tags=["Evaluation"]
)

@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "message": "TrustAI Backend Running"
    }