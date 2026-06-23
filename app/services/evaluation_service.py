class EvaluationService:

    @staticmethod
    def evaluate():

        # dummy ground truth (you can change later)
        ground_truth = [
            {"message": "my account hacked", "category": "security"},
            {"message": "order delayed", "category": "shipping"},
            {"message": "refund not received", "category": "billing"},
        ]

        correct = 0

        for item in ground_truth:

            msg = item["message"]
            expected = item["category"]

            # simple test using your model
            from app.services.ollama_service import OllamaService

            res = OllamaService.classify(msg)

            if res.get("category") == expected:
                correct += 1

        total = len(ground_truth)

        return {
            "accuracy": round(correct / total, 2),
            "total": total,
            "correct": correct
        }