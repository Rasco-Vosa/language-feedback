from pathlib import Path
import speech_recognition as sr

class AudioTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()


    def load_text(self, file_path: str) -> str:
        path = Path(file_path)
        return path.read_text().strip()


    def trascribe_audio(self, file_path: str) -> str:
        audio_file = sr.AudioFile(file_path)
        with audio_file as audio_source:
            audio_data = self.recognizer.record(audio_source)

        try:
            transcript = self.recognizer.recognize_google(audio_data)
            return transcript
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Speech Recognition Api Error: {e}")
            return ""
        
