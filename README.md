[![wakatime](https://wakatime.com/badge/github/dieguesmosken/servidor_bedrock.svg?style=flat-square)](https://wakatime.com/badge/github/dieguesmosken/servidor_bedrock)
# Script de Redirecionamento de Portas para Servidor Minecraft Bedrock

Este é um script em Python que permite redirecionar portas para um servidor Minecraft Bedrock em execução no seu computador. Ele recebe as conexões dos clientes e as redireciona para o servidor Minecraft Bedrock, permitindo que jogadores externos se conectem ao seu servidor.

## Pré-requisitos

- Python 3 instalado no seu computador.
- Bibliotecas Python: `socket`.

## Como usar

1. Clone ou faça o download deste repositório.

2. Instale as bibliotecas necessárias usando o comando `pip install -r requirements.txt`.

3. Abra o arquivo `server_redirection.py` em um editor de texto.

4. Na seção de configurações, atualize as seguintes variáveis de acordo com suas necessidades:

   - `MINECRAFT_SERVER_IP`: O endereço IP do seu servidor Minecraft Bedrock.
   - `MINECRAFT_SERVER_PORT`: A porta do seu servidor Minecraft Bedrock.

5. Execute o script usando o comando `python server_redirection.py`.

6. O servidor de redirecionamento será iniciado e estará pronto para receber conexões dos jogadores.

## Configurando o Redirecionamento de Portas no Roteador

Para que o redirecionamento de portas funcione corretamente, você precisará configurar manualmente o redirecionamento de portas no seu roteador. Consulte o manual do seu roteador ou as instruções fornecidas pelo fabricante para obter detalhes sobre como realizar essa configuração.

Certifique-se de redirecionar a porta do servidor Minecraft Bedrock (por padrão, porta 19132) para o endereço IP local do computador onde o servidor está sendo executado.

## Limitações

- Este script foi fornecido como uma solução de exemplo e pode não funcionar em todos os ambientes ou configurações específicas. Certifique-se de adaptá-lo às suas necessidades e realizar testes adequados.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou recursos adicionais.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

