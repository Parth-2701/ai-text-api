import yake

def extract_keywords(text: str, top_n: int = 5) -> list:
    """
    Extracts top keywords using YAKE.
    """
    kw_extractor = yake.KeywordExtractor(
        lan="en", 
        n=2,              # Max ngram size (1=word, 2=bigram)
        dedupLim=0.9,     # Deduplication threshold
        top=top_n, 
        features=None
    )
    
    keywords = kw_extractor.extract_keywords(text)
    # YAKE returns (keyword, score). Lower score = more relevant.
    # We only return the keyword string.
    return [kw[0] for kw in keywords]