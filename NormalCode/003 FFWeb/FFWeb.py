from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path = 'C:\Learning\PythonTraining\chromedriver.exe')

driver = webdriver.Chrome(service=service)

# url
url = 'http://localhost/FFWeb'
driver.get(url)

import time
time.sleep(2)


time.sleep(1)

# 获取按钮_
button = driver.find_element(By.XPATH,'//div[@class="pull-right"]/a')

# 点击按钮
button.click()


time.sleep(1)

item = driver.find_element(By.XPATH,'//ul[@class="nav"]/li[2]/a')
item.click()

time.sleep(1)

item1 = driver.find_element(By.XPATH,'//div[@id="webClientPlugins"]/ul/li[3]/a')
item1.click()
time.sleep(1)

item2 = driver.find_element(By.XPATH,'//ul[@class="breadcrumb"]/li[4]/a')
item2.click()

time.sleep(20)

input=driver.find_element(By.XPATH,'//input[@id="btnConfirm"]')
input.click()
time.sleep(1)



time.sleep(50)

# 退出
driver.quit()