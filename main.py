#!/usr/bin/env python
import sys
if sys.version_info[0] == 3:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')
torpath = config.get('tor', 'torpath')
torrc = config.get('tor', 'torrc')
c = []

for arg in sys.argv[1:]:
    print(arg)
'''
ExitNodes {ua}
StrictNodes 1

ExitNodes {ua},{ug},{kp},{ie}

'''