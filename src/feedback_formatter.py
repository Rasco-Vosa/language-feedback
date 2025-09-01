class FeedbackFormatter:
    def __init__(self):
        pass

    def format(self, feedback: dict) -> str:
        return f"Word count: {feedback['word_count']}\nMessage: {feedback['message']}"
