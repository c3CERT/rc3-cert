#!/usr/bin/env python3
from PIL import Image
import sys
import os

BASE_DIR = 'imgs'
COMPOSE_TILESHEETS = True
TILESHEET_WIDTH = 512

class Row():
    def __init__(self, width=TILESHEET_WIDTH, height=32):
        self.width = width
        self.height = height
        self.remainingWidth = width
        self.sprites = []

    def append(self, Img):
        x,y = Img.size
        if (self.remainingWidth  - x) < 0:
            raise Exception('ImageTooLarge')
        self.height = max(self.height, y)
        self.remainingWidth = self.remainingWidth - x
        self.sprites.append(Img)
        return self.remainingWidth

    def merge(self):
        Image.new('RGBA', (self.width, self.height),(255,255,255,0))
        x_offset = 0
        for img in self.sprites:
            x,y = img.size
            Image.alpha_composite(img, (x_offset,0))
            x_offset += x
        return Image


print("Check images dimensions")
print('Absolute path:', os.getcwd() + '/imgs')
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
     if file.endswith('.png'):
      x,y = Image.open(os.path.join(root, file)).size
      if not(x % 32 == y % 32 == 0):
          sys.exit("%s has wrong dimensions." % file)


if COMPOSE_TILESHEETS:

    for dir in os.listdir(BASE_DIR):
        if dir != "tilesheets":
            name = dir
            row = Row()
            for file in os.listdir(os.path.join(BASE_DIR, dir)):
                try:
                    row.append(Image.open(os.path.join(BASE_DIR, dir, file)))
                except:
                    break
            row.merge().save('row.png')