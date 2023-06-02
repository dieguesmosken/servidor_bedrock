import tkinter as tk
from tkinter import filedialog, messagebox
import os
import nbtlib

def carregar_nbt(file_path):
    try:
        # Carrega o arquivo NBT
        nbt_data = nbtlib.load(file_path)
        return nbt_data
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar o arquivo NBT: {str(e)}')
        return None

def salvar_nbt(file_path, nbt_data):
    try:
        # Salva o arquivo NBT
        nbt_data.save(file_path)
        messagebox.showinfo('Sucesso', 'O arquivo NBT foi salvo com sucesso.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar o arquivo NBT: {str(e)}')

def abrir_arquivo():
    # Abre a caixa de diálogo para selecionar o arquivo level.dat
    file_path = filedialog.askopenfilename(filetypes=[('Arquivo NBT', '*.dat')])
    if file_path:
        nbt_data = carregar_nbt(file_path)
        if nbt_data:
            criar_interface(file_path, nbt_data)

def criar_interface(file_path, nbt_data):
    window = tk.Tk()
    window.title('Editor de level.dat')

    # Obtém as tags do arquivo NBT
    tags = nbt_data.tags

    # Cria os rótulos e campos de entrada para cada tag
    for tag_name, tag_value in tags.items():
        label = tk.Label(window, text=f'{tag_name}:')
        label.pack()
        entry = tk.Entry(window)
        entry.insert(0, str(tag_value))
        entry.pack()

        tags[tag_name] = entry

    # Função para salvar as alterações
    def salvar_alteracoes():
        try:
            # Atualiza as tags com os valores dos campos de entrada
            for tag_name, entry in tags.items():
                tag_value = entry.get()
                nbt_data[tag_name] = eval(tag_value)

            # Salva o arquivo NBT
            salvar_nbt(file_path, nbt_data)
        except Exception as e:
            messagebox.showerror('Erro', f'Ocorreu um erro ao salvar as alterações: {str(e)}')

    # Botão para salvar as alterações
    salvar_button = tk.Button(window, text='Salvar', command=salvar_alteracoes)
    salvar_button.pack()

    window.mainloop()

# Função para selecionar o arquivo level.dat
def selecionar_arquivo():
    # Abre a caixa de diálogo para selecionar a pasta do mundo
    world_path = filedialog.askdirectory()
    if world_path:
        level_dat_path = os.path.join(world_path, 'level.dat')
        if os.path.exists(level_dat_path):
            nbt_data = carregar_nbt(level_dat_path)
            if nbt_data:
                criar_interface(level_dat_path, nbt_data)
        else:
            messagebox.showerror('Erro', 'Arquivo level.dat não encontrado no mundo selecionado.')

# Cria a interface para selecionar o arquivo level.dat
root = tk.Tk()
root.title('Selecionar Mundo')
selecionar_button = tk.Button(root, text='Selecionar Mundo', command=selecionar_arquivo)
selecionar_button.pack()
root.mainloop()
