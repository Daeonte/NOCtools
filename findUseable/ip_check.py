#!/usr/bin/env python

"""
exceptions

drop sub from find_useable into module *
snstatus on sub *
grep subnet line *
regex subnet line to /xx
convert xx to int 
subtract 32 from int
2 ^ difference to give useable

for each useable reserve first and last
check: if 256 useable -> reserve .100-.103
for each useable range reserve first next 4 after first

useful below
subi 10.146.177.1 | sed '3q;d' | awk '{print $1}'
"""

import subprocess
import re
import sys

def exclude(sub):
	snstatus = subprocess.Popen(('snstatus', sub), stdout=subprocess.PIPE)
	findSubnet = subprocess.Popen('grep Subnet', stdin=snstatus.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]
	
	print findSubnet
	
	subnetValue = subnet(findSubnet)
	return subnetValue
	
def subnet(line):
	s = line
	r = re.compile('([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})(.*$)')
	alter = r.sub(r'\5',line)
	return alter[-3:]

sub = sys.argv[1]
a = exclude(sub)
subnetNum = int(a)
print subnetNum
