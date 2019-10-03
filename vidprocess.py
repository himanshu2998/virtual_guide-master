import os
import numpy as np
import text_code as txt

def process():

    list_text=[]
    list_vid=[]
    lab=[]
    dis=[]
    cwd=os.getcwd()
    path=os.path.join(cwd,'IMAGES')
    list_monuments=os.listdir(path)
    for direc in list_monuments:
        pathr=os.path.join(path,direc)
        for folder in os.listdir(pathr):
            lab.append(folder)
            pathf=os.path.join(pathr,folder)
            for file in os.listdir(pathf):
                if(file.endswith('.mp4')):
                    list_vid.append(os.path.join(pathf,file))
                elif(file.endswith('.txt')):
                    list_text.append(os.path.join(pathf,file))
    list_lab=txt.lables

    list_dist=txt.features[:,-1:]
    lables=[]
    dist=[]

    for i in range(len(list_lab)):
        if(list_lab[i] not in lables):
            lables.append(list_lab[i])
            dist.append(list_dist[i])
    dist=np.array(dist)
    lables=np.array(lables)
    for i in range(len(lab)):
        for j in range(len(lables)):
            if(lab[i]==lables[j,0]):
                dis.append(dist[j,0])
                continue


    for i in range(len(dis)):
        for j in range(i+1,len(dis)):
            if(dis[i]>dis[j]):
                temp1=dis[i]
                dis[i]=dis[j]
                dis[j]=temp1
                temp1=lab[i]
                lab[i]=lab[j]
                lab[j]=temp1
                temp1=list_vid[i]
                list_vid[i]=list_vid[j]
                list_vid[j]=temp1
                temp1=list_text[i]
                list_text[i]=list_text[j]
                list_text[j]=temp1
    #print(dis)
    #print(lab)
    #print(list_vid)
    #print(list_text)
    return(list_vid,lab,list_text)

