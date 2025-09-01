class FeedbackAnalyzer:
    def __init__(self, config):
        self.config = config

    def generate_feedback(self, text: str) -> dict:
        words = text.split()
        return {
            "word_count": len(words),
            "message": "Demo feedback: keep practicing!"
        }
