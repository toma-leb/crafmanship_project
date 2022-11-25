from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main_success():
    response = client.put("http://localhost:8080/api/words", json={
        "w": "key-hello",
        "t": [
            {"language": "en", "translation": "hello"},
            {"language": "fr", "translation": "bonjour"},
            {"language": "it", "translation": "ciao"},
        ]
    })
    print(response)
    assert response.status_code == 201
    assert response.json() == {"w": "key-hello",
                               "t": [
                                   {"language": "en", "translation": "hello"},
                                   {"language": "fr", "translation": "bonjour"},
                                   {"language": "it", "translation": "ciao"},
                               ],
                               "url": "http://localhost:8080/api/words/key-hello"
                               }


def test_read_main_fail():

    response = client.put("/api/words")
    assert response.status_code == 201
    assert response.json() == {"w": "key-hello",
                               "t": [
                                   {"language": "en", "translation": "hello"},
                                   {"language": "fr", "translation": "bonjour"},
                                   {"language": "it", "translation": "ciao"},
                               ],
                               "url": "http://localhost:8080/api/words/key-hello"
                               }


test_read_main_success()
