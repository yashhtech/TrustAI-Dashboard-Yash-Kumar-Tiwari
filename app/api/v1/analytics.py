from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.analytics_service import (
    AnalyticsService
)

router = APIRouter()


@router.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):

    return AnalyticsService.get_dashboard(
        db
    )

@router.get("/analytics/categories")
def category_stats(
    db: Session = Depends(get_db)
):

    return AnalyticsService.category_stats(
        db
    )


@router.get("/analytics/priorities")
def priority_stats(
    db: Session = Depends(get_db)
):

    return AnalyticsService.priority_stats(
        db
    )


