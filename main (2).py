from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome)
driver.get("")
time.sleep(5)

Input_name = driver.find_element(By.NAME , value="fName")
time.sleep(1)
Input_name.send_keys("<First name>")
Input_name.send_keys(Keys.ENTER)
time.sleep(1)
Last_name = driver.find_element(By.NAME,value="lName")
Last_name.send_keys("<Last name>")
Last_name.send_keys(Keys.ENTER)
time.sleep(1)
Email_Input = driver.find_element(By.NAME, value="email")
Email_Input.send_keys("<Your Email>")
Email_Input.send_keys(Keys.ENTER)
time.sleep(1)
language_selection = driver.find_element(By.ID,value="langSelect-EN")
language_selection.click()
