"""revised script to find useable IP addresses based on new output"""

import subprocess
import timeSince
import sys
import csv

import timeSince as ts
import ip_check as ipc
import potential_ip as potip

def findIP(sub):
	freeAddresses = subprocess.Popen("snstatus " + subnet + " | grep free | awk '{print $1}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)	# grabs the last line of snstatus ::= equivalent to the available addresses in a subnet
	free = freeAddresses.communicate()[0].split()
	return free

subnet = sys.argv[1]
numAddresses = int(sys.argv[2])	# need to interpret input as int not raw data for reasons I still need to look into

addresses = []
reserve = []

callSubi = subprocess.Popen('subi ' + subnet, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
subi = callSubi.communicate()[0]

exception = sys.argv[3]
print exception

if ('*' not in subi or exception): 
	print 'Currently running...'
	
	firstFour, subnetSlash = ipc.CIDR(subnet)
	subnetLine = firstFour[0] + '.' + firstFour[1] + '.' + firstFour[2] + '.' + firstFour[3] + '/' + subnetSlash
	subMask = ipc.subnetMask(subnetSlash)
	defGate = ipc.defaultGateway(firstFour, subnetSlash)
	resForInfrastructure = potip.vrrp(firstFour, subnetSlash)
	
	#command to find useableIP
	addresses = findIP(subnet)
	for IP in addresses:
		if IP not in resForInfrastructure:
			if timeSince.daysSince(IP) > 0:
				reserve.append(IP)
				if numAddresses == len(reserve): break
else: 
	print subi
	
csvfile = "ip.txt"	# output file to store the IP addresses that will be reserved
open(csvfile, 'w').close()	# erases content of output file

# writes to the output file each value in the list, reserve, with each element on a its own line
with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in reserve:
		writer.writerow([val]) 
	writer.writerow(['Subnet: ' + subnetLine])
	writer.writerow(['Subnet Mask: ' + subMask])
	writer.writerow(['Default Gateway: ' + defGate])
