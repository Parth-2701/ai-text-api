from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes text polarity.
    Returns: label (str), score (float)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return {
        "sentiment": sentiment,
        "polarity_score": round(polarity, 2)
    }