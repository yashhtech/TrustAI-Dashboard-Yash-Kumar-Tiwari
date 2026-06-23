from app.models.audit_log import AuditLog
class SecurityEngine:

    SECURITY_WORDS = [
        "hack", "hacked", "fraud", "chargeback",
        "security", "breach", "unauthorized", "stolen",
        "legal", "kill", "murder", "attack", "bomb",
        "shoot", "die", "threat"
    ]

    @staticmethod
    def evaluate(message, result):

        msg = message.lower()
        triggered = []

        for word in SecurityEngine.SECURITY_WORDS:
            if word in msg:
                triggered.append(word)

        if triggered:
            # 🔥 Override decision
            result["category"] = "security"
            result["priority"] = "P0"
            result["needs_human"] = True
            result["confidence"] = 1.0
            result["risk_level"] = "HIGH"

            # 🧠 Explainability (VERY IMPORTANT FOR SCORE)
            if "explanation" not in result:
                result["explanation"] = []

            result["explanation"].append(
                f"security_keywords_detected:{','.join(triggered)}"
            )
            result["audit_event"] = "SECURITY_OVERRIDE"

        return result