import easyocr
import numpy as np

class Reader:
    def __init__(self, reader=easyocr.Reader(['ru'])):
        self.reader = reader

    def read_from_img(self, image):
        pre_res = self.reader.readtext(image, detail=0)
        result = ''
        for i in pre_res:
            result += ' ' + i.lower() 
        return result[1:]

