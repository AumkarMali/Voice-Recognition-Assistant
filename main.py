# for speech-to-text
import speech_recognition as sr
# for text-to-speech
import simpleaudio as sa

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import transformers
import ctypes
import webbrowser
import os
import requests
import time
from threading import Thread
import wolframalpha

from secondary import play_music
# for data
import os


import numpy as np
# Building the AI


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone(1) as mic:
        print("Now listening to audio input.....")
        audio = recognizer.listen(mic)
        text="ERROR"
    try:
        text = recognizer.recognize_google(audio).lower()
        print("Me  --> ", text)
    except:
        print("Me  -->  ERROR")

    return text

def text_to_speech(text):

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

            os.remove('speech.wav')

        except KeyboardInterrupt:
            pass
        


def RUN_CORTANA():

    RunLoop = True
    print("RUNNING MAIN FUNCTION")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while RunLoop:
        text = speech_to_text()

        if "weather" in text:
            city = "mississauga"

            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=55e2a19f818d978dbf28576c98ae2dc2&units=metric'.format(city)
            res = requests.get(url)
            data = res.json()

            temp = data['main']['temp']
            wind = data['wind']['speed']
            lat = data['coord']['lat']
            long = data['coord']['lon']
            desc = data['weather'][0]['description']
            res = f"The temperature is {temp}°C with {desc}."

        elif "calc" in text:
            question = text
            app_id = "PH8RJ2-J579TR7PVT"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            res = f"The answer is {answer}"

        elif "play" in text:
            song = text.replace("play", "")
            play_music(song)
            res = ''

        elif 'search' in text:
            speak = False
            text = text.replace("search", "")
            url = 'https://google.com/search?q=' + text
            webbrowser.open(url)
            res = ''

        elif 'close window' in text:
            speak = False
            res = ""
            ctypes.windll.user32.LockWorkStation()

        else:
            if any(i in text for i in
                   ["exit", "close", "bye", "cya", "have a nice day", "see you", "talk to you later"]):
                res = np.random.choice(["Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
                RunLoop = False

            elif text=="ERROR":
                res=""
                pass
            else:
                chat = nlp(transformers.Conversation(text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()


        text_to_speech(res)
    print("----- Closing down Cortana -----")


if True:
    print("----- Starting up -----")
    RUN_CORTANA()









