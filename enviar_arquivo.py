import socket
import os
import tkinter as tk
from tkinter import filedialog

def enviar_arquivos(arquivo):
    HOST = '192.168.1.102'  # Endereço IP do servidor
    PORT = 55555  # Porta usada pelo servidor

    largura_janela = root.winfo_width()
    altura_janela = root.winfo_height()

    mensagem_label.config(text="Aguardando conexão...")
    mensagem_label.pack(pady=100, padx=200)
    mensagem_label.place(x=(largura_janela-mensagem_label.winfo_reqwidth()) /2,
                         y=(altura_janela-mensagem_label.winfo_reqheight()) /2)
    root.update()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        mensagem_label.config(text="Conexão realizada com: " + str(HOST) + " pela porta " + str(PORT))
        mensagem_label.update()
        
        with open(arquivo, 'rb') as file:
            print(f"Enviando {arquivo}...")
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)
        
        mensagem_label.config(text=mensagem_label.cget("text") + "\nArquivo enviado com sucesso!")
        mensagem_label.update()
        mensagem_label.place(x=(largura_janela-mensagem_label.winfo_reqwidth())/2,
                             y=(altura_janela-mensagem_label.winfo_reqheight())/2)

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename()
    if arquivo:
        enviar_arquivos(arquivo)

def janela():
    global root
    root = tk.Tk()
    root.title("Enviar Arquivos - Solda por Resistência")

    # Tamanho da janela
    root.geometry("600x400")

    botao_selecionar = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
    botao_selecionar.pack(pady=100, padx=200)

    global mensagem_label
    mensagem_label = tk.Label(root, text="", justify="left")
    mensagem_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    janela()