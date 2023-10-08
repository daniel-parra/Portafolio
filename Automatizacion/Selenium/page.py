from selenium import webdriver
from selenium.webdriver.common.by import By


class Page():

    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def __buscar_elemento_id__(self, valor):
        return self.driver.find_element(by=By.ID, value=valor)

    def __buscar_elemento_xpath__(self, valor):
        return self.driver.find_element(by=By.XPATH, value=valor)

    def __buscar_elemento_link__(self, valor):
        return self.driver.find_element(by=By.LINK_TEXT, value=valor)
    
    def __devolver_titulo__(self):
        return self.driver.title
    
    def __finalizar__(self):
        self.driver.close()

    def __esperar__(self, segundos):
        self.driver.implicitly_wait(segundos)


