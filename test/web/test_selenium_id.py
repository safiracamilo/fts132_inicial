# 1 - Importar Bibliotecas / Pacotes

import pytest     # Framework de Teste de Unidade / Engine / Motor
import time       # Controle do Tempo
import json       # Ler Escrever no formado Json
from selenium import webdriver                   #Biliotecas de Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#2 Classe e Definições
class TestConsultaMatins2022():
    def setup_method(self, method):
        #instanciar o objeto do Selenium WebDrive como Chrome
        self.driver = webdriver.Chrome('C:/Users/SAFIRA/PycharmProjects/fts132_inicial/drivers/chrome96/chromedriver.exe')
        self.driver.implicitly_wait(30) # o robo irá esperar por até 30 segundos pelos elementos
        self.driver.maximize_window()   # maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultaMatins2022(self):
        self.driver.get("https://iterasys.com.br/")
        self.driver.set_window_size(1132, 690)
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()
        # time.sleep(3) #pause forçada / "alfinete"/ sempre deve remover antes de salvar no repositório
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"

