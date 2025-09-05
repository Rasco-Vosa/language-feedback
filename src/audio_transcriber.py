from pathlib import Path
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
from .config_loader import Config

class AudioTranscriber:
    def __init__(self, config):
        self.config = config
        self.config.load_creds()

        self.speech_config = speechsdk.SpeechConfig(
            subscription=os.getenv("AZURE_TTS_KEY"),
            region=self.config.get_setting("azure_region")
        )

    def load_text(self, file_path: str) -> str:
        path = Path(file_path)
        return path.read_text().strip()

    def trascribe_audio(self, file_path: str, test:bool = False) -> str:

        audio_config = speechsdk.audio.AudioConfig(filename=file_path)
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            audio_config=audio_config
        )

        result = speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")
            return ""
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"Speech Recognition canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation.error_details}")
            return ""