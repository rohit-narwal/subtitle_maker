# extracting the audio
import moviepy.editor as mp
# source and destination for audio file
source = r"test_case1.mov"
dest = r"test.wav"
def audio_extract(source, dest):
    my_clip = mp.VideoFileClip(source)
    my_clip.audio.write_audiofile(dest)

audio_extract(source, dest)

# storing the text
text = '' 

# speech to text
import speech_recognition as sr

filename = "test.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)

print(f"English Subtitles: {text}")
# language conversion

from googletrans import Translator

translator = Translator()

source_lan = "en"

translated_to= "hi"

translated_text = translator.translate(text, src=source_lan, dest = translated_to)

print(f"Hindi Subtitles: {translated_text.text}")

print(f"Pronunciation {translated_text.pronunciation}")
