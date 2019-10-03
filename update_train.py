import os
import compress_image as compress
from PIL import Image
import cv2
import numpy as np

def update():
    iar_mean=[]
    iar_var=[]
    iar_dist=[]
    iar_lable=[]
    iar_name=[]
    lab=[]
    cwd=os.getcwd()
    path=os.path.join(cwd,'IMAGES')
    list_monuments=os.listdir(path)
    for direc in list_monuments:
        pathr=os.path.join(path,direc)
        for folder in os.listdir(pathr):
            lab.append(folder)
            pathf=os.path.join(pathr,folder)
            num=np.random.randint(1,11)
            for img in os.listdir(pathf):
                if(img.endswith('.jpg')):
                    iar_name.append(img)
                    path_img=os.path.join(pathf,img)
                    img=Image.open(path_img)
                    img=compress.compress(img)
                    iar_mean.append(np.mean(img))
                    iar_var.append(np.var(img))
                    iar_dist.append(num)
                    iar_lable.append(folder)
    fp=open("trainer.txt","w")
    for i in range(len(iar_name)):
        fp.write(iar_name[i]+","+str(iar_mean[i])+","+str(iar_var[i])+","+str(iar_dist[i])+","+iar_lable[i]+"\n")
    fp.close
    return True

