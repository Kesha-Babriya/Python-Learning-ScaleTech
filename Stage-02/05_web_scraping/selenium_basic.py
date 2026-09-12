from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#webdriver test webpages on various browser nd various os

driver = webdriver.Chrome()

driver.get("https://books.toscrape.com/index.html")

print(driver.title)

old_url = driver.current_url

print("Old url",old_url)
print("Initial title",driver.title)

#navigate in travel link

driver.find_element(By.LINK_TEXT , "Travel").click()
time.sleep(3)
new_url = driver.current_url
print("new url" , new_url)
print("New title" , driver.title)

#again go to home and go to mystery

driver.find_element(By.LINK_TEXT , "Home").click()
driver.find_element(By.LINK_TEXT , "Mystery").click()

print("Mystery url",driver.current_url)

driver.quit

#-----------------------------------------

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search = driver.find_element(By.NAME , "q")
search.send_keys("Drishyam")
search.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()



