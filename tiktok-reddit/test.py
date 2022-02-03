from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from PIL import Image
import math

screensize = (460,720)
black = (0,0,0)
a1 = AudioFileClip("title.mp3")

#cc = ColorClip(screensize, black, duration=25).write_videofile("test.mp4", fps=25)
img = Image.open('title.png')
img_size = img.size
img = img.resize((800, math.floor(img_size[1]*800 / img_size[0])))
print(img.size)
print(img_size)
img.save('title.png')
logo = (ImageClip("title.png", duration=a1.duration))
cc = ColorClip(screensize, black, duration=a1.duration)
cvc = CompositeVideoClip([cc,logo.set_position("center")])
cvc = cvc.set_audio(a1)
cvc.write_videofile("test.mp4", fps=25)