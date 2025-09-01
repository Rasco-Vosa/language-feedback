from src.config_loader import Config
from src.audio_transcriber import AudioTranscriber
from src.feedback_analyzer import FeedbackAnalyzer
from src.feedback_formatter import FeedbackFormatter

class LanguageFeedbackApp:
    def __init__(self):
        self.config = Config()
        self.input_handler = AudioTranscriber()
        self.analyzer = FeedbackAnalyzer(self.config)
        self.formatter = FeedbackFormatter()

    def run(self, text_file_path: str):
        # Step 1 - Audio Transcription
        transcript = self.input_handler.trascribe_audio(text_file_path)
        print("Transcript:", transcript)
        if not transcript:
            print("Audio couldn't be transcribed")
            return

        # Step 2 - Analyze transcript
        feedback = self.analyzer.generate_feedback(transcript)

        # Step 3 - Format Outup 
        formatted = self.formatter.format(feedback)

        # Step 4 - Print Feedback
        print("Feedback: ", formatted)

if __name__ == "__main__":
    app = LanguageFeedbackApp()
    app.run("data/raw/audio_test.wav")
