#!/usr/bin/env python3
import os
import sys
import yt_dlp

def download_video(url, output_path="."):
    """
    Télécharge une vidéo YouTube à partir de l'URL donnée.
    :param url: URL de la vidéo YouTube
    :param output_path: Dossier de destination (par défaut : dossier courant)
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"\nTéléchargement terminé : {info_dict['title']}")
            print(f"Fichier enregistré dans : {output_path}")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 download_youtube_video.py <URL> [DOSSIER_DE_DESTINATION]")
        sys.exit(1)

    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "."

    download_video(url, output_path)
