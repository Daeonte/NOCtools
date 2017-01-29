#!/usr/bin/env python

import subprocess
import re
import sys

def CIDR(sub):
	snstatus = subprocess.Popen(('snstatus', sub), stdout=subprocess.PIPE)
	findSubnet = subprocess.Popen('grep Subnet', stdin=snstatus.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]

	cidrNotation = re.compile('([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})(.*$)')
	slash = cidrNotation.search(findSubnet).group(5)
	firstThreeOctets = cidrNotation.search(findSubnet).group(1,2,3,4)
	return firstThreeOctets, slash[-2:]

def defaultGateway(firstFour, subnet):
	if (subnet == '24'):
		dg = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.100'
	else:
		lastOctet = int(firstFour[3]) + 1
		dg = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.' + str(lastOctet)
	return dg
	
# to build octet within subnetMask method
def octet(subnet):
	sValue = 255
	if (subnet <= 8):
		nBits = 8 - subnet 
		shiftValue = sValue << 8
		newValue = shiftValue >> subnet
		sValue = 255 & newValue		
	return str(sValue)

# last two refers to the slash
def subnetMask(subnet):
	subnet = int(subnet)
	sM = ['0','0','0','0']
	count = 0
	while (subnet >= 0):
		sM[count] = octet(subnet)
		subnet = subnet - 8
		count = count + 1
	return sM[0] + '.' + sM[1] + '.' + sM[2] + '.' + sM[3]
