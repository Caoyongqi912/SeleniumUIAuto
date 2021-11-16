# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 5:39 下午 
# @Author  : cyq
# @File    : Graphical.py


from io import BytesIO

import cv2
import numpy
from PIL import Image


class GraphicalLocator():

    def __init__(self, img_path):
        self.locator = img_path
        # x, y position in pixels counting from left, top corner
        self.x = None
        self.y = None
        self.img = cv2.imread(img_path)
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]
        self.threshold = None

    @property
    def center_x(self):
        return self.x + int(self.width / 2) if self.x and self.width else None

    @property
    def center_y(self): return self.y + int(self.height / 2) if self.y and self.height else None

    def find_me(self, drv):  # Clear last found coordinates
        self.x = self.y = None
        # Get current screenshot of a web page
        scr = drv.get_screenshot_as_png()
        # Convert img to BytesIO
        scr = Image.open(BytesIO(scr))
        # Convert to format accepted by OpenCV
        scr = numpy.asarray(scr, dtype=numpy.float32).astype(numpy.uint8)
        # Convert image from BGR to RGB format
        scr = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)

        # Image matching works only on gray images
        # (color conversion from RGB/BGR to GRAY scale)
        img_match = cv2.minMaxLoc(
            cv2.matchTemplate(cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY),
                              cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY),
                              cv2.TM_CCOEFF_NORMED))
        # Calculate position of found element
        self.x = img_match[3][0]
        self.y = img_match[3][1]

        # From full screenshot crop part that matches template image
        scr_crop = scr[self.y:(self.y + self.height),
                   self.x:(self.x + self.width)]

        # Calculate colors histogram of both template# and matching images and compare them
        scr_hist = cv2.calcHist([scr_crop], [0, 1, 2], None,
                                [8, 8, 8], [0, 256, 0, 256, 0, 256])
        img_hist = cv2.calcHist([self.img], [0, 1, 2], None,
                                [8, 8, 8], [0, 256, 0, 256, 0, 256])
        comp_hist = cv2.compareHist(img_hist, scr_hist,
                                    cv2.HISTCMP_CORREL)

        # Save treshold matches of: graphical image and image histogram
        self.threshold = {'shape': round(img_match[1], 2), 'histogram': round(comp_hist, 2)}

        # Return image with blue rectangle around match
        return cv2.rectangle(scr, (self.x, self.y),
                             (self.x + self.width, self.y + self.height),
                             (0, 0, 255), 2)