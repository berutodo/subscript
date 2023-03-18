from fastapi import FastAPI, File, UploadFile, Response
from moviepy.editor import *

app = FastAPI()
@app.get("/")
async def hello_world():
    return "Hello World"

@app.get("/another")
async def another_route():
    return "Another Route"