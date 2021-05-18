'''
os_util.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
'''

import os
import shutil
import sys
from pathlib import Path


def dir_check(dir):
    try:
        os.makedirs(f'{os.getcwd()}/{dir}')
    except FileExistsError:
        pass

def os_start_file(file_name):
    if sys.platform == 'win32':
        os.system(f'start {file_name}')
    elif sys.platform == 'darwin':
        os.system(f'open {file_name}')

def clear_temp(file_name):
    shutil.rmtree(file_name)

def resolve_confict_png_name(png_name):
    original_png_name = png_name
    i = 1
    while Path(f'{png_name}.png').exists():
        png_name = f'{original_png_name}#{i}'
        i = i + 1
    return png_name