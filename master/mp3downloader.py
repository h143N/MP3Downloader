import yt_dlp
import os

print("\nMP3 Downloader v1.1.0 by hideNFN\n")

currentfolder = os.getcwd()
datafolder = currentfolder + "\\.data"
ffmpegfolder = datafolder + "\\.ffmpeg"
ffmpegcheck = ffmpegfolder + "\\ffmpeg.exe"
ffprobecheck = ffmpegfolder + "\\ffprobe.exe"


if os.path.exists(datafolder) is False or os.path.exists(ffmpegfolder) is False:
    print("\nCreating necessary folders...")
    if os.path.exists(datafolder) is False:
        os.mkdir(datafolder)
    if os.path.exists(ffmpegfolder) is False:
        os.mkdir(ffmpegfolder)

if os.path.exists(ffmpegcheck) is True and os.path.exists(ffprobecheck) is True:
    print("\nThe FFmpeg install has been found.\n")
else:
    print('\nThe FFmpeg install hasn\'t been found, please download FFmpeg and place ffmpeg.exe and ffprobe.exe inside the "\\.data\\.ffmpeg" path.\n')

os.chdir(datafolder)

def mp3dwn():
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