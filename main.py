from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("https://autos.trovit.com.ec/autos/quito")
pa = driver.find_element(By.CLASS_NAME,"js-loadPremium")
for f in pa:
 precio = f.find_element(by=By.CLASS_NAME,value="item-title")
  #  room = p.find_element(by=By.CLASS_NAME,value="df597226dd")
 print(precio)
#print(room)
driver.close()
