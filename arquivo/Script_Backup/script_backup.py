import shutil
import os
import datetime
import schedule
import time
import hashlib

# Caminho para a pasta do servidor Minecraft
minecraft_path = 'BDS-Server/bedrock-server-1.20.0.01/'

# Caminho para a pasta de backup
backup_path = 'BDS-Server/backups-bedrock-server'

def calcular_hash(file_path):
    # Cria um objeto hash MD5
    md5_hash = hashlib.md5()

    # Lê o arquivo em blocos para processar grandes arquivos eficientemente
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)

    # Retorna o hash MD5 em formato hexadecimal
    return md5_hash.hexdigest()

def fazer_backup():
    # Gera um timestamp para o nome do arquivo de backup
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Cria o nome do arquivo de backup
    backup_file = f'mundo_backup_{timestamp}.zip'

    # Caminho completo para o arquivo de backup
    backup_file_path = os.path.join(backup_path, backup_file)

    try:
        # Cria um arquivo zip do mundo do servidor Minecraft
        shutil.make_archive(backup_file_path, 'zip', minecraft_path)

        print(f'Backup do mundo do servidor Minecraft criado com sucesso: {backup_file_path}')

        # Calcula o hash do arquivo de backup
        hash_file = calcular_hash(backup_file_path)

        # Salva o hash em um arquivo
        hash_file_path = f'{backup_file_path}.md5'
        with open(hash_file_path, 'w') as file:
            file.write(hash_file)

        print(f'Arquivo de hash criado: {hash_file_path}')
    except Exception as e:
        print(f'Ocorreu um erro ao criar o backup: {str(e)}')

def verificar_backup():
    for backup_file in os.listdir(backup_path):
        if backup_file.endswith('.zip'):
            # Caminho completo para o arquivo de backup
            backup_file_path = os.path.join(backup_path, backup_file)

            # Caminho completo para o arquivo de hash
            hash_file_path = f'{backup_file_path}.md5'

            if not os.path.isfile(hash_file_path):
                print(f'Arquivo de hash não encontrado para o backup: {backup_file}')
                continue

            # Calcula o hash atual do arquivo de backup
            hash_atual = calcular_hash(backup_file_path)

            # Lê o hash salvo do arquivo de hash
            with open(hash_file_path, 'r') as file:
                hash_salvo = file.read()

            if hash_atual == hash_salvo:
                print(f'Backup verificado com sucesso: {backup_file}')
            else:
                print(f'Backup corrompido: {backup_file}')

def escolher_tempo():
    while True:
        print("Escolha o tempo entre os backups:")
        print("1. 30 minutos")
        print("2. 1 hora")
        print("3. 2 horas")
        print("4. 4 horas")
        print("5. 8 horas")
        print("6. Verificar backups")
        print("7. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            schedule.every(30).minutes.do(fazer_backup)
            break
        elif opcao == "2":
            schedule.every(1).hours.do(fazer_backup)
            break
        elif opcao == "3":
            schedule.every(2).hours.do(fazer_backup)
            break
        elif opcao == "4":
            schedule.every(4).hours.do(fazer_backup)
            break
        elif opcao == "5":
            schedule.every(8).hours.do(fazer_backup)
            break
        elif opcao == "6":
            verificar_backup()
        elif opcao == "7":
            print("Saindo do programa...")
            return
        else:
            print("Opção inválida. Digite um número válido.")

    while True:
        schedule.run_pending()
        time.sleep(1)

escolher_tempo()

