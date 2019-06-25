
import numpy as np
from PIL import Image
import cv2
import requests


class CodePass(object):

    def __init__(self):
        # self.url = "http://necaptcha.nosdn.127.net/782e5e3dc8754a32b6fe405d009ba12a.jpg"
        self.url = "http://necaptcha.nosdn.127.net/6346d2badb514049a16aa3c086b9b6f0.jpg"

    def get_img(self):
        ret = requests.get(self.url)
        with open("./code.jpg", "wb") as f:
            f.write(ret.content)

    def er_zhi_im(self):
        im1 = Image.open('./code.jpg')
        im1 = im1.convert('L')
        im1 = im1.point(lambda x: 255 if x > 170 else 0)
        im1.save('./code_h.png')

    def img_get_line(self):
        im1 = cv2.imread('code_h.png')
        im2 = np.mean(im1, axis=2).T
        for i in range(im2.shape[0]):
            if i ==0:
                continue
            b = im2[i]
            index = self.make_line(b, 30, 255)
            if index:
                # print(i, index)
                pre_im = im2[i-1][index-30:index]
                # print(pre_im)
                a = self.make_line(pre_im, 29, 0)
                if a:
                    return i

    def make_line(self, b, n, v):
        count = 0
        for i in range(len(b)):
            if b[i] != v:
                continue
            if i == len(b)-1:
                break
            if count >= n-1:
                return i
            if b[i] == b[i+1]:
                count += 1
            elif b[i] != b[i+1]:
                count = 0

    def run(self):
        self.get_img()
        self.er_zhi_im()
        return self.img_get_line()


if __name__ == '__main__':
    code_pass = CodePass()
    a = code_pass.run()
    print(a)
