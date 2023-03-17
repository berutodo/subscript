import speech_recognition as sr

# Define o caminho do arquivo de áudio
audio_path = "./audio.wav"

# Inicializa o reconhecedor de fala
r = sr.Recognizer()

# Carrega o arquivo de áudio usando a biblioteca SpeechRecognition
with sr.AudioFile(audio_path) as source:
    audio = r.record(source)

# Faz a transcrição usando a API da OpenAI (Whisper)
openai_api_key = "API_KEY"
transcript = r.recognize_huggingface(audio, api_key=openai_api_key, model="facebook/wav2vec2-base-960h", language="en-US")

# Imprime a transcrição na tela
print(transcript)


