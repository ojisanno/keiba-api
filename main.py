from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "クラウドでPythonが動いています"}

from fastapi import FastAPI, HTTPException
import httpx

@app.get("/odds/history")
async def odds_history(race_id: str):
    # 本来はスクレイピングするが、まずはダミーでOK
    return [
        {
            "horseName": "サンプルホースA",
            "oddsHistory": [
                {"time": "2024-01-01T12:00:00", "odds": 2.4},
                {"time": "2024-01-01T12:05:00", "odds": 2.3},
                {"time": "2024-01-01T12:10:00", "odds": 2.1},
            ]
        },
        {
            "horseName": "サンプルホースB",
            "oddsHistory": [
                {"time": "2024-01-01T12:00:00", "odds": 5.8},
                {"time": "2024-01-01T12:05:00", "odds": 6.0},
                {"time": "2024-01-01T12:10:00", "odds": 6.4},
            ]
        }
    ]
