from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Python310\Chome_Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
time.sleep(2)

nom= driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys ("Edwin")
time.sleep(2)


driver.close()