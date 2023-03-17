from moviepy.video.io.VideoFileClip import VideoFileClip

# Define o caminho do arquivo de vídeo
video_path = "./testingvideo.mp4"

# Cria um objeto VideoFileClip a partir do arquivo de vídeo
video = VideoFileClip(video_path)

# Extrai o áudio do arquivo de vídeo
audio = video.audio

# Define o caminho do arquivo de áudio de saída
audio_path = "./audio.mp3"

# Salva o áudio como um arquivo separado
audio.write_audiofile(audio_path,codec="libmp3lame", bitrate="128k")


