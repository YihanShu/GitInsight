import requests
import json


class LLMClient:

    def __init__(self, use_mock=False, model="llama3"):
        self.use_mock = False
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"
    def analyze_diff(self, prompt):

        # =====================
        # MOCK模式
        # =====================
        print(self.use_mock)
        if self.use_mock:
            return """
            {
                "module": "Battery",
                "summary": "增加Battery Retry机制",
                "impact": "提高稳定性",
                "risk": "Medium"
            }
            """

        # =====================
        # OLLAMA真实调用
        # =====================
        try:
            response = requests.post(
                self.base_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=180
            )

            data = response.json()

            return data["response"]

        except Exception as e:
            return json.dumps({
                "module": "Unknown",
                "summary": f"Ollama调用失败: {str(e)}",
                "impact": "Unknown",
                "risk": "Medium"
            })
