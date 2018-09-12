#!/usr/bin/env python
import datetime
from shutil import copyfile
import sys
import os
if sys.version_info[0] == 3:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

'''
WARNING: The Tor Project devs dont like the idea of changing entry/exit nodes.

Use this script if you know what you are doing and at your own risk.
'''
config = ConfigParser()
config.read(os.getcwd() + os.path.sep + 'config.ini')
torpath = config.get('tor', 'torpath')
torrc = config.get('tor', 'torrc')
c = []
p = []
m = False
v = r'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

for arg in sys.argv[1:]:
    #TODO: Some real validation should be nice to have
    if len(arg) > 2:
        sys.exit('< ' + arg + ' > not a valid country code. See %s for a list' \
        'of countries. Aborting.' %v)
    c.append(arg)

rc = torpath + os.path.sep + torrc + os.path.sep + 'torrc'
if os.path.exists(rc):
    with open(rc, "r") as f:
        for l in f:
            if 'ExitNodes' in l:
                pass
            elif 'StrictNodes' in l:
                pass
            else:
                p.append(l)
else:
    sys.exit('Missing configuration or wrong values or' \
     ' < %s > lacks proper permissions. Aborting.' %rc)

if len(c) > 1:
    o = 'ExitNodes '
    for i in c:
        o +='{%s},' % i
    p.append(o.rstrip(',') + '\n')
else:
    o = 'ExitNodes {%s}\n'
    p.append(o %c[0])
    p.append('StrictNodes 1\n')

ed = os.path.getmtime(rc)
now = datetime.datetime.fromtimestamp(ed).strftime("%b%d%Y%H")
copyfile(rc, rc + '.bk.' + now)

with open(rc, "w") as f:
    for l in p:
        f.write(l)
sys.exit(0)