import os
import socket
import tkinter as tk
from tkinter import filedialog

def receber_arquivos():
    HOST = '192.168.1.102'  # Pode ser o endereço IP do computador ou '0.0.0.0' para aceitar conexões de qualquer endereço
    PORT = 55555  # Porta para aceitar conexões

    # Especifique o caminho completo para o diretório onde deseja salvar o arquivo recebido
    SAVE_PATH = 'C:/Users/pedro/Desktop/ArquivosRecebidos'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # Aceitar apenas uma conexão

        largura_janela = root.winfo_width()
        altura_janela = root.winfo_height()

        mensagem_label.config(text="Aguardando conexão...")
        mensagem_label.pack(pady=100, padx=200)
        mensagem_label.place(x=(largura_janela - mensagem_label.winfo_reqwidth()) / 2,
                             y=(altura_janela - mensagem_label.winfo_reqheight()) / 2)
        root.update()

        connection, address = server_socket.accept()

        with connection:
            mensagem_label.config(text="Conexão aceita de: " + str(HOST) + " pela porta " + str(PORT))
            mensagem_label.update()

            # Modifique o caminho para incluir o diretório de salvamento
            save_file_path = SAVE_PATH + '/arquivo_recebido'

            with open(save_file_path, 'wb') as file:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    file.write(data)
            mensagem_label.config(text=mensagem_label.cget("text") + "\nArquivo recebido com sucesso!")
            mensagem_label.update()

            # Centralizar as últimas duas mensagens no meio da janela
            mensagem_label.place(x=(largura_janela - mensagem_label.winfo_reqwidth()) / 2,
                                 y=(altura_janela - mensagem_label.winfo_reqheight()) / 2)

            # Adicionando o botão para abrir o local do arquivo
            btn_abrir_arquivo = tk.Button(root, text="Abrir local do arquivo", command=abrir_local_arquivo)
            btn_abrir_arquivo.pack(pady=100)

def ocultar_botao_e_mostrar_mensagem():
    botao_conectar.pack_forget()
    receber_arquivos()

def abrir_local_arquivo():
    # Abre o diretório onde o arquivo foi salvo
    os.startfile('C:/Users/pedro/Desktop/ArquivosRecebidos')

def janela():
    global root
    root = tk.Tk()
    root.title("Receber Arquivos - Solda por Resistência")

    # Define o tamanho da janela
    root.geometry("600x400")

    global botao_conectar
    botao_conectar = tk.Button(root, text="Conectar", command=ocultar_botao_e_mostrar_mensagem)
    botao_conectar.pack(pady=100, padx=200)

    global mensagem_label
    mensagem_label = tk.Label(root, text="", justify="left")
    mensagem_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    janela()