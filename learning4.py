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