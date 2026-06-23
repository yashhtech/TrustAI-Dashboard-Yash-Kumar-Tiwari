# app/services/validators/category_validator.py

class CategoryValidator:

    VALID_CATEGORIES = {
        "complaint",
        "refund",
        "billing",
        "technical_issue",
        "account",
        "shipping",
        "cancellation",
        "inquiry",
        "feedback",
        "security",
        "code_support",
        "other"
    }

    MAPPINGS = {
        "delivery_problem": "shipping",
        "delivery": "shipping",
        "bug": "technical_issue",
        "tech": "technical_issue",
        "payment": "billing",
        "hacking": "security"
    }

    @staticmethod
    def validate(category):

        if not category:
            return "other"

        category = category.lower().strip()

        if category in CategoryValidator.VALID_CATEGORIES:
            return category

        if category in CategoryValidator.MAPPINGS:
            return CategoryValidator.MAPPINGS[category]

        return "other"