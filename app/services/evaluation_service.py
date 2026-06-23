from collections import defaultdict
from app.services.ollama_service import OllamaService


class EvaluationService:

    @staticmethod
    def evaluate():

        # 🔥 Better ground truth (realistic dataset)
        ground_truth = [
            {"message": "my account hacked", "category": "security"},
            {"message": "payment failed", "category": "billing"},
            {"message": "refund not received", "category": "billing"},
            {"message": "order delayed", "category": "shipping"},
            {"message": "app is crashing", "category": "technical"},
            {"message": "i love your service", "category": "feedback"},
        ]

        correct = 0
        total_confidence = 0

        category_stats = defaultdict(lambda: {"correct": 0, "total": 0})

        results = []

        for item in ground_truth:

            msg = item["message"]
            expected = item["category"]

            res = OllamaService.classify(msg)

            predicted = res.get("category")
            confidence = float(res.get("confidence", 0))

            is_correct = predicted == expected

            if is_correct:
                correct += 1

            total_confidence += confidence

            category_stats[expected]["total"] += 1
            if is_correct:
                category_stats[expected]["correct"] += 1

            results.append({
                "message": msg,
                "expected": expected,
                "predicted": predicted,
                "confidence": confidence,
                "correct": is_correct
            })

        total = len(ground_truth)

        # 🔥 category-wise accuracy
        category_accuracy = {
            cat: round(v["correct"] / v["total"], 2)
            for cat, v in category_stats.items()
        }

        return {
            "accuracy": round(correct / total, 2),
            "average_confidence": round(total_confidence / total, 2),
            "total": total,
            "correct": correct,
            "category_accuracy": category_accuracy,
            "details": results
        }