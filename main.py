from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from schemas import AnalyzeRequest, AnalyzeResponse
from services.sentiment import analyze_sentiment
from services.keywords import extract_keywords
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Text Analysis API",
    description="A lightweight API for sentiment analysis and keyword extraction.",
    version="1.0.0"
)

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_text(request: AnalyzeRequest):
    logger.info("Received analysis request")
    
    try:
        sentiment_result = await run_in_threadpool(analyze_sentiment, request.text)
        keywords_result = await run_in_threadpool(extract_keywords, request.text)

        return AnalyzeResponse(
            sentiment=sentiment_result["sentiment"],
            polarity_score=sentiment_result["polarity_score"],
            keywords=keywords_result
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
def health_check():
    return {"status": "operational", "version": "1.0.0"}