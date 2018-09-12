#!/usr/bin/env python
import datetime
from functools import reduce
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
q = os.getcwd() + os.path.sep + 'config.ini'
config.read(q)
torpath = config.get('tor', 'torpath')
torrc = config.get('tor', 'torrc')
if not torpath or not torrc:
    sys.exit('Missing configuration in < %s >. Aborting.' %q)

c = []
p = []
m = False
v = r'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

for arg in sys.argv[1:]:
    cd = []
    with open(os.getcwd() + os.path.sep + 'iso3166.csv', "r") as csv:
        for line in csv:
            cd.append(line.split('\t'))
    ftl = [v for sublt in cd for v in sublt]
    if not arg.upper() in [s.strip('\n') for s in ftl]:
        sys.exit('< ' + arg + ' > not a valid country code. See %s for a list' \
        ' of country codes. Aborting.' %v)
    c.append(arg.lower())

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