from lib2to3.pgen2 import driver
from selenium import webdriver

PATH = "C:\Arquivos de Programa (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://facebook.com")
driver.quit()
