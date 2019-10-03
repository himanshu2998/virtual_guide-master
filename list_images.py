import os
import compress_image as compress
from PIL import Image
import cv2
import numpy as np

def img_asarray(path):
    i=Image.open(path)
    i=compress.compress(i)
    i=np.asarray(i)
    return i
def list_images(list):
    iar=[]
    iar_name=[]
    cwd=os.getcwd()
    path=os.path.join(cwd,'IMAGES')
    list_monuments=os.listdir(path)
    for direc in list_monuments:
        pathr=os.path.join(path,direc)
        for folder in os.listdir(pathr):
            pathf=os.path.join(pathr,folder)
            for img in os.listdir(pathf):
                if(img.endswith('.jpg')):
                    if(img in list):
                        iar_name.append(img)
                        path_img=os.path.join(pathf,img)
                        img=Image.open(path_img)
                        img=compress.compress(img)
                        iar.append(np.asarray(img))
    return iar,iar_name
    #print(len(iar))
    #print(iar_name)
'''
    print(iar[0].shape)
    iar[0]=Image.fromarray(iar[0])
    iar[0].show()
'''                



#l=['1.jpg','30.jpg']
#list_images(l)
