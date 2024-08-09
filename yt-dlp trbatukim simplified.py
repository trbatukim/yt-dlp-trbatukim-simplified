#reqs
from __future__ import unicode_literals
import yt_dlp
import os
import keyboard
import webbrowser
from termcolor import colored
import time

#Clean screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Flush the input stream
def flush_input():
    try:
        import msvcrt   #for Windows
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for Linux/unix/macOS
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

#Hyperlinks
def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''
    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
    return escape_mask.format(parameters, uri, label)

clear_console()
print(f"Yazar: trbatukim\nGereksinimler: {colored(link('https://www.ffmpeg.org/', 'ffmpeg'), 'red')}\nTemelinde {colored(link('https://github.com/yt-dlp/yt-dlp', 'yt-dlp'), 'red')} kullanır.\n\n[0] Video ve ses\n[1] Salt ses\n[2] Desteklenen websiteler")

while True:
    if keyboard.is_pressed("0"):
        clear_console()
        print(f"{colored('Dosya türü seçiniz:', 'white', attrs=['bold'])}\n\n[0] MP4\n[1] AVI\n[2] MKV\n[3] MOV\n[4] WMV\n[5] FLV\n[6] WEBM\n[7] MPEG\n[8] M4V")
        time.sleep(0.2)
        while True:
            current_key = keyboard.read_key()
            match current_key:
                case "0":
                    file_type = "MP4"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4'
                    }]}
                    break
                case "1":
                    file_type = "AVI"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'avi'
                    }]}
                    break
                case "2":
                    file_type = "MKV"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mkv'
                    }]}
                    break
                case "3":
                    file_type = "MOV"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mov'
                    }]}
                    break
                case "4":
                    file_type = "WMV"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'wmv'
                    }]}
                    break
                case "5":
                    file_type = "FLV"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'flv'
                    }]}
                    break
                case "6":
                    file_type = "WEBM"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'webm'
                    }]}
                    break
                case "7":
                    file_type = "MPEG"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mpeg'
                    }]}
                    break
                case "8":
                    file_type = "M4V"
                    ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'm4v'
                    }]}
                    break
        break
    elif keyboard.is_pressed("1"):
        clear_console()
        print(f"{colored('Dosya türü seçiniz:', 'white', attrs=['bold'])}\n\n[0] MP3\n[1] WAV\n[2] AAC\n[3] FLAC\n[4] ALAC\n[5] OGG\n[6] WMA\n[7] AIFF\n[8] M4A\n[9] PCM")
        time.sleep(0.2)
        while True:
            current_key = keyboard.read_key()
            match current_key:
                case "0":
                    file_type = "MP3"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]}
                    break
                case "1":
                    file_type = "WAV"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '192',
                    }]}
                    break
                case "2":
                    file_type = "AAC"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'aac',
                        'preferredquality': '192',
                    }]}
                    break
                case "3":
                    file_type = "FLAC"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'flac',
                        'preferredquality': '192',
                    }]}
                    break
                case "4":
                    file_type = "ALAC"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'alac',
                        'preferredquality': '192',
                    }]}
                    break
                case "5":
                    file_type = "OGG"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'ogg',
                        'preferredquality': '192',
                    }]}
                    break
                case "6":
                    file_type = "WMA"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wma',
                        'preferredquality': '192',
                    }]}
                    break
                case "7":
                    file_type = "AIFF"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'aiff',
                        'preferredquality': '192',
                    }]}
                    break
                case "8":
                    file_type = "M4A"
                    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'm4a',
                        'preferredquality': '192',
                    }]}
                    break
        break
    elif keyboard.is_pressed("2"):
        webbrowser.open("https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md")
        time.sleep(0.2)

clear_console()
print(f"{colored(f'{file_type} dosya türüne dönüştürülüyor...', 'white', attrs=['bold'])}")
flush_input()
url = input(colored('\nLinki giriniz: ', 'light_blue'))

#Downloading the video/audio in webm format and converting it to mp3/mp4
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

exit()