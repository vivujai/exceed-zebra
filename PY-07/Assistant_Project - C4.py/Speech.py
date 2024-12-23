import google.cloud.texttospeech as texttospeech
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import wavio as wv
import io
import os
import random
from google.cloud import speech_v1p1beta1 as speech


jpath = './vision-project-207707-f84d39ceed76.json'

class Conversation:
    def stt():
        client = speech.SpeechClient.from_service_account_json(jpath)

        sampleRate = 44100 #resolution in hertz
        language_code = 'en-US'#pronounciation
        duration = 10 #seconds
        frames = int(sampleRate*duration)

        print("recording")
        myRecording = sd.rec(frames, samplerate = sampleRate, channels = 1)
        sd.wait()
        print("end")

        wv.write("output.wav", myRecording, sampleRate, sampwidth =2)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = sampleRate,
            language_code = language_code
            )

        audio_file = "output.wav"

        with io.open(audio_file, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
            response = client.recognize(config=config, audio=audio)

        for result in response.results:
            return (result.alternatives[0].transcript, result.alternatives[0].confidence)

    def tts(input):
        client = texttospeech.TextToSpeechClient.from_service_account_json(jpath)
        ourText = str(input)
        synthesis_input = texttospeech.SynthesisInput(text=ourText)
        languageCode = 'en-US'
        gender = texttospeech.SsmlVoiceGender.MALE
        voice = texttospeech.VoiceSelectionParams(language_code=languageCode, ssml_gender=gender)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = client.synthesize_speech(input=synthesis_input, voice = voice, audio_config=audio_config)
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)
            print(input)
            print("audio content written to output file")

        os.startfile("output.mp3")
