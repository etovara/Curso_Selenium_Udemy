from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\Chome_Driver\chromedriver.exe")

driver = webdriver.Firefox(executable_path="C:\Program Files\Python310\Firefox_Driver\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")
print(driver.title)

driver.close()