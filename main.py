### criar script  em python para criar servidor minecraft local para jogar para a rede internet 
# e jogar com amigos fazendo encaminhameto de portas para o servidor local
### 
# bliblioteca de redirecionamento de portas

from miniupnpc import UPnP

def setup_port_forwarding():
    try:
        # Criar uma instância UPnP
        upnp = UPnP()

        # Descobrir dispositivos UPnP disponíveis
        upnp.discoverdelay = 200
        upnp.discover()

        # Obter o roteador padrão
        upnp.selectigd()

        # Adicionar regras de redirecionamento de portas
        external_port = 19132
        internal_port = 19132
        upnp.addportmapping(external_port, 'UDP', upnp.lanaddr, internal_port, 'Minecraft Server', '')

        print('Port forwarding configured successfully! External Port:', external_port, 'Internal Port:', internal_port)

    except Exception as e:
        print('Error occurred while setting up port forwarding:', str(e))

# Configurar o redirecionamento de porta
setup_port_forwarding()
