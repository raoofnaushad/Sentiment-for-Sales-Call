import os
from datetime import datetime
from typing import Dict, Any
import json
from pathlib import Path

class PromptManager:
    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = Path(prompts_dir)
        self.prompts_dir.mkdir(exist_ok=True)
        
    def save_prompt(
        self,
        system_message: str,
        user_prompt: str,
        metadata: Dict[str, Any] = None
    ) -> str:
        """Save prompt to file with metadata"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'prompt_{timestamp}.json'
        filepath = self.prompts_dir / filename
        
        prompt_data = {
            "system_message": system_message,
            "user_prompt": user_prompt,
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(prompt_data, f, indent=2)  # Fixed: positional argument f comes before keyword argument indent
            
        self._cleanup_old_prompts()
        return str(filepath)
    
    def _cleanup_old_prompts(self, keep_latest: int = 5):
        """Cleanup old prompt files"""
        files = sorted(self.prompts_dir.glob('prompt_*.json'))
        for old_file in files[:-keep_latest]:
            old_file.unlink()