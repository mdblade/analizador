from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
from bs4 import BeautifulSoup


#visualizar o processos ou nao ..
options = Options()
options.headless = False


navegador = webdriver.Chrome(options=options)
link = "https://tipminer.com/login"


navegador.get(url=link)
sleep(1)


inputUsers = navegador.find_element(by=By.NAME, value="email")
inputUsers.send_keys("macieldantas23@hotmail.com")
#sleep(1)


inputPassword = navegador.find_element(by=By.ID, value="password")
inputPassword.send_keys("Dwj135418@")
#sleep(1)

buttonRemember = navegador.find_element(by=By.ID, value="remember")
buttonRemember.click()
#sleep(2)

buttonLoguin = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div/div[2]/div/form/div/div[4]/input")
buttonLoguin.click()
#sleep(2)

buttonAcessar = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div/div/a")
buttonAcessar.click()
sleep(2)

inputQuantidade = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/form/div[1]/div[1]/input")
inputQuantidade.clear()
sleep(2)

inputQuantidade = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/form/div[1]/div[1]/input")
inputQuantidade.send_keys(4000)
sleep(2)

buttonColunas = navegador.find_element(by=By.ID, value="fixed")
buttonColunas.click()
sleep(2)

buttonFiltrar = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/form/div[3]/button")
buttonFiltrar.click()
sleep(2)


#analisar estrategias
buttonUm = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/div[2]/div/div")
buttonUm.click()
sleep(1)

buttonUm = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/div[2]/div/div")
buttonUm.click()
sleep(1)

buttonTestar = navegador.find_element(by=By.XPATH, value="/html/body/main/div/div/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/button[5]")
buttonTestar.click()
sleep(3)









