from __future__ import unicode_literals
import yt_dlp
import os

def mp3dwn():
    print("MP3 Downloader v1.1.0 by hideNFN\n")

    currentfolder = os.getcwd()
    datafolder = currentfolder + "\\.data"
    folderffmpeg = datafolder + "\\.ffmpeg"
    ffmpegcheck = folderffmpeg + "\\ffmpeg.exe"
    ffprobecheck = folderffmpeg + "\\ffprobe.exe"

    if os.path.exists(datafolder) is False or os.path.exists(folderffmpeg) is False:
        print("\nCreating necessary folders...")
        if os.path.exists(datafolder) is False:
            os.mkdir(datafolder)
        if os.path.exists(folderffmpeg) is False:
            os.mkdir(folderffmpeg)

    if os.path.exists(ffmpegcheck) is True and os.path.exists(ffprobecheck) is True:
        print("\nThe FFmpeg install has been found.")
    else:
        print('\nThe FFmpeg install hasn\'t been found, please download FFmpeg and place ffmpeg.exe and ffprobe.exe inside the "\.data\.ffmpeg" path.')

    os.chdir(datafolder)
    
    while True:
        print("\nPaste the URL of the media you would like to download in a mp3 format:\n")

        linkmp3 = input()

        try:
            ydlp_opts = {
                "ffmpeg_location": ".ffmpeg",
                "outtmpl": "%(title)s.%(ext)s",
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
            with yt_dlp.YoutubeDL(ydlp_opts) as ydlp:
                ydlp.download([linkmp3])
        except:
            print("Processing error.")
mp3dwn()