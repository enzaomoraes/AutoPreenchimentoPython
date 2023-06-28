from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from tkinter import * 
from tkinter import ttk, Tk

def autopreenchimento(dicionario, i):       

        # Defina o caminho para o ChromeDriver
    caminho_chromedriver = "your designated path to the chrome driver"

    # Configura o serviço do ChromeDriver
    servico = Service(caminho_chromedriver)

    # Configura as opções do ChromeDriver 
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--start-maximized")  # Abre o navegador maximizado

    # Inicializa o driver do Chrome
    driver = webdriver.Chrome(service=servico, options=opcoes)

    # Abre o formulário do Google
    driver.get("your choice of forms")

    # Preenche o campo de nome
    campo_nome = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 'your desired XPATH')))
    campo_nome.send_keys(dicionario[i][0])

    # Preenche o campo de DATA DE NASCIMENTO
    campo_data_nascimento = driver.find_element(By.XPATH, 'your desired XPATH')
    campo_data_nascimento.send_keys(dicionario[i][1])
                         
    # Preenche o campo de IDADE
    campo_idade = driver.find_element(By.XPATH, 'your desired XPATH')
    campo_idade.send_keys(dicionario[i][2])

    # Clica no botão de envio
    botao_enviar = driver.find_element(By.XPATH, "//span[contains(text(), 'Enviar')]")
    botao_enviar.click()

    time.sleep(5)

dicionario={}

def salvar_json(arquivo, dados):
    with open(arquivo, 'w') as file:
        json.dump(dados, file)

def carregar_json(arquivo):
    with open(arquivo, 'r') as file:
        dicionario = json.load(file)
    return dicionario

dicionario=carregar_json("dados.json")

def encontrar_ultima_chave(dicionario):
    chaves = list(dicionario.keys())
    ultima_chave = chaves[-1]
    return ultima_chave

def valores():
    identificacao = str(int(encontrar_ultima_chave(dicionario)) + 1)
    nome=entry_nome.get()
    idade=entry_idade.get()
    data_nasc=entry_data_nasc.get()
    dicionario[identificacao]=[nome,idade,data_nasc]
    salvar_json("dados.json",dicionario)
    entry_nome.delete(0,END)
    entry_idade.delete(0,END)
    entry_data_nasc.delete(0,END)
    autopreenchimento(dicionario, identificacao)

root = Tk()
root.title("AutoPreenchimento Teste")
root.geometry("200x200")

main_frame = ttk.Frame(root, padding=20)
main_frame.grid()

ttk.Label(main_frame, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = ttk.Entry(main_frame)
entry_nome.grid(row=1, column=0)

ttk.Label(main_frame, text="Idade:").grid(row=2, column=0, sticky="w")
entry_idade = ttk.Entry(main_frame)
entry_idade.grid(row=3, column=0)

ttk.Label(main_frame, text="Data de Nascimento:").grid(row=4, column=0, sticky="w")
entry_data_nasc = ttk.Entry(main_frame)
entry_data_nasc.grid(row=5, column=0)

ttk.Button(main_frame, text="Adicionar no JSON", command=valores).grid(row=8, column=0)

root.mainloop()
