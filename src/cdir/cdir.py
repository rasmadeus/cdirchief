# -*- coding: utf-8 -*-

import shutil
import json


def  _cdir(dirs, source_file):
    for dir in dirs:
        try:
            shutil.copy(source_file, dir)
            print('{file} copied to {dir}'.format(file=source_file, dir=dir))
        except IOError as ex:
            print('Cannot copy {file} to {dir} because {ex}'.format(file=source_file, dir=dir, ex=ex))


def _read_config(config_file):
    try:
        data = json.loads(config_file.read())
        _cdir(data['dirs'], data['src'])
    except ValueError as ex:
        print('Cannot read config because {ex}'.format(ex=ex))


def cdir_from_config(path_to_config):
    try:
        with open(path_to_config, 'r') as config_file:
            _read_config(config_file)
    except OSError as ex:
        print(ex)
