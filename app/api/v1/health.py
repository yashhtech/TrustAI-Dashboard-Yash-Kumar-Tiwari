from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "TrustAI"
    }


@router.get("/system-info")
def system_info():
    return {
        "app": "TrustAI",
        "version": "1.0.0"
    }