import librosa
import numpy as np

class AudioFeatureExtractor:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def extract_features(self, file_path: str) -> dict:
        y, sr = librosa.load(file_path, sr=self.sample_rate)

        # Duration
        duration = librosa.get_duration(y=y, sr=sr)

        # Pitch (fundamental frequency estimate)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch_values = pitches[magnitudes > np.median(magnitudes)]
        avg_pitch = float(np.mean(pitch_values)) if len(pitch_values) > 0 else 0
        pitch_var = float(np.var(pitch_values)) if len(pitch_values) > 0 else 0

        # Energy (loudness proxy)
        rms = float(librosa.feature.rms(y=y).mean())

        # Pauses (low energy segments)
        silence_threshold = 0.01
        silent_frames = np.sum(librosa.feature.rms(y=y) < silence_threshold)

        return {
            "duration_sec": duration,
            "avg_pitch": avg_pitch,
            "pitch_variance": pitch_var,
            "loudness": rms,
            "silent_frames": int(silent_frames),
        }
