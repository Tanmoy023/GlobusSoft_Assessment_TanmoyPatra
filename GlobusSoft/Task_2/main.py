# run the server: uvicorn main:app --reload

from fastapi import FastAPI
from Drone_Count_Detection import detect_drone

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Drone Detection API running"}


@app.get("/detect")
def detect():
    result = detect_drone()
    return result
