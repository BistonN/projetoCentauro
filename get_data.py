from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

navegador = webdriver.Chrome()
navegador.get("https://lista.mercadolivre.com.br/raquete-beach-tennis")
time.sleep(10)

urls = []
for i in range(9):
    produtos_pagina = navegador.find_elements(By.CSS_SELECTOR, '.andes-card')
    for produto in produtos_pagina:
        url = produto.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        urls.append(url)
    id = 3 if i == 0 else 4
    proximo = navegador.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/div[9]/nav/li[{id}]/a').get_attribute("href")
    navegador.get(proximo)
    time.sleep(5)

produtos = []
a = 0
for url in urls:
    a += 1
    print(a, '/', len(urls))
    navegador.get(url)
    produtos.append({
        'nome': navegador.find_element(By.CSS_SELECTOR, 'h1.ui-pdp-title').text,
        'preco': navegador.find_element(By.CSS_SELECTOR, 'span.andes-money-amount').text,
        'parcelamento': navegador.find_element(By.ID, 'pricing_subtitle').text,
        'cor': navegador.find_element(By.CSS_SELECTOR,'.andes-table__body').text,
        'marca': navegador.find_element(By.CSS_SELECTOR,'.andes-table__body').text,
        'url': url
    })
    time.sleep(4)

pd.DataFrame(produtos).to_excel('produtos.xlsx')
print(urls)
