# pip list lists all python related libraries

"""Search Wikipedia for All Entries Relating to Cajun Fiddle Music"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") #Paste in path to Chrome webdriver
driver.implicitly_wait(120) # time in seconds
driver.get("https://en.wikipedia.org/wiki/Main_Page") # get Wikipedia 
print(driver.title) # print title of page
print(driver.current_url) 

search = driver.find_element_by_name("search")
print(search.is_displayed())
print(search.is_enabled())

driver.find_element_by_name("search").click()
driver.find_element_by_name("search").send_keys("cajun fiddle")
driver.find_element_by_name("go").click()
crawl_page = driver.current_url
print(crawl_page)


time.sleep(30)
driver.close() # Closes most recent browser/window
driver.quit() # quits all browsers


#driver.implicitly_wait(5)