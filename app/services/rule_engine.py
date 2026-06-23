class RuleEngine:

    HIGH_PRIORITY_KEYWORDS = [
        "fraud",
        "hack",
        "hacked",
        "security",
        "stolen",
        "payment failed",
        "chargeback",
        "legal"
    ]

    @staticmethod
    def override(message, result):

        msg = message.lower()

        for keyword in RuleEngine.HIGH_PRIORITY_KEYWORDS:

            if keyword in msg:

                result["priority"] = "P0"

                result["needs_human"] = True

                result["confidence"] = 1.0

        return result