import os

from urllib import request


EXTERNAL_FOLDER = 'external'
IGNORE_FOLDER = f'{EXTERNAL_FOLDER}/ignore'

if not os.path.exists(EXTERNAL_FOLDER):
    os.mkdir(EXTERNAL_FOLDER)


def download_file(url: str, target: str):
    file = request.URLopener()
    file.retrieve(url, target)
