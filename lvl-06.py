# Start page: http://www.pythonchallenge.com/pc/def/channel.html

import os
from pprint import pprint
import shutil
import zipfile

from common import EXTERNAL_FOLDER, IGNORE_FOLDER, download_file


START_FILE_NUMBER = 90052

file_name = 'channel.zip'
file_url = f'http://www.pythonchallenge.com/pc/def/{file_name}'
file_path = f'{EXTERNAL_FOLDER}/{file_name}'

download_file(file_url, file_path)

lvl_folder = 'lvl-06'
unzip_folder = os.path.join(IGNORE_FOLDER, lvl_folder)

if os.path.exists(unzip_folder):
    shutil.rmtree(unzip_folder)

comments = []
with zipfile.ZipFile(file_path, 'r') as z:
    comments = {int(x.filename.split('.')[0]): x.comment.decode('utf-8') for x in z.infolist() if x.filename != 'readme.txt'}
    z.extractall(unzip_folder)


file_name_tpl = '{}.txt'

number = START_FILE_NUMBER
message = '\n\n'
while True:
    with open(os.path.join(unzip_folder, file_name_tpl.format(number)), 'r') as f:
        text = f.read()
        print(text)
        try:
            number = int(text.strip().split(' ')[-1])
            message += comments[number]
        except ValueError:
            break

print(message)
