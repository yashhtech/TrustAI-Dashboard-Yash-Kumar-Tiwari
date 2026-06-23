import ollama

from app.core.config import settings
from app.services.json_repair import JSONRepair
from app.services.prompt_templates import TRIAGE_PROMPT


class OllamaService:

    @staticmethod
    def classify(message):

        prompt = TRIAGE_PROMPT.format(
            message=message
        )

        response = ollama.chat(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response["message"]["content"]

        repaired = JSONRepair.repair(
            content
        )

        if repaired:
            return repaired

        return {
            "category": "other",
            "priority": "P2",
            "summary": "AI parsing failed",
            "suggested_action": "Manual review required",
            "needs_human": True,
            "confidence": 0.0
        }