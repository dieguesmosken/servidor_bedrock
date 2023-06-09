import re
import requests

url = "https://www.minecraft.net/en-us/download/server/bedrock"

# Fazer a solicitação HTTP para a página
response = requests.get(url)
html = response.text

# Extrair o link de download da versão mais recente
version_pattern = r"https:\/\/minecraft\.azureedge\.net\/bin-win\/bedrock-server-\d+\.\d+\.\d+\.\d+\.zip"
match = re.search(version_pattern, html)
if match:
    download_link = match.group()
    print("Link de download da versão mais recente:", download_link)
else:
    print("Link de download não encontrado.")
