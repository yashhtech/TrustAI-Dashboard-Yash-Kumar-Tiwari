from app.models.review_queue import ReviewQueue


class ReviewService:

    @staticmethod
    def add_to_queue(
        db,
        message,
        category,
        priority,
        confidence
    ):

        item = ReviewQueue(
            message=message,
            ai_category=category,
            ai_priority=priority,
            ai_confidence=str(confidence)
        )

        db.add(item)

        db.commit()

        db.refresh(item)

        return item