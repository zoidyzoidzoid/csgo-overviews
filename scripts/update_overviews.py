#!/usr/bin/env python
# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

"""Convert an image to another file format supported by pyglet.

Usage::
    virtualenv virtualenv
    . virtualenv/bin/activate
    pip install -r requirements.txt
    python scripts/update_overviews.py

"""

from itertools import ifilter
import os
import shutil
import sys

import pyglet
from pyglet.image.codecs.png import PNGImageEncoder
from PIL import Image

BASE_DIR = os.getcwd()
OVERVIEWS_DIR = os.path.join(BASE_DIR, 'overviews')
RAW_OVERVIEWS_DIR = os.path.join(OVERVIEWS_DIR, 'raw')


def create_backup_file(path):
    shutil.copy(path, path.replace('.', '_bu.'))


class BackedUpFile(object):
    def __init__(self, path):
        self.path = path
        self.backup_path = path.replace('.', '_bu.')

    def __enter__(self):
        shutil.copy(self.path, self.backup_path)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print exc_type, exc_value, traceback

        os.remove(self.backup_path)
        return self


def convert_from_raw():
    raw_dir_files = os.listdir(RAW_OVERVIEWS_DIR)
    raw_file_names = ifilter(lambda x: x.endswith('.dds'), raw_dir_files)
    for raw_file_name in raw_file_names:
        raw_file_path = os.path.join(RAW_OVERVIEWS_DIR, raw_file_name)
        with BackedUpFile(raw_file_path):
            if not os.path.isfile(raw_file_path):
                sys.exit('wat')
            texture = pyglet.image.load(raw_file_path).get_texture()

            processed_file_name = os.path.split(raw_file_path)[-1].replace(
                '_radar.dds', '.png')

            dest_path = os.path.join(OVERVIEWS_DIR, processed_file_name)

            if os.path.isfile(dest_path):
                create_backup_file(dest_path)
                os.remove(dest_path)

            texture.save(dest_path, encoder=PNGImageEncoder())

            image = Image.open(dest_path)
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.resize((768, 768))
            image.save(dest_path)

if __name__ == '__main__':
    if not os.path.isdir(OVERVIEWS_DIR):
        sys.exit('overviews directory not found.\n'
                 'Are you running this from the root of the repo?')

    convert_from_raw()
