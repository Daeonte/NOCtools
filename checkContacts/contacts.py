#!/usr/bin/env python

import csv	# for file manipulation

import subprocess
import re
import sys

fqdn = sys.argv[1]
contact = sys.argv[2]

callConi = subprocess.Popen(('coni', fqdn), stdout=subprocess.PIPE)

checkHead = subprocess.Popen('head -11', stdin=callConi.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

callConi = subprocess.Popen(('coni', fqdn), stdout=subprocess.PIPE)

checkName = subprocess.Popen(('grep', contact, '-A 7'), stdin=callConi.stdout, stdout=subprocess.PIPE).communicate()[0]

print checkHead + checkName

