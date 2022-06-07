'''Multiple speakers
No audio 
(speaker diarization)
Noisy audio'''
import speech_recognition as sr

recognizer = sr.Recognizer()

good_morning_japanese = sr.AudioFile("good-morning-japanense.wav")

with good_morning_japanese as source:
    japanese_audio = recognizer.record(source)

text = recognizer.recognize_google(japanese_audio, language="ja")


print(text)
