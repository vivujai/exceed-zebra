import google.cloud.texttospeech as texttospeech
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import wavio as wv
import io
import os
import random
from google.cloud import speech_v1p1beta1 as speech
# from pydub import AudioSegment



jpath = './vision-project-207707-f84d39ceed76.json'

class Transcribe:
    def transcribe(duration, name):
        print(duration)
        print(name)
        client = speech.SpeechClient.from_service_account_json(jpath)

        sampleRate = 44100 #resolution in hertz
        language_code = 'en-US'#pronounciation
        duration = int(duration) #seconds
        frames = int(sampleRate*duration)

        print("recording")
        myRecording = sd.rec(frames, samplerate = sampleRate, channels = 1)
        sd.wait()
        print("end")

        wv.write(f"{name}.wav", myRecording, sampleRate, sampwidth =2)

        data, samplerate = sf.read(f"{name}.wav")
        sf.write(f"{name}.mp3", data, samplerate)

        os.remove(f"{name}.wav")

#       os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

        os.replace(f"./{name}.mp3",f"./Transcribes/{name}.mp3")

        os.startfile(f"{name}.mp3")

        return f"saving file as mp3, playing file"
