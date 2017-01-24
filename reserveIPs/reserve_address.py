from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium_functions as sf
import login_uw as luw
import csv	# to use text file as input for list of ip addresses

ips = open('ip.txt', 'r')	# text file for ip addresses

driver = webdriver.Firefox()	# opens firefox to use as browser

# login to the UW tools
luw.login(driver)

# DNSMgr
address = "https://barista.cac.washington.edu/dnsmgr/#/fqdn/"	# website to input DNS records
driver.get(address)

for line in ips:
	ip = line	# ip alter records on
	reservation_comment = ""	# reservation comment to add to comment field

	""" searches for the specified ip address """
	sf.search(driver, ip)

	""" reserve IP address with reservation comment """
	sf.reserve_address(driver, reservation_comment)

	""" confirm change """
	sf.confirm_first_element(driver)
	
driver.quit()	# closes the window/keeps selenium cache low
