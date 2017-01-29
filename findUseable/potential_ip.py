#!/usr/bin/env python

"""
only used to determine vrrp exceptions for /24 and higher addresses 
vrrp exceptions are for those ip addresses which are reserved for infrastructure use 
"""

import sys

def inter(altSub):
	iterVal = 1	# use 255 because that represents a fully active octet
	nBits = 8 - altSub	# this number is the number of bits in, starting from the left, until you hit the bit representing the number of useable addresses
	iterVal = iterVal << nBits	# this shifts the 'on' bit to the place in the octet representing the number of useable addresses 
	return iterVal	# returns the number of useable addresses

def unuseable(resForInfrastructure, interval):
	start = 0
	while(start < 255):
		resForInfrastructure.append(start)
		for x in range(1,5):
			resForInfrastructure.append(start + x)
		resForInfrastructure.append(start + interval - 1)
		start = start + interval
	return resForInfrastructure

def vrrp(firstFour, subnetSlash):
	firstThreeOctets = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.'

	# returns the number of useable addresses give a subnet
	interval = inter(int(subnetSlash) - 24)

	# list of ip addresses that can not be used
	resForInfrastructure = []
	# since /24 is a special case I hard code this. algorithmically we would have to look at the defaultgateway and work from there. may do so in later commit
	if (subnetSlash == 24):
		resForInfrastructure = [0, 100, 101, 102, 103, 255]
	else:
		resForInfrastructure = unuseable(resForInfrastructure, interval)
	
	for i in range(0, len(resForInfrastructure)):
		resForInfrastructure[i] = firstThreeOctets + str(resForInfrastructure[i])

	return resForInfrastructure
