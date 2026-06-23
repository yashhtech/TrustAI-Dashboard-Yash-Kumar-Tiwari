class ConfidenceEngine:

    @staticmethod
    def evaluate(result):

        confidence = float(
            result.get(
                "confidence",
                0.50
            )
        )

        category = result.get(
            "category",
            ""
        )

        priority = result.get(
            "priority",
            ""
        )

        # confidence boost
        if category != "other":
            confidence += 0.02

        if priority == "P0":
            confidence += 0.03

        # human review logic
        if confidence < 0.60:
            result["needs_human"] = True

        confidence = max(
            0.0,
            min(confidence, 1.0)
        )

        result["confidence"] = round(
            confidence,
            2
        )

        return result