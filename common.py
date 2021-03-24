import os
import shutil
from typing import Optional

import requests
from requests.auth import HTTPBasicAuth

EXTERNAL_FOLDER = 'external'
IGNORE_FOLDER = f'{EXTERNAL_FOLDER}/ignore'

if not os.path.exists(EXTERNAL_FOLDER):
    os.mkdir(EXTERNAL_FOLDER)


def download_file(url: str, target: str, user: Optional[str] = None, password: Optional[str] = None):
    auth = None
    if user is not None and password is not None:
        auth = HTTPBasicAuth(user, password)

    r = requests.get(url, stream=True, auth=auth)
    if r.status_code == 200:
        with open(target, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
