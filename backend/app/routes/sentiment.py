# backend/app/routes/sentiment.py
from fastapi import APIRouter
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.llms.generate import get_sentiment

router = APIRouter()

@router.post("/", response_model=SentimentResponse)  # Changed from "/sentiment-analysis" to "/"
async def analyze_sentiment(request: SentimentRequest):
    # Get sentiment analysis result
    result = await get_sentiment(request)
    
    return SentimentResponse(
        message=result["message"],
        sentiment=result["sentiment"],
        confidence=result["confidence"]
    )