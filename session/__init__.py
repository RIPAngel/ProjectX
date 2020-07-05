import subprocess
import datetime
import os
import streamlink

def startRecord (id):
    m3u8 = streamlink.streams(f"https://www.twitch.tv/{id}")
    url = m3u8["best"].url
    cmd = [
        "ffmpeg",
        "-i", url,
        "-c", "copy",
        "-map_metadata", "0",
        f"{id}_{datetime.datetime.now()}.mkv"
    ]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print (f'[INFO] Starting Record Session for {id}, PID : {process.pid}')