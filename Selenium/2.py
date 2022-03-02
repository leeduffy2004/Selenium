from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/AscII.html")

try:
    element1 = driver.find_element_by_name("msg1")
    element1.send_keys("Lee is BACK DB007")
#driver.quit() will close the browswer automatically!
    print("===============================>")

except NoSuchElementException:
    print("OOPs Lee has created the Element with the name of msg1>")



time.sleep(3)
driver.quit()