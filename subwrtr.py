# # modules
# import cv2
# from os import path

# # import moviepy.editor
# #   video input
# video_cap = cv2.VideoCapture("test_case1.mp4")
# fps = video_cap.get(cv2.CAP_PROP_FPS)
# #   reading every frame
# while True:
#     success, frame = video_cap.read()
#     cv2.imshow("frame", frame)

#     if cv2.waitKey(1) & 0xFF== ord('q'):
#         break

# video_cap.release()
# cv2.destroyAllWindows()
# #   seprating audio from video
# # my_clip = moviepy.VideoFileClip(r"test_case1.mov")
# # my_clip.audio.write_audiofile(r"my_result.mp3")

# mp3 to wav
from pydub import AudioSegment                                                                     
# files    
src = "case1.mp3"
dst = "test.wav"

    # convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


# speech to text

# language conversion
import googletrans
# making the object
transalator = googletrans.Translator()
# translating the languages
translated = transalator.translate('I love india', dest = 'hi')
print(translated)
# inserting subtitles into video
