# -*- coding: utf-8 -*-

import os
from distutils.core import setup

def get_files(dirs, prefix=None):
    oldpwd = os.path.abspath(os.curdir)
    if prefix:
        os.chdir(prefix)

    result = []
    for dir in dirs:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                result.append(os.path.join(dirpath, filename))

    os.chdir(oldpwd)
    return result

setup(
    name='django-debug-toolbar',
    version='0',
    packages=(
        'debug_toolbar',
        'debug_toolbar.toolbar',
        'debug_toolbar.panels',
    ),
    package_data={
        'debug_toolbar': get_files(['media', 'templates'], 'debug_toolbar'),
    },
)
