'''
    File name: network_location.py
    Author: Netics W
    Date created: 1/11/2017
    Date last modified: 1/11/2017
    Python Version: 3.5
'''

import json
import sys

print(len(sys.argv))
if len(sys.argv) != 3:
    print("Incorrect syntax!")
    print("             Usage: python -f network_location.py <full path to config.json> <network SSID>")
    sys.exit()

try:
    with open(sys.argv[1]) as netconf:
        try:
            nets = json.load(netconf)
        except json.decoder.JSONDecodeError:
            print("Config file is not well JSON-formatted file")
            sys.exit()
    try:
        print(nets[sys.argv[2]])
    except KeyError:
        print("Network SSID is not found in config file")
except FileNotFoundError:
    print("Config file provided is not found")
