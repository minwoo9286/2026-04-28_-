import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ── 1) 텍스트 생성 테스트 ─────────────────────────────────────────────────────
print("=" * 50)
print("[1] 텍스트 생성 테스트 - qwen/qwen3.6-plus:free")
print("=" * 50)

text_payload = {
    "model": "qwen/qwen3.6-plus:free",
    "messages": [
        {"role": "user", "content": "안녕하세요! 오늘 점심 메뉴 추천해줘. 한 줄로 짧게."}
    ]
}

res = requests.post(BASE_URL, headers=HEADERS, json=text_payload)
if res.status_code == 200:
    answer = res.json()["choices"][0]["message"]["content"]
    print(f"응답: {answer}")
else:
    print(f"오류 {res.status_code}: {res.text}")

# ── 2) 이미지 인식 테스트 ─────────────────────────────────────────────────────
print()
print("=" * 50)
print("[2] 이미지 인식 테스트 - google/gemma-3-27b-it:free")
print("=" * 50)

# 공개 이미지 URL로 테스트 (고양이 사진)
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/320px-Cat03.jpg"

image_payload = {
    "model": "google/gemma-3-27b-it:free",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "이 이미지에 무엇이 보이나요? 한국어로 한 줄로 설명해줘."},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ]
}

res2 = requests.post(BASE_URL, headers=HEADERS, json=image_payload)
if res2.status_code == 200:
    answer2 = res2.json()["choices"][0]["message"]["content"]
    print(f"이미지 URL: {image_url}")
    print(f"응답: {answer2}")
else:
    print(f"오류 {res2.status_code}: {res2.text}")

print()
print("테스트 완료!")
