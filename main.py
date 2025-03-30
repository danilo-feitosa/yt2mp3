import streamlit as st
import yt_dlp
import os
import re
import tempfile


def baixar_mp3(url, progress_callback):
    st.write("Espera, o arquivo está em processo de preparação.")

    temp_dir = tempfile.gettempdir()

    def hook(d):
        if d['status'] == 'downloading':
            percent_match = re.search(r"(\d+\.\d+)%", d['_percent_str'])
            if percent_match:
                percent = float(percent_match.group(1))
                progress_callback(percent)
        elif d['status'] == 'finished':
            progress_callback(100)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'ffmpeg/bin/ffmpeg.exe',
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        'progress_hooks': [hook]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            arquivo_mp3 = os.path.join(temp_dir, f"{info['title']}.mp3")
        return arquivo_mp3
    except yt_dlp.utils.DownloadError as e:
        st.error(f"Erro ao baixar o vídeo: {e}")
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
    return None


st.title("🎵 MP3 Downloader com Progresso")

url_direta = st.text_input("📌 Insira um link do YouTube:")
progress = st.progress(0)


def atualizar_progresso(valor):
    progress.progress(int(valor))


if url_direta:
    if st.button("Baixar pelo Link"):
        arquivo_mp3 = baixar_mp3(url_direta, atualizar_progresso)
        if arquivo_mp3:
            st.success("Finalizado!  Clique no botão abaixo para fazer o download do arquivo.")
            with open(arquivo_mp3, "rb") as file:
                st.download_button(label="📥 Baixar MP3", data=file, file_name=os.path.basename(arquivo_mp3),
                                   mime="audio/mpeg")
