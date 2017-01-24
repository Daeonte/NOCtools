from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
	# login to the UW tools
	driver.get('https://weblogin.washington.edu/')

	username = driver.find_element_by_id('weblogin_netid')
	username.clear()	# clears existing characters in field
	username.send_keys('Enter your username')	# enters text (usrname)

	password = driver.find_element_by_id('weblogin_password')
	password.clear()	# clears existing characters in field
	password.send_keys('Enter your password')	# enters text (psswrd)

	driver.find_element_by_name('submit').click()	# clicks login button