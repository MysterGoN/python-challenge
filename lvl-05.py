# Start page: http://www.pythonchallenge.com/pc/def/peak.html

import os
import pickle

from common import EXTERNAL_FOLDER, download_file
from pprint import pprint
from urllib import request

file_name = 'banner.p'
sound_page = f'http://www.pythonchallenge.com/pc/def/{file_name}'

file_path = os.path.join(f'{EXTERNAL_FOLDER}/{file_name}')

download_file(sound_page, file_path)

with open(file_path, 'br') as f:
    data = pickle.load(f)

for line in data:
    res_line = ''
    for symbol, count in line:
        res_line += symbol*count
    print(res_line)
