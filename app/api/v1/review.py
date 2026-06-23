from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.review_queue import ReviewQueue

from app.schemas.review import ReviewDecision

router = APIRouter()


@router.get("/review-queue")
def review_queue(
    db: Session = Depends(get_db)
):

    data = db.query(
        ReviewQueue
    ).filter(
        ReviewQueue.status == "pending"
    ).all()

    return data


@router.post("/review/approve")
def approve_review(
    payload: ReviewDecision,
    db: Session = Depends(get_db)
):

    item = db.query(
        ReviewQueue
    ).filter(
        ReviewQueue.id == payload.id
    ).first()

    if not item:
        return {
            "error": "Not found"
        }

    item.reviewed = True

    item.status = "approved"

    db.commit()

    return {
        "message": "Approved"
    }


@router.post("/review/override")
def override_review(
    payload: ReviewDecision,
    db: Session = Depends(get_db)
):

    item = db.query(
        ReviewQueue
    ).filter(
        ReviewQueue.id == payload.id
    ).first()

    if not item:
        return {
            "error": "Not found"
        }

    item.ai_category = payload.category

    item.ai_priority = payload.priority

    item.status = "overridden"

    item.reviewed = True

    db.commit()

    return {
        "message": "Updated"
    }


