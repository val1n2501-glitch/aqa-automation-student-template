import os

import requests


def test_health():
    base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    response = requests.get(f"{base_url}/api/health", timeout=5)
    assert response.status_code == 200
