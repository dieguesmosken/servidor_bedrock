import tkinter as tk
from tkinter import messagebox

def carregar_configuracoes():
    try:
        # Abre o arquivo server.properties em modo de leitura
        with open('server.properties', 'r') as file:
            configuracoes = {}
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=')
                    configuracoes[key.strip()] = value.strip()

        return configuracoes
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar as configurações: {str(e)}')
        return {}

def salvar_configuracoes():
    try:
        configuracoes = {
            'motd': motd_entry.get(),
            'gamemode': gamemode_entry.get(),
            'max-players': max_players_entry.get(),
            'spawn-protection': spawn_protection_entry.get(),
            # Adicione outras configurações aqui
        }

        with open('server.properties', 'w') as file:
            for key, value in configuracoes.items():
                file.write(f'{key}={value}\n')

        messagebox.showinfo('Sucesso', 'As configurações foram salvas com sucesso.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar as configurações: {str(e)}')

def criar_interface():
    window = tk.Tk()
    window.title('Editor de server.properties')

    configuracoes = carregar_configuracoes()

    # Cria os rótulos e campos de entrada
    for key, value in configuracoes.items():
        label = tk.Label(window, text=f'{key}:')
        label.pack()
        entry = tk.Entry(window)
        entry.insert(0, value)
        entry.pack()

        configuracoes[key] = entry

    # Botão para salvar as configurações
    salvar_button = tk.Button(window, text='Salvar', command=salvar_configuracoes)
    salvar_button.pack()

    window.mainloop()

criar_interface()
