import openai
# openai.api_key = "API_KEY"
audio_file= open("./audio.wav", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)