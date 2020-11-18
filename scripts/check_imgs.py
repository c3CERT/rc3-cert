#!/usr/bin/env python3
from PIL import Image
import sys
import os

print("Check images dimensions")
print('Absolute path:', os.getcwd() + '/imgs')
for root, dirs, files in os.walk('imgs'):
    for file in files:
     if file.endswith('.png'):
      x,y = Image.open(os.path.join(root, file)).size
      if not(x % 32 == y % 32 == 0):
          sys.exit("%s has wrong dimensions." % file)

