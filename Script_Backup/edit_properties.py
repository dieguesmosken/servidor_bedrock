import tkinter as tk
from tkinter import messagebox

def carregar_configuracoes():
    try:
        with open('BDS-Server/server.properties', 'r') as file:
            configuracoes = {}
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=')
                    configuracoes[key.strip()] = value.strip()

        return configuracoes
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar as configurações: {str(e)}')
        return {}

def salvar_configuracoes(configuracoes):
    try:
        with open('BDS-Server/server.properties', 'r') as file:
            linhas_originais = file.readlines()

        with open('BDS-Server/server.properties', 'w') as file:
            for linha in linhas_originais:
                if '=' in linha:
                    key = linha.split('=')[0].strip()
                    if key in configuracoes:
                        value = configuracoes[key]
                        linha = f'{key}={value}\n'
                file.write(linha)

        messagebox.showinfo('Sucesso', 'As configurações foram salvas com sucesso.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar as configurações: {str(e)}')

def criar_interface():
    window = tk.Tk()
    window.title('Editor de server.properties')

    configuracoes = carregar_configuracoes()
    num_propriedades = len(configuracoes)

    largura_janela = 700
    altura_janela = min(num_propriedades * 30 + 100, 500)
    window.geometry(f'{largura_janela}x{altura_janela}')

    entries = {}
    coluna_atual = 0

    def atualizar_valor(event, key):
        configuracoes[key] = entries[key].get()

    def salvar_configuracoes_e_fechar():
        salvar_configuracoes(configuracoes)
        window.destroy()

    barra_botoes = tk.Frame(window)
    barra_botoes.pack(side='top')

    salvar_button = tk.Button(barra_botoes, text='Salvar', command=salvar_configuracoes_e_fechar)
    salvar_button.pack(side='left')

    sair_button = tk.Button(barra_botoes, text='Sair', command=window.quit)
    sair_button.pack(side='left')

    frame_propriedades = tk.Frame(window)
    frame_propriedades.pack(side='top')

    for i, (key, value) in enumerate(configuracoes.items()):
        propriedade_frame = tk.Frame(frame_propriedades)
        propriedade_frame.pack(side='top')

        label = tk.Label(propriedade_frame, text=key)
        label.pack(side='left', padx=5, pady=5)

        entry = tk.Entry(propriedade_frame)
        entry.insert(0, value)
        entry.pack(side='left', padx=5, pady=5)

        entry.bind('<Return>', lambda event, key=key: atualizar_valor(event, key))
        entries[key] = entry

    window.mainloop()

criar_interface()
