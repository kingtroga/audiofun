# import the necessary library
import speech_recognition as sr 

# instantiate the necessary library that is Recognizer
recognizer = sr.Recognizer()

# convert the audio in an AudioFile object
clean_support_call = sr.AudioFile("clean-support-call.wav")

# convert the AudioFile object into an AudioData object
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
# we are using Google's Web Api cuz it's free
text = recognizer.recognize_google(clean_support_call_audio, language="en-US")
print(text)
