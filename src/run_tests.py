#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


if __name__ == "__main__":
    suite = unittest.TestLoader().discover(start_dir='./cdir/', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=1).run(suite)
