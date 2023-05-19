#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Automação web com python 

# Selenium
# Baixar o webdriver
get_ipython().system('pip install selenium')


# In[ ]:


# firefox -> geckodriver
# chrome -> chromedriver

# Abrir o navegador
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")


# In[8]:


# Importar a base de dados
import pandas as pd

tabela = pd.read_excel("commodities.xlsx")

display(tabela)


# In[9]:


#OBS> 
# .click() -> clicar
# .send_keys("texto") -> escrever
# .get_attribute() -> pegar um valor


# Ações
# Pesquisar o valor do produto
# Atualizar o valor na base de dados
# Decidir quais produtos comprar
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace(
    "ç", "c").replace("ú", "u").replace("é", "e")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    
    
print("Acabou")
display(tabela)


# In[ ]:


# Preenchimento da coluna de comprar
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)

# Exportação da base para o excel
tabela.to_excel("commodities_atualizado.xlsx", index=False)


# In[ ]:


navegador.quit()

