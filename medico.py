from base64 import *
from socket import *

"""
Lado do cliente: Usa sockets para mandar data para o servidor, e imprime
a resposta do servidor para cada linha na mensagem. Podemos colocar o 
host como sendo localhost para indicar que o servidor está na mesma máquina.
Para rodar através da internet é preciso colocar o servidor em outra
máquina e passar para o nome do host o endereço de IP ou o nome do
domínio.
"""

serverHost = 'localhost'
serverPort = 50007

# Menssagem a ser mandada condificada em bytes
mensagem = 'Médico conectado!'.encode('utf-8')

# Criamos o socket e o conectamos ao servidor
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

# Mandamos a menssagem linha por linha
sockobj.send(mensagem)

# Depois de mandar uma linha esperamos uma resposta
# do servidor

while True:
    while True:
        data = sockobj.recv(1024)

        if  not data:
            break

        print('Médico recebeu:', data.decode('utf-8'))
    # Fechamos a conexão
    sockobj.close()
