### criar script  em python para criar servidor minecraft local para jogar para a rede internet 
# e jogar com amigos fazendo encaminhameto de portas para o servidor local
### 

import socket
import threading
import miniupnpc

# Configurações do servidor
IP = '0.0.0.0'  # Endereço IP para escutar as conexões
PORT = 19132  # Porta para escutar as conexões

# Endereço IP e porta do servidor de Minecraft Bedrock
MINECRAFT_SERVER_IP = 'localhost'  # Substitua pelo IP do seu servidor Minecraft Bedrock
MINECRAFT_SERVER_PORT = 19132

def handle_client(client_socket):
    while True:
        # Receber dados do cliente
        data = client_socket.recv(4096)
        
        if not data:
            break
        
        try:
            # Conectar-se ao servidor de Minecraft Bedrock
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((MINECRAFT_SERVER_IP, MINECRAFT_SERVER_PORT))
            
            # Enviar dados para o servidor de Minecraft Bedrock
            server_socket.sendall(data)
            
            # Receber dados do servidor de Minecraft Bedrock
            response = server_socket.recv(4096)
            
            # Enviar dados de resposta para o cliente
            client_socket.sendall(response)
            
            # Fechar a conexão com o servidor de Minecraft Bedrock
            server_socket.close()
        
        except Exception as e:
            print('Erro na conexão com o servidor de Minecraft Bedrock:', str(e))
    
    # Fechar a conexão com o cliente
    client_socket.close()

def start_server():
    # Criar um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitir reutilização de endereços
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Vincular o socket ao endereço IP e porta
    server_socket.bind((IP, PORT))
    
    # Aguardar conexões
    server_socket.listen(5)
    
    print('Servidor de redirecionamento iniciado em {}:{}'.format(IP, PORT))
    
    while True:
        # Aceitar uma conexão do cliente
        client_socket, client_address = server_socket.accept()
        
        # Iniciar uma thread para lidar com a conexão do cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def setup_port_forwarding():
    try:
        # Criar uma instância UPnP
        upnp = miniupnpc.UPnP()
        
        # Descobrir dispositivos UPnP disponíveis
        upnp.discoverdelay = 200
        upnp.discover()
        
        # Obter o roteador padrão
        upnp.selectigd()
        
        # Adicionar regras de redirecionamento de portas
        upnp.addportmapping(MINECRAFT_SERVER_PORT, 'TCP', upnp.lanaddr, MINECRAFT_SERVER_PORT, 'Minecraft Server', '')
        
        print('Redirecionamento de porta configurado com sucesso.')
    
    except Exception as e:
        print('Erro ao configurar o redirecionamento de porta:', str(e))

# Configurar o redirecionamento de porta
setup_port_forwarding()

# Iniciar o servidor de redirecionamento
start_server()
