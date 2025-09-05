class ScoringEngine:
    def __init__(self):
        pass

    def compute_scores(self, audio_features: dict, text_features: dict) -> dict:
        # Fluency: words per minute (rough proxy)
        duration_min = audio_features["duration_sec"] / 60 if audio_features["duration_sec"] > 0 else 1
        wpm = text_features["word_count"] / duration_min

        # Pronunciation proxy: grammar issues + silent frames
        pronunciation_score = max(0, 100 - (text_features["grammar_issues"] * 5) - (audio_features["silent_frames"] * 0.1))

        # Fluency score: optimal speaking rate ~120-160 wpm
        if wpm < 80:
            fluency_score = max(0, (wpm / 80) * 100)
        elif wpm > 180:
            fluency_score = max(0, (180 / wpm) * 100)
        else:
            fluency_score = 100

        # Intonation: based on pitch variance (higher = more natural)
        intonation_score = min(100, audio_features["pitch_variance"] * 10)

        # Vocabulary richness
        vocab_ratio = text_features["unique_words"] / text_features["word_count"] if text_features["word_count"] > 0 else 0
        vocab_score = vocab_ratio * 100

        # Grammar score
        grammar_score = max(0, 100 - (text_features["grammar_issues"] * 5))

        # Overall score = weighted average
        overall = round((
            0.25 * pronunciation_score +
            0.25 * fluency_score +
            0.20 * intonation_score +
            0.15 * grammar_score +
            0.15 * vocab_score
        ), 1)

        return {
            "pronunciation": round(pronunciation_score, 1),
            "fluency": round(fluency_score, 1), 
            "intonation": round(intonation_score, 1),
            "grammar": round(grammar_score, 1),
            "vocabulary": round(vocab_score, 1),
            "overall": overall,
            "words_per_minute": round(wpm, 1)
        }
