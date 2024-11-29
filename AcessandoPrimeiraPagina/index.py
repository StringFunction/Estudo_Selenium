#IMPORTANDO MODELOS 
from selenium import webdriver #FUNCAO : ABRIR NEVAGADOR
from selenium.webdriver.common.by import By #FUNCÃO : PROCURA ELEMENTO 
import pyautogui as p

#inicializar uma instância do WebDriver para o navegador Google Chrome
driver = webdriver.Chrome()
#abrir navegador com Url desejada e vai esperar carregar pagina por completo com ajuda
#do evento onload
driver.get("https://www.google.com.br/?hl=pt-BR")

#Verifico se titulo do site em palavra google
assert "Google" in driver.title
print(f"NOME DO TITULO DA PAGINA {driver.title}")