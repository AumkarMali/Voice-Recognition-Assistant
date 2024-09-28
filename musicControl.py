import keyboard
import os
import simpleaudio as sa
from playsound import playsound
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import speech_recognition as sr
import os.path
import urllib.request
import re
import youtube_dl
import winsound
import random
import webbrowser
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

os.system("")

authenticator = IAMAuthenticator('JCoD4sHVpURg-mRU2Z2M7AdpNhnc5rYJFSBeaK7qUk5H')
text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9eea1d81-0642-4cd7-8560-2782ee6d4ff1')

def tts(output):
    text = output

    if text != "":
        text = (text.replace("cortana", "")).lower()
        authenticator = IAMAuthenticator('JCoD4sHVpURg-mRU2Z2M7AdpNhnc5rYJFSBeaK7qUk5H')
        text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )
        text_to_speech.set_service_url(
            'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9eea1d81-0642-4cd7-8560-2782ee6d4ff1')

        print("CORTANA --> ", text)

        with open('speech.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(text, voice='en-GB_CharlotteV3Voice',
                                          accept='audio/wav').get_result().content)
        try:
            wave_object = sa.WaveObject.from_wave_file('speech.wav')

            play_object = wave_object.play()
            play_object.wait_done()

        except KeyboardInterrupt:
            pass



def remove(text, onlyfiles):
    text = text.replace('remove', '')
    music_name = text
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    exam = concatMusic1["content"]
    exam = exam.replace(".", "")
    exam = exam.replace("'", "")
    exam = exam + ".mp3"

    exam_path = r"C:\Users\docto\PycharmProjects\Cortana 3\MusicPlaylist" + "\\" + exam

    check = False

    for i in onlyfiles:
        i = i.replace(".mp3", "")

        if text in i.lower():
            check = True

    song = concatMusic1

    if check:
        os.remove(exam_path)
        delete = concatMusic1["content"] + " has been deleted from playlist..."
        tts(delete)

    elif not check:
        tts("Track not found...")

def open_app(text):
    if "roblox" in text:
        webbrowser.open("https://web.roblox.com/home")

    if "minecraft" in text:
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Studios\\Minecraft Education Edition\\Minecraft.Windows.exe')

    if "chrome" in text:
        subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    if "pycharm" in text:
        subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm 2020.3.2\\bin\pycharm64.exe')

    if "spotify" in text:
        subprocess.Popen('C:\\Users\\docto\\AppData\\Roaming\\Spotify\\Spotify.exe')

    if "Notepad" in text:
        subprocess.Popen(["Notepad"])

def play_music(text):
    print("[Loading Track....]")
    text = text.replace('cortana', '')
    text = text.replace("play", "")

    music_name = text
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    exam_raw = concatMusic1["content"]

    exam = exam_raw[0:19]
    exam = exam.replace(".", "")
    exam = exam.replace("/", "")
    exam = exam.replace(":", " -")
    exam = exam.replace("|", "_")
    exam = exam.replace("'", "")

    exam_path = r"C:\Users\docto\PycharmProjects\Cortana 3\MusicPlaylist" + "\\" + exam + ".wav"
    check = os.path.exists(exam_path)
    song = concatMusic1

    if check:
        print('Now playing:', concatMusic1['content'], clip2)

        MusicWave = sa.WaveObject.from_wave_file(exam_path)
        play_object = MusicWave.play()
        play_object.wait_done()

    elif not check:
        tts("[Downloading track...]")

        location = r'C:\Users\docto\PycharmProjects\Cortana 3\MusicPlaylist/%(title)s.%(ext)s'

        ydl_opts = {
            'outtmpl': location,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([clip2])

        exam2 = concatMusic1["content"]
        exam2 = exam2.replace(".", "")
        exam2 = exam2.replace("/", "")
        exam2 = exam2.replace(":", " -")
        exam2 = exam2.replace("|", "_")
        exam2 = exam2.replace("'", "")

        old_name = r"C:\Users\docto\PycharmProjects\Cortana 3\MusicPlaylist" + "\\" + exam2 + ".wav"

        print(old_name)
        new_name = r"C:\Users\docto\PycharmProjects\Cortana 3\MusicPlaylist" + "\\" + exam + ".wav"
        os.rename(old_name, new_name)

        print("Renaming to:", new_name)
        print("Now playing:", concatMusic1['content'], "(" + clip2 + ")")

        MusicWave = sa.WaveObject.from_wave_file(new_name)
        play_object = MusicWave.play()

        play_object.wait_done()


def play_playlist():
    path = 'C:\\Users\\docto\\PycharmProjects\\Cortana 2.6\\Playlist\\'
    num = 0
    file = path + os.listdir(path)[num]
    p = vlc.MediaPlayer(file)
    p.play()
    name = os.listdir(path)[num].replace(".mp3", "")
    print("Now playing:", name)

    while True:
        text = input("Would you like to skip?")
        p.stop()

        if "stop" in text:
            break

        num = num + 1
        file = path + os.listdir(path)[num]
        p = vlc.MediaPlayer(file)
        p.play()
        name = os.listdir(path)[num].replace(".mp3", "")
        print("Now playing:", name)


def play_random():
    music_dir = "C:\\Users\\docto\\PycharmProjects\\Cortana 2.6\\Playlist"
    files = os.listdir(music_dir)
    music = random.choice(files)
    music_name = music.replace(".mp3", "")
    print("Now playing " + music_name)
    p = vlc.MediaPlayer(os.path.join(music_dir, music))
    p.play()

