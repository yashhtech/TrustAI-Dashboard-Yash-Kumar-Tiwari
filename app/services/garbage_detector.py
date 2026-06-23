import re


class GarbageDetector:

    @staticmethod
    def detect(text: str):

        text = text.strip()

        if len(text) < 3:
            return True

        letters = re.findall(r"\w", text, re.UNICODE)

        if len(letters) < 2:
            return True

        return False