import socket

class MinecraftServer:
    def __init__(self, host='localhost', post=8080):
        self.host = host
        self.port = port 

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket