#!/usr/bin/env python3
import requests
import uuid
import sys
import re
import builtins
import base64

def downloadImageFromUrl(url, path):
    if not url.startswith('http'):
        return None
    img_data = requests.get(url).content
    fPath = path+'/'+str(uuid.uuid1())+'.jpg'
    with open(fPath, 'wb') as handler:
        handler.write(img_data)
    return fPath

def print(ftext, **args):
    if sys.stdout.isatty():
        builtins.print (ftext, flush=True, **args)
    else:
        builtins.print(re.sub('\33\[\d+m',' ',ftext), flush=True, **args)

def hideURL(url):
    message_bytes = url.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return "atob('{}')".format(base64_message)