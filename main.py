from src.config_loader import Config
from src.input_handler import InputHandler
from src.feedback_analyzer import FeedbackAnalyzer
from src.feedback_formatter import FeedbackFormatter

class LanguageFeedbackApp:
    def __init__(self):
        self.config = Config()
        self.input_handler = InputHandler()
        self.analyzer = FeedbackAnalyzer(self.config)
        self.formatter = FeedbackFormatter()

    def run(self, text_file_path: str):
        text = self.input_handler.load_text(text_file_path)
        feedback = self.analyzer.generate_feedback(text)
        formatted = self.formatter.format(feedback)
        print("\n=== Feedback ===")
        print(formatted)

if __name__ == "__main__":
    app = LanguageFeedbackApp()
    app.run("data/raw/sample.txt")
