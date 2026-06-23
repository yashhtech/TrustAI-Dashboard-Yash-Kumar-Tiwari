class PromptInjectionDetector:

    SUSPICIOUS_PATTERNS = [
        "ignore previous instructions",
        "forget instructions",
        "act as",
        "system prompt",
        "override",
        "developer mode",
        "jailbreak",
        "ignore all rules",
        "you are chatgpt"
    ]

    @staticmethod
    def detect(text: str):

        text = text.lower()

        for pattern in PromptInjectionDetector.SUSPICIOUS_PATTERNS:

            if pattern in text:
                return True

        return False