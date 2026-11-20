from datetime import timedelta
from app import checker
import requests


class FakeResponse:
    def __init__(self, status_code):
        self.status_code = status_code
        self.elapsed = timedelta(seconds=0.5)


def test_check_site_up(monkeypatch):
    def fake_get(url, timeout):
        return FakeResponse(200)

    monkeypatch.setattr(checker.requests, "get", fake_get)

    result = checker.check_site("https://ejemplo.com")

    assert result == "[UP]   HTTP 200 | 0.50 s | https://ejemplo.com"

def test_check_site_500(monkeypatch):
    def fake_get(url, timeout):
        return FakeResponse(500)

    monkeypatch.setattr(checker.requests, "get", fake_get)

    result = checker.check_site("https://ejemplo.com")

    assert result == "[DOWN] HTTP 500 | https://ejemplo.com"

def test_check_site_timeout(monkeypatch):
    def fake_get(url, timeout):
        raise requests.Timeout

    monkeypatch.setattr(checker.requests, "get", fake_get)

    result = checker.check_site("https://ejemplo.com")

    assert result == "[DOWN] TIMEOUT | https://ejemplo.com"