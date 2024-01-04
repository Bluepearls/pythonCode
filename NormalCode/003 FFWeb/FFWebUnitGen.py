from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path = 'C:\Learning\Pythontraining\chromedriver.exe')

driver = webdriver.Chrome(service=service)

# url
url = 'http://localhost/FFWeb'
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

item = driver.find_element(By.XPATH,'//ul[@id="select2-partFamilyId-results"]/li[2]')
item.click()

time.sleep(1)
item = driver.find_element(By.XPATH,'//ul[@id="select2-partId-results"]/li[2]')
item.click()


time.sleep(3)

""" complete=driver.find_element(By.ID,'task-complete')

complete.click()
 """
""" time.sleep(2)
 """
SerialNumbersToGenerate=driver.find_element(By.ID,'PanelsToGenerate')

SerialNumbersToGenerate.send_keys(2)


time.sleep(3)

completebutton=driver.find_element(By.ID,'task-complete')

completebutton.click()

time.sleep(30)

# 退出
driver.quit()