import numpy as np

data=np.genfromtxt("trainer.txt",dtype="str",delimiter=",")
img_name=data[:,0:1]
features=data[:,1:-1]
features=features.astype("float")
lables=data[:,-1:]
#print(features)
#print(img_name)
#print(type(lables))
def check_img(name):
    if(name in img_name):
        return True
    else:
        return False




'''
d={}
count=0
for k in lables:
    if(k[0] not in d):
        d[k[0]]=count
        count+=1

print(d)
lable=[]
for k in lables:
    lable.append(d[k[0]])
print(lable)

print(d["Statue"])
'''
