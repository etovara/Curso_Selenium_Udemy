import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()

options.add_argument("start-maximized")
options.add_argument("disable-extensions")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://demoqa.com/text-box")
time.sleep(2)

nom= driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys ("Edwin")
time.sleep(2)


driver.close()