import json
from .base import BaseAnalyzer
from llm.client import LLMClient
from llm.prompts import build_prompt


class LLMAnalyzer(BaseAnalyzer):

    def __init__(self):
        self.llm = LLMClient()

    def analyze(self, commit, diff_text):

        prompt = build_prompt(commit, diff_text)

        result = self.llm.analyze_diff(prompt)

        try:
            return json.loads(result)
        except:
            return {
                "module": "Unknown",
                "summary": result[:200],
                "impact": "Unknown",
                "risk": "Medium"
            }