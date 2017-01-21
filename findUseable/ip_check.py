#!/usr/bin/env python

"""
exceptions

drop sub from find_useable into module *
snstatus on sub *
grep subnet line *
regex subnet line to /xx *
convert xx to int *
subtract 32 from int
2 ^ difference to give useable

for each useable reserve first and last
check: if 256 useable -> reserve .100-.103
for each useable range reserve first next 4 after first

"""

import subprocess
import re
import sys

def CIDR(sub):
	snstatus = subprocess.Popen(('snstatus', sub), stdout=subprocess.PIPE)
	findSubnet = subprocess.Popen('grep Subnet', stdin=snstatus.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

	cidrNotation = re.compile('([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})(.*$)')
	subnetMask = cidrNotation.search(findSubnet).group(5)
	firstThreeOctets = cidrNotation.search(findSubnet).group(1,2,3,4)
	return firstThreeOctets, subnetMask[-2:]

sub = sys.argv[1]
firstFour, subnet = CIDR(sub)

if (subnet == '24'):
	defaultGateway = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.100'
else:
	lastOctet = int(firstFour[3]) + 1
	defaultGateway = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.' + str(lastOctet)
print defaultGateway