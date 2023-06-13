### criar script em python para criar servidor minecraft local para jogar para a rede internet 
# e jogar com amigos fazendo encaminhameto de portas para o servidor local

from game.server import MinecraftServer

def main():
    # Inicializar e Executar o servidor
    server = MinecraftServer()
    server.start()

if __name__ == "__main__":
    main()