import os
import shutil
import urllib.request
import zipfile
import re
from bs4 import BeautifulSoup

# URL do site oficial do Minecraft para download do servidor Bedrock
url = "https://www.minecraft.net/en-us/download/server/bedrock"

# Diretório do seu servidor Minecraft Bedrock
server_directory = "content/servidor-atual"

# Diretório de backup para salvar os arquivos
backup_directory = "content/servidor-backup"

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
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    link_download = soup.find("a", href=re.compile(r"bedrock-server-\d+\.\d+\.\d+\.\d+\.zip"))["href"]

    # Extrair a versão do link de download
    padrao = r"bedrock-server-(\d+\.\d+\.\d+\.\d+)\.zip"
    resultado = re.search(padrao, link_download)

    if resultado:
        return resultado.group(1)

    return None

# Função para atualizar o servidor Bedrock
def atualizar_servidor():
    # Verificar se o diretório de backup existe, caso contrário, criá-lo
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Obter a versão mais recente do servidor Bedrock
    versao_mais_recente = obter_versao_mais_recente()

    if versao_mais_recente:
        # Construir a URL de download com base na versão mais recente
        download_url = "https://minecraft.azureedge.net/bin-win/bedrock-server-" + versao_mais_recente + ".zip"

        # Realizar backup dos arquivos e diretórios
        fazer_backup_arquivos()

        # Baixar o arquivo zip da versão mais recente
        urllib.request.urlretrieve(download_url, "bedrock_server.zip")

        # Extrair o arquivo zip na pasta do servidor
        with zipfile.ZipFile("bedrock_server.zip", "r") as zip_ref:
            zip_ref.extractall(server_directory)

        # Remover o arquivo zip baixado
        os.remove("bedrock_server.zip")

        print("O servidor foi atualizado com sucesso!")
    else:
        print("Não foi possível obter a versão mais recente do servidor Bedrock.")

