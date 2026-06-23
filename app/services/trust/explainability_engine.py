class ExplainabilityEngine:

    @staticmethod
    def generate(
        message,
        result
    ):

        explanations = []

        text = message.lower()

        if "hack" in text:
            explanations.append(
                "security_keyword_detected"
            )

        if "refund" in text:
            explanations.append(
                "refund_keyword_detected"
            )

        if "payment" in text:
            explanations.append(
                "payment_keyword_detected"
            )

        explanations.append(
            f"predicted_category:{result['category']}"
        )

        explanations.append(
            f"predicted_priority:{result['priority']}"
        )

        return explanations