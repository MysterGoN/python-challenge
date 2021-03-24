# Start page: http://www.pythonchallenge.com/pc/return/5808.html

import os

from PIL import Image

from common import IGNORE_FOLDER, download_file


LVL_FOLDER = f'{IGNORE_FOLDER}/lvl-11'
FILE_LINK = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
FILE_PATH = f'{LVL_FOLDER}/cave.jpg'
USER = 'huge'
PASSWORD = 'file'

if not os.path.exists(LVL_FOLDER):
    os.makedirs(LVL_FOLDER, exist_ok=True)

if not os.path.exists(FILE_PATH):
    download_file(FILE_LINK, FILE_PATH, USER, PASSWORD)

source_image = Image.open(FILE_PATH)
width, height = source_image.size

pixels = source_image.load()

for x in range(width):
    for y in range(height):
        if 0 not in pixels[x, y]:
            pixels[x, y] = (0, 0, 0)

source_image.save(f'{LVL_FOLDER}/cave_back.jpg')

