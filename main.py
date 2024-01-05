import logging

import uvicorn
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.post("/test")
async def test(request_body: dict):
    logger.info(f"Request's body: {request_body}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
