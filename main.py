<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
=======
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
>>>>>>> fe04360e4533af6d70982d128416b446990ebc21
    return {"message": "クラウドでPythonが動いています"}