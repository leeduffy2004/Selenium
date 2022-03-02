from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/AscII.html")
element1 = driver.find_element_by_name("msg1")
element1.send_keys("Lee is BACK DB007")
#driver.quit() will close the browswer automatically!

time.sleep(3)
button1 = driver.find_element(by=By.NAME, value="btn1")
button1.click()
time.sleep(3)

button2 = driver.find_element(by=By.ID, value="B")
button2.click()
time.sleep(3)

button3 = driver.find_element_by_name("btn3")
button3.click()

element2 = driver.find_element(by=By.NAME, value="msg2")
data =  element2.get_attribute("value")

print("=====================================",data)

element3 = driver.find_element(by=By.ID, value="T")
data1 = element3.text

print("=====================================",data1)

if data1 == "36":

    time.sleep(3)
driver.quit()