from pydub import AudioSegment

# Import the .mp3 file

mp3_file = AudioSegment.from_file(r"C:\Users\TARI\Documents\GitHub\audiofun\Dumebi_slow_and_reverb.mp3", format="mp3")

# Export the .mp3 file as wav
# format is "mp3" by default
mp3_file.export(out_f="dumebi.wav", format="wav")