"""
Sentiment Analysis Prompts
=========================
This module contains the prompts for sentiment analysis
"""
from __future__ import annotations

# Response structure that the model must follow
SENTIMENT_RESPONSE_STRUCTURE = {
    "sentiment": "string (Positive/Negative/Neutral)",
    "confidence": "float (0-1)",
}

# Few shot examples to guide the model
FEW_SHOT_EXAMPLES = [
    {
        "input": "The training modules provided by AlertDriving are fantastic. Our drivers found them engaging, and we have already noticed a reduction in minor incidents. The localized content really helped our teams across different regions feel connected and understood.",
        "output": {
            "sentiment": "Positive",
            "confidence": 0.95,
        }
    },
    {
        "input": "While the FleetDefense® platform has good intentions, we found the interface quite outdated and difficult to navigate. Our team faced several issues trying to access some of the modules, and support response times were slower than we expected.",
        "output": {
            "sentiment": "Neutral",
            "confidence": 0.85,
        }
    },
    {
        "input": "The content of the Hazard Perception 360 training was very informative, but some of our drivers mentioned that the scenarios did not always feel applicable to their everyday driving experiences. However, the reporting tools have been a valuable addition for our managers.",
        "output": {
            "sentiment": "Neutral",
            "confidence": 0.75,
        }
    }
]

def get_sentiment_system_prompt() -> str:
    """
    Returns the system prompt for sentiment analysis
    """
    return f"""
    
## Context
- You are an AI assistant working for AlertDriving, a global leader in driver risk management solutions.
- Your primary task is to analyze customer's long feedback received by the Sales Team and identify the sentiment expressed in each response.

## Objective:
- Detect the overall sentiment of the customer's response: ➔ Positive, Neutral, or Negative.
- Also, give importance to any key emotional indicators (e.g., satisfaction, frustration, interest, hesitation).

##  Instructions:
- Analyze the full customer text carefully.
- Do not infer beyond what is clearly stated.
- Focus on the customer's tone, choice of words, and implied emotions.

## Important
- Avoid using customer metadata (like company name) to bias the sentiment.
- Most importantly always follows the json structure

RESPONSE FORMAT
-------------
You must respond in JSON format following this structure:
{SENTIMENT_RESPONSE_STRUCTURE}

EXAMPLES
--------
Here are some examples of analysis:
{FEW_SHOT_EXAMPLES}

GUIDELINES
---------
- Be objective and consistent
- Consider context and nuance
- Base confidence on clarity of sentiment
- Provide clear, concise explanations
"""

def create_sentiment_user_prompt(text: str) -> str:
    """
    Creates the user prompt for sentiment analysis
    """
    return f"""
Please analyze the sentiment of the following text:

TEXT
----
{text}

Important notes:
- Focus only on the text content without external assumptions.
Provide your analysis following the specified JSON format."""