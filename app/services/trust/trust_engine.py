class TrustEngine:

    @staticmethod
    def calculate(result):

        score = 100

        confidence = result.get(
            "confidence",
            0
        )

        if confidence < 0.90:
            score -= 10

        if confidence < 0.80:
            score -= 15

        if confidence < 0.70:
            score -= 20

        if result.get("needs_human"):
            score -= 20

        return max(score, 0)