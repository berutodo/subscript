from fastapi import FastAPI, File, UploadFile, Response
from moviepy.editor import *

app = FastAPI()

@app.post("/audio")
async def convert_video_to_audio(file: UploadFile = File(...)):
    video = VideoFileClip(file.file.name)
    audio = video.audio
    audio_file = f"{file.filename.split('.')[0]}.mp3"
    audio.write_audiofile(audio_file)
    response = Response(content=open(audio_file, "rb").read())
    response.headers["Content-Disposition"] = f"attachment; filename={audio_file}"
    return response

@app.post("/")
async def hello_world():
    return print('Hello World')