# Passo 1 entrar no google e no site
import pyautogui 
import time

pyautogui.PAUSE = 1.0
pyautogui.press ('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep (2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
# Passo 2 fazer login

pyautogui.click (pyautogui.position(x=887, y=379))
time.sleep(1)
pyautogui.write ('giicarniato')
pyautogui.press('tab')
pyautogui.write ('MinhaSenha')
pyautogui.press('tab')
pyautogui.press('enter')


# Passo 3 cadastro das informações

import pandas

tabela = pandas.read_csv (r'C:\Users\giica\Projetos\Python projects\IA- automatizacao hashtag\produtos.csv')

# Repetir até acabar
for linha in tabela.index:
    pyautogui.click (pyautogui.position(x=901, y=261)) # para apertar no primeiro item

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


        
    