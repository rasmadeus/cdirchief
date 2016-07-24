# -*- coding: utf-8 -*-

import unittest
import os
import json
import shutil
import cdir

class CdirTest(unittest.TestCase):

    def setUp(self):
        self._test_dir = 'test'
        self._test_file = 'test_file.txt'
        self._config_file = 'config.json'
        self._dirs = [str(i) for i in range(5)]

        os.mkdir(self._test_dir)

        self._create_dirs()
        self._create_src()
        self._create_config()


    def _data(self):
        return {'src': self._path(self._test_file), 'dirs': [self._path(dir) for dir in self._dirs]}


    def _path(self, path):
        return os.path.join(self._test_dir, path)


    def _create_dirs(self):
        for dir in self._dirs:
            os.mkdir(self._path(dir))


    def _create_config(self):
        with open(self._path(self._config_file), 'w') as config_file:
            data = json.dumps(self._data(), indent=4)
            config_file.write(data)


    def _create_src(self):
        with open(self._path(self._test_file), 'w') as src_file:
            src_file.write('test data')


    def tearDown(self):
        shutil.rmtree(self._test_dir)


    def test_cdir(self):
        cdir.cdir_from_config(self._path(self._config_file))
        for dir in self._dirs:
            path_to_dir = self._path(dir)
            path_to_file = os.path.join(path_to_dir, self._test_file)
            self.assertTrue(os.path.isfile(path_to_file))
