# app/services/validators/priority_validator.py

class PriorityValidator:

    VALID_PRIORITIES = {
        "P0",
        "P1",
        "P2",
        "P3"
    }

    MAPPING = {
        "critical": "P0",
        "high": "P1",
        "medium": "P2",
        "low": "P3"
    }

    @staticmethod
    def validate(priority):

        if not priority:
            return "P2"

        priority = str(priority).strip()

        if priority in PriorityValidator.VALID_PRIORITIES:
            return priority

        lower = priority.lower()

        if lower in PriorityValidator.MAPPING:
            return PriorityValidator.MAPPING[lower]

        return "P2"