# extracting the audio
import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"testcase2.mov")
my_clip.audio.write_audiofile(r"my_result.mp3")


# converting mp3 into wav
from os import path
from pydub import AudioSegment

# files                                                                         
src = "my_result.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


# speech to text
import speech_recognition as sr
filename = "test.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)


# language conversion
import googletrans
# making the object
transalator = googletrans.Translator()
# translating the languages
translated = transalator.translate('I love india', dest = 'hi')
print(translated)