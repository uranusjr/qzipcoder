#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import zipcodetw


def ignore_copy(dirname, contents):
    return [
        item for item in contents
        if item.endswith('.py') or item.endswith('.csv')
    ]


os.system(
    'cxfreeze qzipcoder/main.py '
    '--target-dir dist '
    '--base-name Win32GUI '
    '--include-modules atexit,sqlite3,csv '
    '--exclude-modules zipcodetw '
    '--target-name=qzipcoder.exe -OO -c')

source_dir = os.path.dirname(zipcodetw.__file__)
target_dir = os.path.join('dist', 'zipcodetw')
shutil.copytree(source_dir, target_dir, ignore=ignore_copy)
