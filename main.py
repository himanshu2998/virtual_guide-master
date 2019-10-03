import os
import get_place as gp
import update_train as ut
#import video
import recom
def get_name(path):
    name=gp.place_in(path)
    return name

def update():
    return ut.update()


#def play(name):
#    video.play_vid(name)


def recommend(name):
    li=recom.recommend(name)
    return li
'''
name=get_name('test-3.jpg')
print(name[0])
print(recommend(name))
'''
#play(name)

