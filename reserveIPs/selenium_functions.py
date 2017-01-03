from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search(driver, fqdn):
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#core-content-container input.form-control[ng-model='query'][placeholder='Full domain name']")))	# finds the search bar 
	element.click()
	element.clear()
	element.send_keys(fqdn)	# enters ip in search bar
	
	button = driver.find_element(By.XPATH, "//button[text()='GoTo ResourceRecords']")	# find search button
	button.click()	# and click submit

def add_new_record(driver):
	driver.find_element(By.XPATH, "//button[text()='Add new record']").click() # have this click in here to mess with the toggle for the time being
	addNewRecord = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add new record']"))) # find 'Add New Record' button
	addNewRecord.click()	# properly clicks
	
def add_record(driver):
	add_new_record(driver)
	
	select = driver.find_element(By.CSS_SELECTOR, "select.form-control")	# opens record type dropbox menu
	select.find_element(By.XPATH, "//option[text()='A']").click()	# selects reservation
	
def add_related(driver):
	add_record(driver)
	select = driver.find_element(By.CSS_SELECTOR, "select.form-control")	# opens record type dropbox menu
	select.find_element(By.XPATH, "//option[text()='A']").click()	# selects reservation
	
def fill_record_text(driver, text):
	#text_box = driver.find_element(By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[3]/div[1]/div[3]/div[1]/form/div/div/span/input")
	text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[3]/div[1]/div[4]/div/form/div/div/span/input")))
	#text_box.clear()
	text_box.send_keys(text)
	
def reserve_address(driver, reservation_comment):
	add_new_record(driver)

	select = driver.find_element(By.CSS_SELECTOR, "select.form-control")	# opens record type dropbox menu
	select.find_element(By.XPATH, "//option[text()='reservation']").click()	# selects reservation
	#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//option[text()='reservation']"))).click()
	
	fill_record_text(driver, reservation_comment)

def del_related(driver):
	#find the delete related checkbox
	delRelated = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[4]/div[2]/div[1]/div[2]/div/div[2]/div/label/input")))
	delRelated.click()

	# clicks the delete related checkbox
	deleteRecord = driver.find_element(By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[1]/span[1]/button")
	deleteRecord.click()	# properly clicks
	
def delete_first(driver):
	# finds the first record's delete button and presses it
	delete_single = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[1]/span[1]/button")))
	delete_single.click()
	
def confirm_first_element(driver):
	confirm_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='core-content-container']/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/div/div[1]/span/button")))	# finds the confirms/add button
	confirm_button.click()	# confirms/add the reservation
	