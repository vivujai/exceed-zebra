import google.cloud.texttospeech as texttospeech
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import wavio as wv
import io
import os
import random
from google.cloud import speech_v1p1beta1 as speech
import openmeteo_requests as weatherAPI
import requests_cache
import pandas as pd
from retry_requests import retry
import math
import datetime as dt
from Speech import Conversation as C
from timefuncs import Time as T
from Calc import Calculator
import Weather as W
from Transcriber import Transcribe as TC



# bday_dist()
# conversation.tts(weather(time.c_hour()))
# c_time()


while True:
    try:
        message,confidence = C.stt()
    except TypeError:
        C.tts("try again")
    try:
        if message == "":
            C.tts("try again")
    except NameError:
        continue
    if "stop" in message:
        quit()
    print("message",message)
    print("Confidence",confidence)


    msg_list = message.split(" ")

    print(msg_list)

    num_list = []
    for word in msg_list:
        if word.isnumeric():
            num_list.append(word)
    
    if len(num_list) > 1:
        if ("plus" in msg_list or "+" in msg_list or "sum" in msg_list) and ("minus" not in msg_list and "subtracted" not in msg_list and "-" not in msg_list) and ("*" not in msg_list and "times" not in msg_list) and ("divide" not in msg_list and "divided" not in msg_list and "/" not in msg_list):
            
            answer = Calculator.add(num_list)
            response = f"The answer is {answer}"
            C.tts(response)


        elif ("minus" in msg_list or "subtracted" in msg_list or "-" in msg_list) and ("plus" not in msg_list and "+" not in msg_list  and "sum" not in msg_list) and ("*" not in msg_list and "times" not in msg_list) and ("divide" not in msg_list and "divided" not in msg_list):
                
            answer = Calculator.subtract(num_list)
            response = f"The answer is {answer}"
            C.tts(response)
            
        elif ("*" in msg_list or "times" in msg_list) and ("minus" not in msg_list and "subtracted" not in msg_list and "-" not in msg_list) and ("plus" not in msg_list and "+" not in msg_list  and "sum" not in msg_list) and ("divide" not in msg_list and "divided" not in msg_list):
             
            answer = Calculator.multi(num_list)
            response = f"The answer is {answer}"
            C.tts(response)

        elif ("divide" in msg_list or "divided" in msg_list or "/" in msg_list) and ("minus" not in msg_list and "subtracted" not in msg_list and "-" not in msg_list) and ("plus" not in msg_list and "+" not in msg_list  and "sum" not in msg_list) and ("*" not in msg_list and "times" not in msg_list):
                
            answer = Calculator.divide(num_list)
            response = f"The answer is {answer}"
            C.tts(response)

    if ("weather" in msg_list or "temperature" in msg_list)and ("today" in msg_list or ("right" in msg_list and "now" in msg_list) or "now" in msg_list or "currently" in msg_list):
        temp, pprob = W.weather(T.c_hour())
        C.tts(f"The temperature is {round(temp)}°C, with a {pprob}% chance of precipitation")

    if ("what's" in msg_list or "what" in msg_list) and "time" in msg_list:
        C.tts(f"The time is {T.c_time()}")

    if "time" in msg_list and "birthday" in msg_list:
        C.tts(f"There are {T.bday_dist()} days till your birthday")

    if ("record" in msg_list or "transcribe" in msg_list):
        duration = None
        for word in msg_list:
            if word.isnumeric():
                duration = word

        if duration == None:
            C.tts("Please specify the duration in seconds")

        message,confidence = C.stt()

        msg_list = message.split(" ")

        print(msg_list)

        while True:
            if message == "":
                C.tts("try again")
                message, confidence = C.stt()
            elif "stop" in msg_list:
                 quit()
            else:
                break

        for word in msg_list:
            if word.isnumeric():
                duration = int(word)

        C.tts("Specify the name, only say the entire name")


        message,confidence = C.stt()
 
        msg_list = message.split(" ")

        print(msg_list)


        while True:
            if message == "":
                C.tts("try again")
                message, confidence = C.stt()
                print(message)
            elif "stop" in msg_list:
                 quit()
            else:
                break


        name = message
        
        print(duration, name)

        TC.transcribe(duration, name)
