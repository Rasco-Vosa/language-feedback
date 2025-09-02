from src.config_loader import Config
from src.audio_transcriber import AudioTranscriber
# from src.feedback_analyzer import FeedbackAnalyzer
# from src.feedback_formatter import FeedbackFormatter

class LanguageFeedbackApp:
    def __init__(self):
        self.config = Config()
        self.transcriber = AudioTranscriber()
        # self.analyzer = FeedbackAnalyzer(self.config)
        # self.formatter = FeedbackFormatter()

    def run(self, audio_file_path: str):
        # Step 1 - Audio Transcription
        transcript = self.transcriber.trascribe_audio(audio_file_path, test=False)
        print("Transcript:", transcript)
        if not transcript:
            print("Audio couldn't be transcribed")
            return

        # # Step 2 - Analyze transcript + audio
        # feedback = self.analyzer.generate_feedback(transcript, audio_file_path)

        # # Step 3 - Format Output
        # formatted = self.formatter.format(feedback)

        # # Step 4 - Print Feedback
        # print("Feedback: ", formatted)

if __name__ == "__main__":
    app = LanguageFeedbackApp()
    app.run("data/raw/audio_test.wav")
