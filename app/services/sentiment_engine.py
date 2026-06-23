class SentimentEngine:

    POSITIVE_WORDS = [
        "good",
        "great",
        "excellent",
        "awesome",
        "thank you",
        "happy",
        "satisfied",
        "amazing",
        "love"
    ]

    NEGATIVE_WORDS = [
        "bad",
        "terrible",
        "angry",
        "frustrated",
        "hacked",
        "issue",
        "problem",
        "disappointed",
        "poor",
        "worst",
        "kill",
        "murder",
        "attack",
        "bomb",
        "shoot",
        "die",
        "threat"
    ]

    @staticmethod
    def detect(message):

        text = message.lower()

        positive_score = 0
        negative_score = 0

        for word in SentimentEngine.POSITIVE_WORDS:

            if word in text:
                positive_score += 1

        for word in SentimentEngine.NEGATIVE_WORDS:

            if word in text:
                negative_score += 1

        if positive_score > negative_score:
            return "positive"

        if negative_score > positive_score:
            return "negative"

        return "neutral"