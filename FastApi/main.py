from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")

async def root():
    return "Hola Elias"


@app.get("/url")
async def root():
    return {"url de hbo max: https://play.max.com/"}