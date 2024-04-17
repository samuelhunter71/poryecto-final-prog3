from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest

class XPathTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
        time.sleep(5)

    def test_login_and_logout(self):
        driver = self.driver

        # Iniciar sesión
        usuario = driver.find_element(By.ID, "username")
        usuario.send_keys("202010618")
        clave = driver.find_element(By.ID, "password")
        clave.send_keys("@Samuel14")
        clave.send_keys(Keys.ENTER)

        body= driver.find_element(By.XPATH, "/html/body")
        body.screenshot('capturas_de_pantalla/calificaciones.png')
        time.sleep(2) 
        
        buscar= driver.find_element(By.XPATH, "html/body/div[2]/nav/ul[2]/li[2]/div/div/div/div/div/a")
        time.sleep(2)
        buscar.click()

        body= driver.find_element(By.XPATH, "/html/body")
        body.screenshot('capturas_de_pantalla/calificaciones2.png')
        time.sleep(2) 
        
        
        preferencias = driver.find_element(By.XPATH, "/html/body/div[2]/nav/ul[2]/li[2]/div/div/div/div/div/div/a[5]")
        time.sleep(2)
        preferencias.click()

        body= driver.find_element(By.XPATH, "/html/body")
        body.screenshot('capturas_de_pantalla/calificaciones3.png')
        time.sleep(2) 
        

        
        
        
        
        time.sleep(10)     
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()