import tkinter as tk
from tkinter import ttk
from configparser import ConfigParser
import os

def salvar_configuracoes(usuario, senha):
    config = ConfigParser()
    config['CONFIGURACOES'] = {'Usuario': usuario, 'Senha': senha}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def verificar_configuracoes():
    if os.path.exists('config.ini'):
        return True
    return False

def fazer_login():
    def verificar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        # Simulação de autenticação
        # Aqui você pode adicionar sua própria lógica de autenticação
        # Se o usuário/senha estiverem corretos, você pode chamar salvar_configuracoes(usuario, senha)
        # Para este exemplo, só vou verificar se o usuário é "user" e a senha é "password"

        if usuario == 'user' and senha == 'password':
            salvar_configuracoes(usuario, senha)
            root_login.destroy()
            janela_principal()
        else:
            label_aviso.config(text="Credenciais inválidas")

    root_login = tk.Tk()
    root_login.title("Login")

    frame_login = ttk.Frame(root_login, padding="20")
    frame_login.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label_usuario = ttk.Label(frame_login, text="Usuário:")
    label_usuario.grid(column=0, row=0, sticky=tk.W)

    entry_usuario = ttk.Entry(frame_login, width=30)
    entry_usuario.grid(column=1, row=0, padx=5, pady=5)

    label_senha = ttk.Label(frame_login, text="Senha:")
    label_senha.grid(column=0, row=1, sticky=tk.W)

    entry_senha = ttk.Entry(frame_login, show="*", width=30)
    entry_senha.grid(column=1, row=1, padx=5, pady=5)

    button_login = ttk.Button(frame_login, text="Login", command=verificar_login)
    button_login.grid(column=1, row=2, padx=5, pady=5)

    label_aviso = ttk.Label(frame_login, text="")
    label_aviso.grid(column=0, row=3, columnspan=2, pady=5)

    root_login.mainloop()


def janela_principal():
    root = tk.Tk()
    root.title("Janela Principal")
    root.geometry("400x300")

    # Adicione widgets ou funcionalidades à sua janela principal aqui

    root.mainloop()


def main():
    if verificar_configuracoes():
        janela_principal()
    else:
        fazer_login()


if __name__ == "__main__":
    main()
