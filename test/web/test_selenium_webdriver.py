# 1 Importar Blibliotecas
import os
from datetime import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.common import by, keys
from selenium.webdriver.common.by import By

caminho_print = 'C:/Users/SAFIRA/PycharmProjects/fts132_inicial/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


# 2Classe
class Test_selenium_webdriver():


    # Definição de Início - Executa antes do teste
    def setup_method(self, method):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/SAFIRA/PycharmProjects/fts132_inicial/drivers/chrome96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O Selenium vai esperar até 30 segundos pelos elementos
        self.driver.maximize_window()  # vai maximizar a janela do navegador

        # Cria a pasta cminho_print apenas antes do primeiro teste
        try:
            os.mkdir(caminho_print)
        except:
            print('A pasta ja existia')

    # Definição do Fim - Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    @pytest.mark.parametrize('id,termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_na_lupa(self, id, termo, curso, preco):
        # O Selenium abre a url indicada
        self.driver.get('https://iterasys.com.br')
        # Tirar print
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 1 -home.png')
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 2 -home.png')
        # O Selenium clica no botaão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em " Matriculise-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Selenium Valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
        self.driver.get('https://iterasys.com.br')
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium pressiona a teclar enter
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(keys.Keys.ENTER)
        # O Selenium clica em " Matriculise-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis' \
            # O Selenium Valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'
