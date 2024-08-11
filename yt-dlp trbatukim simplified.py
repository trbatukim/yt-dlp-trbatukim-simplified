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

video_file_types = ["mp4", "avi", "mkv", "mov", "webm", "m4v"]
audio_file_types = ["mp3", "wav", "flac","m4a"]

clear_console()
print(f"{colored('Yazar: trbatukim', 'white', attrs=['bold'])}\n{colored('Gereksinimler:', 'white', attrs=['bold'])} {colored(link('https://www.ffmpeg.org/', 'ffmpeg'), 'red', attrs=['bold'])}\n{colored('Temelinde', 'white', attrs=['bold'])} {colored(link('https://github.com/yt-dlp/yt-dlp', 'yt-dlp'), 'red', attrs=['bold'])} {colored('kullanır.', 'white', attrs=['bold'])}\n\n[0] Video ve ses\n[1] Salt ses\n[2] Desteklenen siteler")

while True:
    if keyboard.is_pressed("0"):
        clear_console()
        print(f"{colored('Dosya türü seçiniz:', 'white', attrs=['bold'])}\n\n[0] MP4\n[1] AVI (DÜŞÜK KALİTE)\n[2] MKV\n[3] MOV\n[4] WEBM\n[5] M4V")
        time.sleep(0.3)
        while True:
            current_key = keyboard.read_key()
            if current_key.isdigit() and 8 >= int(current_key) >= 0:
                file_type = video_file_types[int(current_key)]
                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': f'{file_type}'
                    }]}
                break
        break
    elif keyboard.is_pressed("1"):
        clear_console()
        print(f"{colored('Dosya türü seçiniz:', 'white', attrs=['bold'])}\n\n[0] MP3\n[1] WAV\n[2] FLAC\n[3] M4A")
        time.sleep(0.3)
        while True:
            current_key = keyboard.read_key()
            if current_key.isdigit() and 9 >= int(current_key) >= 0:
                file_type = audio_file_types[int(current_key)]
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': f'{(file_type)}',
                        'preferredquality': '192',
                    }]}
                break
        break
    elif keyboard.is_pressed("2"):
        webbrowser.open("https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md")
        time.sleep(0.3)

clear_console()
print(f"{colored(f'{file_type.upper()} dosya türüne dönüştürülüyor...', 'white', attrs=['bold'])}")
flush_input()
url = input(colored('\nLinki giriniz: ', 'light_blue'))

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

exit()
