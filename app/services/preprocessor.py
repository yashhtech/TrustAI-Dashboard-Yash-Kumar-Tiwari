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

            return translated if translated else text

        except Exception:
            return text

    @staticmethod
    def clean_text(text: str):
        text = text.strip()
        text = re.sub(r"\s+", " ", text)
        return text

    # 🔥 NEW FUNCTION (MOST IMPORTANT)
    @staticmethod
    def process(text: str):
        cleaned = Preprocessor.clean_text(text)

        language = Preprocessor.detect_language(cleaned)

        translated = Preprocessor.translate_to_english(
            cleaned,
            language
        )

        return {
            "cleaned": cleaned,
            "translated": translated,
            "language": language
        }