import os
import shutil
import urllib.request
import zipfile

# Verificar e instalar as dependências se necessário
try:
    import bs4
except ImportError:
    os.system('pip install beautifulsoup4')

try:
    import requests
except ImportError:
    os.system('pip install requests')

# URL base para download do servidor Bedrock
base_url = "https://minecraft.azureedge.net/bin-win/bedrock-server-"

# Diretório do seu servidor Minecraft Bedrock
server_directory = "BDS-Server/bedrock-server-1.19.83.01/"

# Diretório de backup para salvar os arquivos
backup_directory = "BDS-Server/backup-bedrock-server/"

# Arquivos e diretórios a serem preservados
preserve_files = ["whitelist.json", "server.properties", "permissions.json"]
preserve_directories = ["worlds"]

# Função para realizar o backup dos arquivos e diretórios
def fazer_backup_arquivos():
    for arquivo in preserve_files:
        caminho_arquivo = os.path.join(server_directory, arquivo)
        if os.path.isfile(caminho_arquivo):
            shutil.copy2(caminho_arquivo, backup_directory)

    for diretorio in preserve_directories:
        caminho_diretorio = os.path.join(server_directory, diretorio)
        if os.path.isdir(caminho_diretorio):
            shutil.copytree(caminho_diretorio, os.path.join(backup_directory, diretorio))

# Função para obter a versão mais recente do servidor Bedrock
def obter_versao_mais_recente():
    response = urllib.request.urlopen(base_url)

    html = response.read().decode("utf-8")
    print("Obtendo a versão mais recente do servidor Bedrock...")
    # Procurar pelo link de download da versão mais recente
    inicio_link = html.find(base_url)
    if inicio_link != -1:
        inicio_link += len(base_url)
        fim_link = html.find(".zip", inicio_link)
        
        if fim_link != -1:
            print("Versão mais recente encontrada: " + html[inicio_link:fim_link])
            return html[inicio_link:fim_link]
    print("Não foi possível encontrar a versão mais recente do servidor Bedrock")
    return None

# Função para atualizar o servidor Bedrock
def atualizar_servidor():
    # Verificar se o diretório de backup existe, caso contrário, criá-lo
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        print("O diretório de backup foi criado com sucesso!")

    # Obter a versão mais recente do servidor Bedrock
    versao_mais_recente = obter_versao_mais_recente()

    if versao_mais_recente:
        # Construir a URL de download com base na versão mais recente
        download_url = base_url + versao_mais_recente + ".zip"
        print("Baixando a versão mais recente do servidor Bedrock: " + download_url)
        # Realizar backup dos arquivos e diretórios
        fazer_backup_arquivos()

        # Baixar o arquivo zip da versão mais recente
        urllib.request.urlretrieve(download_url, "bedrock_server.zip")
        print("O servidor foi baixado com sucesso!")
        # Extrair o arquivo zip na pasta do servidor
        with zipfile.ZipFile("bedrock_server.zip", "r") as zip_ref:
            zip_ref.extractall(server_directory)
            print("O servidor foi extraído com sucesso!")
        # Remover o arquivo zip baixado
        os.remove("bedrock_server.zip")
        print("O arquivo zip foi removido com sucesso!")
        print("O servidor foi atualizado com sucesso!")
    else:
        print("Não foi possível obter a versão mais recente do servidor Bedrock.")

# Chamar a função de atualização
atualizar_servidor()
