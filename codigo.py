# Passo 0: Configurar o ambiente

import pyautogui
import time
import pygetwindow as gw
pyautogui.PAUSE = 0.5

# Passo 1: Abrir o sistema da empresa
# Apertar a tecla win e digitar o nome do navegador e dar enter.
# Função para simplificar o código
def press_and_write(key, text, reverse_order=False):
    if reverse_order:
        # Se reverse_order for True, primeiro pressiona a tecla e depois escreve o texto
        pyautogui.press(key)
        pyautogui.write(text)
    else:
        # Se reverse_order for False, primeiro escreve  e o texto e depois pressiona a tecla
        pyautogui.write(text)
        pyautogui.press(key)
        
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(0.5) # O tempo depende da sua máquina, você escolhe conforme for o desempenho.

maximizar_janela = gw.getWindowsWithTitle('Chrome')[0]
maximizar_janela.maximize()

time.sleep(0.8)

# Selecionar o usuário do navegador
pyautogui.click(x=145, y=958)
time.sleep(0.8)
maximizar_janela = gw.getWindowsWithTitle('Chrome')[0]
maximizar_janela.maximize()
# Digitar o endereço do sistema e dar enter
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
press_and_write('enter', link)

# Pedir para o sistema esperar um tempo
time.sleep(3)

# Passo 2: Fazer login
# Clicar na caixa de diálogo para digitar o usuário
pyautogui.click(x=735, y=467)
time.sleep(0.2)
pyautogui.write('mariabonitinha@gmail.com') # Digitar o usuário
pyautogui.press('tab') # Passar para o campo de senha
pyautogui.write('minha senha aqui')
pyautogui.press('tab') # Passar para o login
pyautogui.press('enter') # Fazer login


# Passo 3: Importar base de dados
import pandas as mona

tabela = mona.read_csv('produtos.csv')
print(tabela)

time.sleep(1.5)

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    
    pyautogui.click(x=705, y=322) # clicar no primeiro campo

    # código
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preço_unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # OBS
    obs = str(tabela.loc[linha, 'obs']) # transformando em string já na variável
    
    # Verificar se 'obs' possui um valor, se possuir, vai preencher, se não, apenas continua.
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') # Apertar o botão de 'enviar'
    pyautogui.scroll(10000) # Scroll até o topo


# Passo 5: Repetir o passo 4 até acabar todos os produtos

