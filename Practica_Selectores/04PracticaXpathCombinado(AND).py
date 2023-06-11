import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = Options()

options.add_argument("start-maximized")
options.add_argument("disable-extensions")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://demoqa.com/text-box")
time.sleep(2)

""" Cuando se hace dificil de encontrar el elemento, lo recomendable es fortalecer el selector con el operador
logico (and) que permite acortar la selección

Ejemplo     //input[@type='text' and @id='userName'] 
            //entrada[Primer Valor and Segundo Valor]
"""


nom= driver.find_element(By.XPATH,"//input[@type='text' and @id='userName']").send_keys("Edwin")
time.sleep(1)
email= driver.find_element(By.XPATH,"//input[@type='email' and @id='userEmail']").send_keys("prueba@prueba.com.ar")
time.sleep(1)
dir= driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address' and @id='currentAddress']").send_keys("Dirección Principal")
time.sleep(1)
dir2= driver.find_element(By.XPATH,"//textarea[@rows='5'and @id='permanentAddress']").send_keys("Dirección Segundaria")
time.sleep(1)

"""" En ciertas ocasiones los elementos no se identificados por la automatización para eso es requerido
realizar un Scroll con el siguiente comando de JavaScript. (driver.execute_script("window.scrollTo(0,600)") """

submit= driver.find_element(By.XPATH,"//button[@type='button' and @id='submit']").click()
driver.execute_script("window.scrollTo(0,600)")
time.sleep(3)
driver.close()