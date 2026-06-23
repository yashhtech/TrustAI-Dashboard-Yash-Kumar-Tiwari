import re


class PIIDetector:

    @staticmethod
    def detect(text: str):

        findings = []

        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        phone_pattern = r"\b\d{10}\b"

        pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"

        aadhaar_pattern = r"\b\d{12}\b"

        if re.search(email_pattern, text):
            findings.append("email")

        if re.search(phone_pattern, text):
            findings.append("phone")

        if re.search(pan_pattern, text):
            findings.append("pan")

        if re.search(aadhaar_pattern, text):
            findings.append("aadhaar")

        return findings