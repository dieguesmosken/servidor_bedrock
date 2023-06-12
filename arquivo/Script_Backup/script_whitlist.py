import socket
import threading
print("Script para whitelist de jogadores no servidor Minecraft Bedrock Edition.")
# Lista de jogadores permitidos (whitelist)
whitelist = ['player1', 'player2', 'player3']

# Classe para manipular conexões de clientes
class ClientThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            print("Recebido do cliente:", data)
            response = "Recebido: " + data
            self.client_socket.send(response.encode())
        self.client_socket.close()

# Configurações do servidor
HOST = 'localhost'
PORT = 8080

# Inicialização do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Servidor Minecraft em execução.")

while True:
    client_socket, address = server_socket.accept()
    print("Cliente conectado:", address)
    player_name = client_socket.recv(1024).decode()

    # Verifica se o jogador está na whitelist
    if player_name in whitelist:
        print("O jogador", player_name, "foi permitido.")
        client_socket.send("Você foi autorizado a se conectar.".encode())

        client_thread = ClientThread(client_socket)
        client_thread.start()
    else:
        print("O jogador", player_name, "não está na whitelist.")
        client_socket.send("Você não tem permissão para se conectar.".encode())
        client_socket.close()
