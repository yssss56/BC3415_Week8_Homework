from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text using TextBlob and returns the sentiment label.

    Args:
    - text (str): The input text to analyze.

    Returns:
    - str: The sentiment label, e.g., "Positive", "Negative", or "Neutral".
    """
    # Analyze the text using TextBlob
    analysis = TextBlob(text)
    
    # Classify based on the polarity score
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"
