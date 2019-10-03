import numpy as np
def match(im1,im2):
    m1=im1.mean()
    v1=im1.var()
    m2=im2.mean()
    v2=im2.var()
    cov=(im1-m1)*(im2-m2)
    c1=0.01*0.01
    c2=0.03*0.03
    ssim=(((2*m1*m2)+c1)*(2*cov.sum()+c2))/(((m1*m1)+(m2*m2)+c1)*(v1+v2+c2))
    return ssim
def similar(ssim):
    if(ssim>0.5):
        return True
    else:
        return False
