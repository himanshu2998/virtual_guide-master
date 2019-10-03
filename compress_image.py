import numpy as np
from PIL import Image
import cv2
import numpy as np
def compress(img):
    img=img.convert('L')
    #img=img.resize((1040,780))
    img=img.resize((520,390))
    return img







