# ====================
# src/utils.py
# ====================
import os
from openai import OpenAI


class ChatGPTConnector():

    def __init__(self,
                 api_key=None,
                 model_name: str = 'gpt-4.1-mini',
                 temperature: float = 0.0,
                 top_p: float = 1.0,
                 max_tokens: int = 512):
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
    
    def generate(self, messages, functions=None) -> any:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
            functions=functions
        )
        return response.choices[0].message