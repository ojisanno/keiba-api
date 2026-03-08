from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "クラウドでPythonが動いています"}