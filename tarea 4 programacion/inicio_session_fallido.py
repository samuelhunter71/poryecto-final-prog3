from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Chrome()
driver.get("https://plataformavirtual.itla.edu.do/login/index.php")

# driver.get_screenshot_as_file("C:\Users\samuel\Desktop\tarea 4 programacion")

usuario = driver.find_element(By.ID,"username")
usuario.send_keys("202010618")

time.sleep(5)

clave = driver.find_element(By.ID,"password")
clave.send_keys("Samuel14")
clave.send_keys(Keys.ENTER)

time.sleep(3)

body= driver.find_element(By.XPATH, "/html/body")
body.screenshot('capturas_de_pantalla/inicio_fallido.png')

time.sleep(10)