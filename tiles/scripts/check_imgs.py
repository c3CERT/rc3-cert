#!/usr/bin/env python3
from PIL import Image
import argparse
import sys
import os

BASE_DIR = 'imgs'
COMPOSE_TILESHEETS = True

parser = argparse.ArgumentParser(description='Checks Tilesheet dimensions and compose tilesheets from directories.')
parser.add_argument('--width', dest='width', type=int, default=512,
                    help='Max tilesheet width')

parser.add_argument('--height', dest='height', type=int, default=2048,
                    help='Max tilesheet height')
parser.add_argument('--ignore', action='store_true', help='ignore tilesheets with wrong dimensions')

args = parser.parse_args()

TILESHEET_WIDTH = args.width
TILESHEET_HEIGHT = args.height
IGNORE = args.ignore

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
        if self.height > TILESHEET_HEIGHT:
            raise Exception("Tilesheet full")
        self.remainingWidth = self.remainingWidth - x
        self.sprites.append(Img.convert(mode='RGBA'))
        return self.remainingWidth

    def render(self):
        row = Image.new('RGBA', (self.width, self.height),(255,255,255,0))
        x_offset = 0
        for img in self.sprites:
            x,y = img.size
            row.alpha_composite(img, (x_offset,0))
            x_offset += x
        return row

class Spritesheet():
    def __init__(self, width=TILESHEET_WIDTH, height=TILESHEET_HEIGHT):
        self.width = width
        self.height = height
        self.rows = []

    def append(self, Img):
        x,y = Img.size
        # self.height += y
        self.rows.append(Img)

    def render(self):
        sheet = Image.new('RGBA', (self.width, self.height),(255,255,255,0))
        y_offset = 0
        for img in self.rows:
            x,y = img.size
            sheet.alpha_composite(img, (0,y_offset))
            y_offset += y
        return sheet

if __name__ == "__main__":
    print("Check images dimensions")
    print('Absolute path:', os.getcwd() + '/imgs')
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
         if file.lower().endswith('.png'):
          x,y = Image.open(os.path.join(root, file)).size
          if not(x % 32 == y % 32 == 0 and x <= TILESHEET_WIDTH):
            if IGNORE:
                print("%s has wrong dimensions." % file)
            else:
              sys.exit("%s has wrong dimensions." % file)


    if COMPOSE_TILESHEETS:
        print("Generate Tilesheets")
        for dir in os.listdir(BASE_DIR):
            if dir != "tilesheets" and not (dir.endswith('.png') or dir.endswith('.ase')): 
                name = dir
                print("Processing:", dir)
                sheet = Spritesheet()
                row = Row()
                for file in sorted(os.listdir(os.path.join(BASE_DIR, dir)),key=str.lower):
                    try:
                        if file.endswith('.png'):
                            row.append(Image.open(os.path.join(BASE_DIR, dir, file)))
                    except:
                        # new row
                        sheet.append(row.render())
                        row = Row()
                        row.append(Image.open(os.path.join(BASE_DIR, dir, file)))
                        
                sheet.append(row.render())
                sheet.render().save(os.path.join(BASE_DIR, 'tilesheets', name + '.png'))

