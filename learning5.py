from pydub import AudioSegment

import speech_recognition as sr

recognizer = sr.Recognizer()

#Import audio file
volume_adjusted = AudioSegment.from_file(file="volume_adjusted.wav", format="wav")

#Lower the volume by 60 dB
quiet_volume_adjusted = volume_adjusted - 60

with quiet_volume_adjusted as source:
    quiet_volume_adjusted_audio = recongizer.record(source)

recognizer.recognize_google(quiet_volume_adjusted_audio)
