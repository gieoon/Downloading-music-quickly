from pytube import YouTube
import os
import subprocess
import signal
import sys

print(sys.argv[1:])
url = sys.argv[1]

if url != None and len(url.strip()) > 0:
    
    output_path = './temp/'

    yt=YouTube(url)
    t=yt.streams.filter(only_audio=True).all()
    t[0].download(output_path)
    print("filename: ", t[0].default_filename)
    filename = t[0].default_filename
    process = subprocess.Popen([
        "ffmpeg",
        "-i", 
        os.path.join(output_path, filename),
        os.path.join('./', f'{filename}.mp3')
    ])#, stdout=subprocess.PIPE, shell=True)

    # os.killpg(os.getpgid(process.pid), signal.SIGTERM) 
    # process.kill()

    print("DOWNLOAD COMPLETE")