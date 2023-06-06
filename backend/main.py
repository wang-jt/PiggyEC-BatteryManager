
from fastapi import FastAPI
import uvicorn
from init import *

app = FastAPI()

@app.get("/")
async def index():
    return {"name": "a"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5555)