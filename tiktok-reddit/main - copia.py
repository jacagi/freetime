from selenium import webdriver
import numpy as np
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from PIL import Image
import re, praw, os, gtts,math

target_url = 'https://www.reddit.com/r/AskReddit/comments/sh32t0/what_is_a_clear_sign_of_you_getting_older/'
post_id = re.findall(r"\/comments\/(.*)\/.*\/", target_url)[0]
cookies_button_class = '_1tI68pPnLBjR1iHcL7vsee'
useragent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
max_comments = 10
screensize = (828,1792)
black = (0,0,0)

reddit = praw.Reddit(
    client_id="L6mNZ452VKIiDK-pdOU_Tw",
    client_secret="VfDMlPU0bhvOYRipLPP3UfqIvqKCFQ",
    user_agent="windows:com.testapp.testapp:v1.0.0 (by /u/Winter-Platypus-926)",
)
submission = reddit.submission(id=post_id)

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent)
options = webdriver.FirefoxOptions()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

def init_webdriver():
    fox = webdriver.Firefox(firefox_profile=profile,options=options)
    fox.get(target_url)
    fox.maximize_window()
    fox.implicitly_wait(5)
    buttons = fox.find_elements_by_class_name(cookies_button_class)
    buttons[0].click()
    return fox

def screenshot_title(fox):
    fox.find_element_by_id('t3_' + post_id).screenshot("./" + post_id + "/title.png")
    tts = gtts.gTTS(submission.title)
    tts.save("./" + post_id + "/title.mp3")
    print('Title Screenshoted')

def screenshot_comments(fox):
    top_level_comments = list(submission.comments)
    top_level_comments.pop(-1)
    top_level_comments = top_level_comments[:max_comments]
    for t in top_level_comments:
        comment_id = t.id
        fox.find_element_by_id("t1_" + comment_id).screenshot("./" + post_id + "/"+comment_id+".png")
        tts = gtts.gTTS(t.body)
        tts.save("./" + post_id + "/"+comment_id+".mp3")
    print('Comment Screenshoted')
    return top_level_comments

def create_video(id):
    files_path= './'+ post_id +'/'+ id 
    img = Image.open(files_path+'.png')
    aud = AudioFileClip(files_path +'.mp3')
    img_size = img.size
    img = img.resize((800, math.floor(img_size[1]*800 / img_size[0])))
    img.save(files_path+'.png')
    logo = (ImageClip(files_path+'.png', duration=aud.duration))
    cc = ColorClip(screensize, black, duration=aud.duration)
    cvc = CompositeVideoClip([cc,logo.set_position("center")])
    cvc = cvc.set_audio(aud)
    cvc.write_videofile(files_path+'.mp4', fps=25)
    return cvc

def create_videos(comments):
    ids_to_proccess = [c.id for c in comments]
    ids_to_proccess = ["title"] + ids_to_proccess
    videos = []
    for i in ids_to_proccess:
        videos.append(create_video(i))
    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile('./'+ post_id +'/result.mp4', fps=25)
    
if __name__ == '__main__':
    print('Starting...')
    os.mkdir("./" + post_id)
    fox = init_webdriver()
    screenshot_title(fox)
    comments = screenshot_comments(fox)
    fox.close()
    create_videos(comments)
    print('Finish')  