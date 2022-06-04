# load the necessary libraries
import speech_recognition as sr

# instantiate the Recognizer object
recognizer = sr.Recognizer()

# Loud the audio as an AudioFile object
three_seconds_of_static_at_the_front = sr.AudioFile("static-out-of-warranty.wav")

# convert the AudioFile object in an AudioData object
with three_seconds_of_static_at_the_front as source:
    three_seconds_of_static_at_the_front_audio = recognizer.record(
        source,
        offset=3
    )

# transcribe the AudioData into text
text = recognizer.recognize_google(three_seconds_of_static_at_the_front_audio)
print(text)