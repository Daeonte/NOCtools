#!/usr/bin/env python

import subprocess
import re
import datetime

def daysSince(address):
	# pipe output into a command
	proc = subprocess.Popen('adhist ' + address, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	output, waste = proc.communicate()

	# return 1 if useable, return -1 if not usable
	if 'last poll' in output:
		return -1
	elif 'has not been in use' in output:
		return 1
	elif 'since' in output:
		# greps to find the line containing the date
		procAgain = subprocess.Popen(('adhist', address), stdout=subprocess.PIPE)
		key = subprocess.Popen(('grep', 'since'), stdin=procAgain.stdout, stdout=subprocess.PIPE).communicate()[0]

		# regular expression to find the date from the command
		match = re.search(r'(\d+-\d+-\d+)', key)
		helpful = match.group(1)
		
		# creates new datetime object and grabs the difference between the two dates
		today = datetime.datetime.today()
		compare = datetime.datetime.strptime(helpful, '%Y-%m-%d')
		daysSince = today - compare

		if daysSince.days > 90:
			return 1
		else:
			return -1