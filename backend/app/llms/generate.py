from typing import Dict, Any
import json
from openai import OpenAI
from app.config import model
from app.schemas.sentiment import SentimentRequest
from app.llms.prompts.base_prompts import get_sentiment_system_prompt, create_sentiment_user_prompt
from datetime import datetime

class SentimentAnalyzer:
    def __init__(self):
        self.client = OpenAI()
        
    async def get_sentiment(self, request: SentimentRequest) -> Dict[str, Any]:
        # Get prompts from our prompt library
        system_prompt = get_sentiment_system_prompt()
        user_prompt = create_sentiment_user_prompt(request.text)
        
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "text_length": len(request.text)
        }
        
        try:
            completion = self.client.chat.completions.create(
                model=model,  # Fixed the model name from gpt-4o to gpt-4
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=300,
                response_format={"type": "json_object"}
            )

            content = completion.choices[0].message.content.strip()
            
            try:
                parsed_content = json.loads(content)
                return {
                    "message": "success",
                    "sentiment": parsed_content["sentiment"],
                    "confidence": parsed_content["confidence"],
                }
                
            except json.JSONDecodeError as json_err:
                error_response = {
                    "message": "error",
                    "sentiment": "Unknown",
                    "confidence": 0.0,
                }
                return error_response

        except Exception as e:
            error_response = {
                "message": "error",
                "sentiment": "Unknown",
                "confidence": 0.0,
            }
            return error_response

# Create a singleton instance
sentiment_analyzer = SentimentAnalyzer()

# Function to be called from the route
async def get_sentiment(request: SentimentRequest) -> Dict[str, Any]:
    return await sentiment_analyzer.get_sentiment(request)