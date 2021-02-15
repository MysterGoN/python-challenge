# Start page: http://www.pythonchallenge.com/pc/def/oxygen.html

import os
from PIL import Image, ImageDraw

from common import EXTERNAL_FOLDER, IGNORE_FOLDER, download_file
from pprint import pprint


file_name = 'oxygen.png'
file_url = f'http://www.pythonchallenge.com/pc/def/{file_name}'
file_path = f'{EXTERNAL_FOLDER}/{file_name}'

if not os.path.exists(file_path):
    download_file(file_url, file_path)

image = Image.open(file_path)
draw = ImageDraw.Draw(image)
width = image.width
height = image.height
pixels = image.load()

print(f'width={width}, height={height}')

x_min, x_max = 0, 607
y_min, y_max = 43, 51

prev_pix = None
res = ''
for x in range(x_min, x_max + 1):
    pix = pixels[x, y_min][0]
    
    if pix != prev_pix:
        prev_pix = pix
        res += chr(pix)

print(res)

lvl = [105, 10, 16, 101, 103, 14, 105, 16, 121]
lvl = [105, 110, 116, 101, 103, 114, 105, 116, 121]

pprint(''.join([chr(x) for x in lvl]))
