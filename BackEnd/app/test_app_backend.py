import requests

def test_home():
    response = requests.get("http://localhost:00/")
    assert response.status_code == 200
    assert response.json() == {"health_check":"OK","model_version":"0.5.0"}

def test_predict():
    response = requests.post("http://localhost:80/predict", json={"text": "test text"})
    assert response.status_code == 200
    assert "language" in response.json()
