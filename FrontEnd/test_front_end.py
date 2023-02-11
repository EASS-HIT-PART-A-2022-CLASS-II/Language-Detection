import os
import requests
import psycopg2
import json

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:mysecretpassword@localhost/postgres")

def test_api_request():
    url = "http://localhost/predict"

    payload = {"text": "Hello, World"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "language" in data

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("SELECT text, result FROM results ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    assert result is not None

    text, result_str = result
    result = json.loads(result_str)
    assert result == data

    conn.close()
