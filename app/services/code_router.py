class CodeRouter:

    @staticmethod
    def route(contains_code, result):

        if contains_code:

            result["category"] = "code_support"

            if result["priority"] == "P3":
                result["priority"] = "P2"

        return result