#!/usr/bin/env python
import datetime
import os
from shutil import copyfile
import sys
if sys.version_info[0] == 3:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

'''
WARNING: The Tor Project devs dont like the idea of changing entry/exit nodes.

Use this script if you know what you are doing and at your own risk.
'''

config = ConfigParser()
iso = os.getcwd() + os.path.sep + 'config.ini'
config.read(iso)
torpath = config.get('tor', 'torpath')
torrc = config.get('tor', 'torrc')
if not torpath or not torrc:
    sys.exit('Error. Missing configuration in < %s >. Aborting.' %iso)

stdin = []
prg = []
default = False
see = r'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

if not sys.argv[1:]:
    sys.exit('Please provide either one or a space-separated list of valid' \
    ' country codes, or < default > to reset Tor to default behaviour.')

for arg in sys.argv[1:]:
    if 'default' in arg.lower():
        default = True
    else:
        cd = []
        with open(os.getcwd() + os.path.sep + 'iso3166.tsv', "r") as csv:
            for line in csv:
                cd.append(line.split('\t'))
        ftl = [v for sublt in cd for v in sublt]
        if not arg.upper() in [s.strip('\n') for s in ftl]:
            sys.exit('Error. < ' + arg + ' > not a valid country code.' \
            ' See %s for a list of country codes. Aborting.' %see)
        stdin.append(arg.lower())

rc = torpath + os.path.sep + torrc + os.path.sep + 'torrc'
if os.path.exists(rc):
    with open(rc, "r") as f:
        for l in f:
            if 'ExitNodes' in l:
                pass
            elif 'StrictNodes' in l:
                pass
            else:
                prg.append(l)
else:
    sys.exit('Error. Missing configuration or wrong values or' \
     ' < %s > lacks proper permissions. Aborting.' %rc)

if not default:
    if len(stdin) > 1:
        o = 'ExitNodes '
        for i in stdin:
            o +='{%s},' % i
        prg.append(o.rstrip(',') + '\n')
    else:
        o = 'ExitNodes {%s}\n'
        prg.append(o %stdin[0])
        prg.append('StrictNodes 1\n')

ed = os.path.getmtime(rc)
now = datetime.datetime.fromtimestamp(ed).strftime("%b%d%Y%H")
copyfile(rc, rc + '.bk.' + now)

with open(rc, "w") as f:
    for l in prg:
        f.write(l)

sys.exit(0)