class RiskEngine:

    @staticmethod
    def evaluate(result):

        category = result.get(
            "category",
            ""
        )

        priority = result.get(
            "priority",
            ""
        )

        if priority == "P0":
            return "HIGH"

        if category == "security":
            return "HIGH"

        if priority == "P1":
            return "MEDIUM"

        return "LOW"