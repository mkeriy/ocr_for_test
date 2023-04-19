import easyocr
import json, io
from PIL import Image
import numpy as np
import json


def det_and_rec(img):

#     reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')

    reader = easyocr.Reader(['ru','en']) 
     # need to run only once to download and load model into memory
    img_array = np.array(Image.open(io.BytesIO(img)).convert('RGB')) 
   
    res= reader.readtext(img_array)

    result = {}
    for idx in range(len(res)):
        line = res[idx]
        result[line[1]] = line[0]

    return result

# # draw result
# def draw_detected(img: bytes, res):
#     res=res[0]
#     img_array = np.array(Image.open(io.BytesIO(img)).convert('RGB')) 
#     boxes = [line[0] for line in res]
#     im_show = draw_ocr(img_array, boxes)
#     im_show = Image.fromarray(im_show)
#     im_show.save('result.jpg')



if __name__=='__main__':
    # print(det_and_rec('./example/1.png'))
    
    reader = easyocr.Reader(['ru','en']) # this needs to run only once to load the model into memory
    result = reader.readtext('./examples/1.png')
    print(result)
    
    