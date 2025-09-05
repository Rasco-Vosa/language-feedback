from src.analysis.audio_features import AudioFeatureExtractor
from src.analysis.text_features import TextFeatureExtractor
from src.analysis.scoring import ScoringEngine

class FeedbackAnalyzer:
    def __init__(self, config):
        self.config = config
        self.audio_extractor = AudioFeatureExtractor()
        self.text_extractor = TextFeatureExtractor()
        self.scorer = ScoringEngine()

    def generate_feedback(self, transcript: str, audio_file: str) -> dict:
        # Extract features
        audio_features = self.audio_extractor.extract_features(audio_file)
        text_features = self.text_extractor.extract_features(transcript)

        # Compute scores
        scores = self.scorer.compute_scores(audio_features, text_features)

        return {
            "audio_features": audio_features,
            "text_features": text_features,
            "scores": scores,
        }
