import moviepy
import os
from moviepy.editor import *
import pygame
import vidprocess


def vid_play(name):
    list_vid,list_lable,list_text=vidprocess.process()
    text_file=[]
    for path in list_text:
        f=open(path,"r")
        f1=f.readlines()
        desc=''
        for x in f1:
            desc=desc+x
        f.close()
        text_file.append(desc)
            
    
    pygame.display.set_caption('title')
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    desc_clip=[]
    txt_clip=[]
    clip=[]
    j=0
    stop=0
    for i in range(len(list_lable)):
        if(name==list_lable[i]):
            stop=i
            break
            
    txt_clip.append((TextClip(list_lable[stop],fontsize=70,color='white',size=(1920,1080))).set_duration(3))
    clip.append(((VideoFileClip(list_vid[stop])).resize((1920,1080))).without_audio())
    desc_clip.append((TextClip(text_file[stop],fontsize=50,color='cyan',size=(1920,1080))).set_duration(3))
    final_clip = concatenate_videoclips([txt_clip[j],clip[j],desc_clip[j]])
    j=j+1
    init=stop+1
    for i in range(init,len(list_lable)):
        txt_clip.append((TextClip(list_lable[i],fontsize=70,color='white',size=(1920,1080))).set_duration(3))
        clip.append(((VideoFileClip(list_vid[i])).resize((1920,1080))).without_audio())
        desc_clip.append((TextClip(text_file[i],fontsize=50,color='cyan',size=(1920,1080))).set_duration(3))
        final_clip = concatenate_videoclips([final_clip,txt_clip[j],clip[j],desc_clip[j]])
        j=j+1
            
    final_clip.preview(fps=30)


'''
list_vid,list_lable,list_text=vidprocess.process()
text_file=[]
for path in list_text:
    f=open(path,"r")
    f1=f.readlines()
    desc=''
    for x in f1:
        desc=desc+x
    f.close()
    text_file.append(desc)
print(text_file)
'''

