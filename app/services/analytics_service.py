from sqlalchemy import func

from app.models.message import Message
from app.models.triage_result import TriageResult
from app.models.review_queue import ReviewQueue


class AnalyticsService:

    @staticmethod
    def get_dashboard(db):

        total_messages = db.query(
            Message
        ).count()

        total_reviews = db.query(
            ReviewQueue
        ).count()

        avg_confidence = db.query(
            func.avg(
                TriageResult.confidence
            )
        ).scalar()

        return {
            "total_messages":
                total_messages,

            "review_queue":
                total_reviews,

            "average_confidence":
                round(
                    avg_confidence or 0,
                    2
                )
        }
    
 # ==========================
    # PHASE 9.2
    # ==========================

    @staticmethod
    def category_stats(db):

        rows = db.query(
            TriageResult.category,
            func.count(
                TriageResult.id
            )
        ).group_by(
            TriageResult.category
        ).all()

        result = {}

        for category, count in rows:

            result[category] = count

        return result
    


    @staticmethod
    def priority_stats(db):

        rows = db.query(
        TriageResult.priority,
        func.count(
            TriageResult.id
        )
        ).group_by(
        TriageResult.priority
         ).all()

        result = {}
 
        for priority, count in rows:

         result[priority] = count

        return result