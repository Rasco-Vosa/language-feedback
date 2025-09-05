import re
from collections import Counter
import language_tool_python

class TextFeatureExtractor:
    def __init__(self, lang="en-US"):
        self.tool = language_tool_python.LanguageToolPublicAPI(lang)

    def extract_features(self, transcript: str) -> dict:
        words = re.findall(r"\b\w+\b", transcript.lower())
        word_count = len(words)
        unique_words = len(set(words))
        word_freq = Counter(words).most_common(5)

        # Grammar issues
        matches = self.tool.check(transcript)
        grammar_issues = len(matches)

        return {
            "word_count": word_count,
            "unique_words": unique_words,
            "most_common_words": word_freq,
            "grammar_issues": grammar_issues,
            "grammar_suggestions": [m.message for m in matches[:5]],
        }
