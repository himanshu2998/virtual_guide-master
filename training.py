import numpy as np
import text_code as text
#import os
#from PIL import Image
#import cv2

top=5

#test=Image.open("test-1.jpg")
#test=compress.compress(test)
#test=np.asarray(test)
#testm=np.mean(test)
#testv=np.var(test)

def mean_img(im):
    return np.mean(im)

def var_img(im):
    return np.var(im)

def sort(list1,list2):
    lim=0
    for i in range(len(list2)-1):
        for j in range(len(list2)-i-1):
            if(list2[j,0]<list2[j+1,0]):
                temp2=list2[j,0]
                list2[j,0]=list2[j+1,0]
                list2[j+1,0]=temp2

                temp1=list1[j,0]
                list1[j,0]=list1[j+1,0]
                list1[j+1,0]=temp1
        lim+=1
        if(lim==top):
            break
    l1=list1[-top:,:]
    return l1[::-1]

def positive(listr):
    for i in range(len(listr)):
        if(listr[i]<0):
            listr[i]=-listr[i]
    return listr

def get_lable(name):
    lisn=text.img_name
    lisl=text.lables
    for i in range(len(lisn)):
        if(name==lisn[i]):
            return lisl[i]

def training_algo(m,v):
    features=np.copy(text.features)
    img_name=np.copy(text.img_name)
    means=[]
    variance=[]
    means=features[:,:1]-m
    means=positive(means)
    variance=features[:,1:2]-v
    variance=positive(variance)
    #print(means)
    #print(variance)
    n1=np.copy(img_name)
    n2=np.copy(img_name)
    n1=sort(n1,means)
    n2=sort(n2,variance)
    #print(n1)
    #print(n2)
    #print(means)
    #print(variance)
    n3=np.intersect1d(n1,n2)
    #print(n3)
    return n3
#training_algo(testm,testv)   





















