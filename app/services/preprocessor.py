import re
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

from deep_translator import GoogleTranslator


class Preprocessor:

    @staticmethod
    def detect_language(text: str):

        try:
            return detect(text)

        except LangDetectException:
            return "unknown"

        except Exception:
            return "unknown"

    @staticmethod
    def translate_to_english(text: str, language: str):

        if language in ["en", "unknown"]:
            return text

        try:

            translated = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(text)

            if translated:
                return translated

            return text

        except Exception:
            return text

    @staticmethod
    def clean_text(text: str):

        text = text.strip()

        text = re.sub(r"\s+", " ", text)

        return text