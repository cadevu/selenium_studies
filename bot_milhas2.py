from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
precos={}
browser = Firefox()
def formatar_valor(price,qtd):
    """Formata o preço do formato BRL para um fortmato utilizável no código e retorna o valor do milheiro ( preço total / quantidade de milhas cotadas
    """
    price = price[3:]
    price = price.replace('.', '')
    price = price.replace(',', '.')
    price = float(price)
    qtd_total = int(qtd)
    valor_do_milheiro = (price / qtd_total)
    preco_format= (f'{valor_do_milheiro:.2f}')
    return (f'{valor_do_milheiro:.2f}')
def login_site():
    browser.get ('https://cliente.hotmilhas.com.br/auth/sign-in')
    sleep(5)
    # login
    browser.find_element(By.NAME, 'email').send_keys('automationcadevu@gmail.com')
    browser.find_element(By.NAME, 'password').send_keys('********')
    sleep(5)
    browser.find_element(By.CLASS_NAME, 'laVb1m').click()  #botao entrar
def fazer_cotacao(cia,qtd):
    sleep(6)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/span').click()  # botao cotacoes
    sleep(3)
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[2]/div/div/div/button/div[1]').click()  # clica nas cotacoes
    cia_aerea=browser.find_element(By.XPATH,'//*[@id="react-select-4-input"]')
    cia_aerea.send_keys(cia)
    if cia not in precos:
        precos[cia] = {}
    cia_aerea.send_keys(Keys.TAB)
    sleep(3)
    quantidade_de_milhas =browser.find_element(By.XPATH,'//*[@id="react-select-13-input"]')
    quantidade_de_milhas.send_keys(qtd)
    quantidade_de_milhas.send_keys(Keys.TAB)
    sleep(2)
    preco=browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[2]/div/div/div/div[2]/main/div/div[2]/ul/li[4]/div')
    precos[cia][qtd]=formatar_valor(preco.text,qtd) #armazena o preço da qtd de milhas em dicionários
    sleep(2)
    browser.refresh()
login_site()
fazer_cotacao('SMILES','100')
sleep(1)
fazer_cotacao('SMILES','49')
sleep(1)
fazer_cotacao('SMILES','29')
sleep(1)
fazer_cotacao('TUDO AZUL','80')
sleep(1)
fazer_cotacao('TUDO AZUL','100')
sleep(1)
fazer_cotacao('LATAM PASS','49')
sleep(1)
fazer_cotacao('LATAM PASS','99')
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M') # fomata a data e o horário
print(f'Data e horário da cotação: {data_e_hora_em_texto}')
for cia in precos:
    print(cia)
    for qtd in precos[cia]:
        print(f'Até {qtd}K: {precos[cia][qtd]}')
