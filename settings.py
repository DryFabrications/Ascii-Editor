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
    res = config['resolution']
    return res.split(',')
