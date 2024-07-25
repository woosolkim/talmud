from crewai_tools import BaseTool
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import Any
import deepl
from langdetect import detect
import os


class EmotionAnalysisTool(BaseTool):
    name: str = "Emotion Analysis Tool"
    description: str = "Analyzes the emotional content of a given text using TextBlob and NLTK"

    def _run(self, text: str) -> str:
        client = deepl.Translator(auth_key=os.getenv('DEEPL_API_KEY'))
        detected_lang = detect(text)
        if detected_lang != 'en':
            translation = client.translate_text(text, target_lang='EN-US')
            translationtext = translation.text
        else:
            translationtext = text

        blob = TextBlob(translationtext)
        sia = SentimentIntensityAnalyzer()
        
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        nltk_sentiment = sia.polarity_scores(translationtext)
        
        result = f"""
        TextBlob Analysis:
        - Polarity: {polarity} (-1 very negative, 1 very positive)
        - Subjectivity: {subjectivity} (0 very objective, 1 very subjective)

        NLTK Analysis:
        - Negative: {nltk_sentiment['neg']}
        - Neutral: {nltk_sentiment['neu']}
        - Positive: {nltk_sentiment['pos']}
        - Compound: {nltk_sentiment['compound']}

        Interpretation:
        The text has a {'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'} tone overall.
        It is {'highly' if subjectivity > 0.5 else 'somewhat' if subjectivity > 0.3 else 'not very'} subjective.
        """
        return result

    def _parse_input(self, text: str) -> Any:
        """Parse the input string."""
        return text