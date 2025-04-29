"""Dynamic user-prompt template"""

from __future__ import annotations
from typing import Dict, Any
import json

def create_user_prompt(
    age: int,
    height: float,
    weight: float,
    health_score: float,
    biological_age: float,
    bmi: float,
    risk_category: str,
    assessment_data: Dict[str, Any]
) -> str:
    """
    Packs *only* the raw facts that the LLM needs.
    """
    return f"""
PATIENT DATA
• Age: {age}
• Height: {height} cm
• Weight: {weight} kg
• BMI: {bmi}
• Health Score: {health_score}
• Biological Age: {biological_age}
• Risk Category: {risk_category}

ASSESSMENT ANSWERS (JSON)
{json.dumps(assessment_data, indent=2)}

Follow the SYSTEM instructions and emit the required JSON.
"""
