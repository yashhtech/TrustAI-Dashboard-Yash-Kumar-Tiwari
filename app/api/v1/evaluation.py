from fastapi import APIRouter
from app.services.evaluation_service import EvaluationService

router = APIRouter()


@router.get("/evaluation")
def run_evaluation():
    return EvaluationService.evaluate()