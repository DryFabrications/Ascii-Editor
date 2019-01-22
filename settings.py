#!/usr/bin/env python3

import json
import os

INSTALL_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(INSTALL_DIR, 'config.json')


def read_config(config_file):
    """Reads the config json file and returns the contents as a dictionary"""
    with open(config_file) as config_data:
        return json.load(config_data)


def resolution(config):
    """Returns the x and y values for the resolution of your canvas in a list"""
    error_msg = 'ERROR: Resolution value invalid. eg: \'200,200\''
    raw_res = config['resolution']
    res = raw_res.split(',')

    if len(res) is 2:
        try:
            res[0] = int(res[0])
            res[1] = int(res[1])
        except ValueError:
            print(error_msg)
            exit(10)
    else:
        print(error_msg)

    return res
