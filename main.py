from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = chrome)
driver.get("https://www.wikipedia.org")

click_on_search = driver.find_element(By.NAME,value="search")
click_on_search.send_keys("Python programming language")
click_on_search.send_keys(Keys.RETURN)

time.sleep(3)
driver.close() 
