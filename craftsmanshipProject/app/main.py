from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/api/words", status_code=201)
async def read_put():
    return {
        "w": "key-hello",
        "t": [
            {"language": "en", "translation": "hello"},
            {"language": "fr", "translation": "bonjour"},
            {"language": "it", "translation": "ciao"},
        ],
        "url": "http://localhost:8080/api/words/key-hello"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
