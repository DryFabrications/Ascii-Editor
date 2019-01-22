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
    raw_res = config['resolution']
    res = raw_res.split(',')

    def error_handle():
        print('ERROR: Resolution value invalid. eg: \'200,200\'')
        exit(10)

    if len(res) is 2:
        try:
            res[0] = int(res[0])
            res[1] = int(res[1])
        except ValueError:
            error_handle()
    else:
        error_handle()

    return res
