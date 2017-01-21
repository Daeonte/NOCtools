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

def CIDR(sub):
	snstatus = subprocess.Popen(('snstatus', sub), stdout=subprocess.PIPE)
	findSubnet = subprocess.Popen('grep Subnet', stdin=snstatus.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

	cidrNotation = re.compile('([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})(.*$)')
	subnetMask = cidrNotation.search(findSubnet).group(5)
	firstThreeOctets = cidrNotation.search(findSubnet).group(1,2,3)
	return firstThreeOctets, subnetMask[-2:]

sub = sys.argv[1]
firstThree, subnet = CIDR(sub)
print firstThree
print subnet