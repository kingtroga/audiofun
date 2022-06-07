# Import PyDub main class
from pydub import AudioSegment

# Import an audio file
# Format parameter only for readability
wav_file = AudioSegment.from_file(file="good-morning-japanense.wav", format="wav")


# Playing an audio file
from pydub.playback import play
#play()

#Audio parameters
wav_file.channels



wav_file.frame_rate

#find the number of bytes per sample
wav_file.sample_width

# Find the max amplitude
wav_file.max

#Duration of audio file in mills
len(wav_file)

#changing audio parameters
# the higher the values excluding channels the better.

# Manipulating audio files with Pydub
# Increasing the volume. (That's basically what you need)

# Import AudioSegment and normalize
from pydub import AudioSegment
from pydub.effects import normalize


# Wow you can contencate two audio files together using the audio operation,
# Splitting your audio

# Import phone call audio 
phone_call = AudioSegment.from_file("phone












