# Passo 1 entrar no google e no site
import pyautogui 
import time

pyautogui.PAUSE = 0.5
pyautogui.press ('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep (2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Passo 2 fazer login
   # Usar print do botão de login
email = pyautogui.locateOnScreen(r'C:\Users\giica\Projetos\Python projects\IA- automatizacao\botaoEmail.png',confidence=0.6)
if email:
    pyautogui.click (email)
    time.sleep(1.5)
    pyautogui.write ('giicarniato')
    pyautogui.press('tab')
    pyautogui.write ('MinhaSenha')
    pyautogui.press('tab')
    pyautogui.press('enter')
else:
    print('Botão de login não encontrado!')

# Passo 3 cadastro das informações

import pandas

tabela = pandas.read_csv (r'C:\Users\giica\Projetos\Python projects\IA- automatizacao\produtos.csv')

# Repetir até acabar
for linha in tabela.index:
    primeiro_item = pyautogui.locateOnScreen(r'C:\Users\giica\Projetos\Python projects\IA- automatizacao\primeiro_item.png', confidence=0.6)
    pyautogui.click (primeiro_item) 

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha,'obs']

    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha,'obs']))

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)
    time.sleep(1.2)


        
    