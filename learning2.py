# import necessary library.
import speech_recognition as sr

# intialize the Recognizer object
recognizer = sr.Recognizer()

# convert the audio into an AudioFile object
thirty_seconds_of_nothing = sr.AudioFile("30-seconds-of-nothing-16k.wav")

# convert the AudioFile into and AudioData object
with thirty_seconds_of_nothing as source:
    thirty_seconds_of_nothing_audio = recognizer.record(source, duration=5)

# Transcribe the audio to text
text = recognizer.recognize_google(thirty_seconds_of_nothing_audio)
print(text)
