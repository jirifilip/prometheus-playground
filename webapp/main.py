from fastapi import FastAPI
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
def index() -> str:
    return "Hello world"


@app.get("/dict")
def return_dict() -> dict[str, str]:
    return {"hello": "world", "bla": "ble", "bli": "blu"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
