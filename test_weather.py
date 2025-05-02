# test_weather.py
from unittest.mock import patch
from bot import get_weather

@patch("bot.requests.get")
def test_valid_city(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "main": {"temp": 21.5},
        "weather": [{"description": "ясно"}],
    }

    result = get_weather("Київ")
    assert "Погода в Київ" in result
    assert "21.5" in result

def test_invalid_city():
    result = get_weather("Невідомемісто12345")
    assert "Не вдалося отримати погоду" in result
