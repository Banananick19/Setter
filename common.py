import os
import sys

def run_config(config_apps):
    errors = {}
    for app in config_apps:
        if os.path.exists(config_apps[app]) and os.path.isfile(config_apps[app]):
            os.popen(config_apps[app])



