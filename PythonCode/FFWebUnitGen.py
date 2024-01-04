from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path = 'C:\Learning\Python\Code\chromedriver.exe')

driver = webdriver.Chrome(service=service)

# url
url = 'http://localhost/FFWeb293'
driver.get(url)

import time
time.sleep(2)

# 获取文本框的对象
input = driver.find_element(By.ID, 'UserName')

# 输入用户名
input.send_keys('admin')

time.sleep(1)

Password=driver.find_element(By.ID,'Password')

Password.send_keys('admin')

time.sleep(1)

# 获取按钮_
button = driver.find_element(By.XPATH,'//div[@class="buttons"]/button')

# 点击按钮
button.click()


time.sleep(1)

item = driver.find_element(By.XPATH,'//ul[@id="select2-PoNumbers-results"]/li')
item.click()


#dropdownlist=driver.find_element(By.ID,'PoNumbers')

#Select(driver.find_element(By.ID,'PoNumbers')).select_by_value("SuperPO00003")

time.sleep(1)

complete=driver.find_element(By.ID,'task-complete')

complete.click()

time.sleep(2)

SerialNumbersToGenerate=driver.find_element(By.ID,'SerialNumbersToGenerate')

SerialNumbersToGenerate.send_keys(20)


time.sleep(1)

completebutton=driver.find_element(By.ID,'task-complete')

completebutton.click()

time.sleep(50)

# 退出
driver.quit()