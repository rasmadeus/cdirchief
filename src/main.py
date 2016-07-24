#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from cdir import cdir


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', help='Specify config file')
    return parser


if __name__ == "__main__":
    args = create_parser().parse_args()
    cdir.cdir_from_config(args.config)
