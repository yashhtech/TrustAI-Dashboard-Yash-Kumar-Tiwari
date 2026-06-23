import re


class CodeDetector:

    @staticmethod
    def detect(text: str):

        patterns = [
            r"def\s+\w+\(",
            r"class\s+\w+",
            r"import\s+\w+",
            r"SELECT\s+",
            r"INSERT\s+",
            r"UPDATE\s+",
            r"DELETE\s+",
            r"while\s*\(",
            r"for\s*\("
        ]

        for pattern in patterns:

            if re.search(pattern, text, re.IGNORECASE):
                return True

        return False