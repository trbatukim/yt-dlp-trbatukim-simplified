#reqs
from __future__ import unicode_literals
import yt_dlp
import os
import sys
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

#Find the downloads folder
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads') # Includes solutions for macOS/Linux

#Find the real path of the .exe file
def get_real_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))
current_dir = get_real_path()

#Setting up ffmpeg path
ffmpeg_path = os.path.join(current_dir, 'ffmpeg', 'bin', 'ffmpeg.exe')
#Setting up downloads path
download_dir = get_download_path()
#Setting up cookies.txt path
cookies_dir = os.path.join(current_dir, 'cookies', 'cookies.txt')

video_file_types = ["mp4", "avi", "mkv", "mov", "webm", "m4v"]
audio_file_types = ["mp3", "wav", "flac","m4a"]

clear_console()
print(f"{colored('Written by: trbatukim', 'white', attrs=['bold'])}\n{colored('Uses', 'white', attrs=['bold'])} {colored(link('https://github.com/yt-dlp/yt-dlp', 'yt-dlp'), 'red', attrs=['bold'])} {colored('at its base.', 'white', attrs=['bold'])}\n\n[0] Video and audio\n[1] Only audio\n[2] Supported websites\n\nDownloaded videos will be saved to: {download_dir}")

while True:
    if keyboard.is_pressed("0"):
        clear_console()
        print(f"{colored('Select a file type:', 'white', attrs=['bold'])}\n\n[0] MP4\n[1] AVI (LOW QUALITY)\n[2] MKV\n[3] MOV\n[4] WEBM\n[5] M4V")
        time.sleep(0.3)
        while True:
            current_key = keyboard.read_key()
            if current_key.isdigit() and 8 >= int(current_key) >= 0:
                file_type = video_file_types[int(current_key)]
                ydl_opts = {
                    'cookiefile': cookies_dir,
                    'format': 'bestvideo+bestaudio/best',
                    'ffmpeg_location': ffmpeg_path,
                    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': f'{file_type}'
                    }]}
                break
        break
    elif keyboard.is_pressed("1"):
        clear_console()
        print(f"{colored('Select a file type:', 'white', attrs=['bold'])}\n\n[0] MP3\n[1] WAV\n[2] FLAC\n[3] M4A")
        time.sleep(0.3)
        while True:
            current_key = keyboard.read_key()
            if current_key.isdigit() and 9 >= int(current_key) >= 0:
                file_type = audio_file_types[int(current_key)]
                ydl_opts = {
                    'cookiefile': cookies_dir,
                    'format': 'bestaudio/best',
                    'ffmpeg_location': ffmpeg_path,
                    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
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
print(f"{colored(f'Converting to {file_type.upper()}...', 'white', attrs=['bold'])}")
flush_input()
url = input(colored('\nPaste the link here: ', 'light_blue'))

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

exit()
