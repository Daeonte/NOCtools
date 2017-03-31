#!/usr/bin/env python

import subprocess
import re
import sys

fqdn = sys.argv[1]
contact = sys.argv[2]

callConi = subprocess.Popen(('coni', fqdn), stdout=subprocess.PIPE)

checkHead = subprocess.Popen('head -7', stdin=callConi.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

checkName = subprocess.Popen('grep ' + contact + ' -B 3 -A 4', stdin=callConi.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

print checkHead + '\n' + checkName

