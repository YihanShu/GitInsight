import requests

r = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "hello",
        "stream": False
    },
    timeout=30
)

print(r.status_code)
print(r.text)