# test_weather.py

from bot import get_weather

def test_valid_city():
    result = get_weather("Київ")
    assert "Погода в Київ" in result

def test_invalid_city():
    result = get_weather("Невідомемісто12345")
    assert "Не вдалося отримати погоду" in result
