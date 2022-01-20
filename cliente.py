import socket
import random

# class pessoa:
#     def __init__(self, nome, idade, batimentos):
#         self.nome = nome
#         self.idade = idade
#         self.batimentos = batimentos

#         return None


# def geradorPacientes():
#     array_de_nomes = ["Miguel", "Denerson", "Heitor", "Theo", "Gabriel", "Bernardo", "Samuel", "Mairon", "Helena", "Luana", "Laura", "Maria Alice", "Poli", "Luisa", "Maria Clara", "Maria Cecilia", "Maria Julia"]
#     array_de_sobrenomes = ["Silva", "Azevedo", "Oliveira", "Tobias", "Rodrigues", "Ferreira", "Berudio",  "Pereira", "Lima", "Leal", "Ribeiro"]

#     for i in range(5):
#         vetor = []
#         open(f'infos_pessoa{i}.txt', "x")
#         document = open(f'infos_pessoa{i}.txt', "w")
#         document.write(array_de_nomes[random.randint(0, 16)] + " " + array_de_sobrenomes[random.randint(0, 9)])
#         document.write("\n" + f'{random.randint(45, 90)}')

#         for i in range(0, 50):
#             vetor.append(random.randint(30, 120))

#         document.write("\n" + f'{vetor}')

#         return None
"""
Lado do cliente: Usa sockets para mandar data para o servidor, e imprime
a resposta do servidor para cada linha na mensagem. Podemos colocar o 
host como sendo localhost para indicar que o servidor está na mesma máquina.
Para rodar através da internet é preciso colocar o servidor em outra
máquina e passar para o nome do host o endereço de IP ou o nome do
domínio.
"""

from socket import *

# Configurações de conexão do servidor
# O nome do servidor pode ser o endereço de
# IP ou o domínio (ola.python.net)
serverHost = 'localhost'
serverPort = 50007

# Menssagem a ser mandada condificada em bytes
menssagem = [b'Ola mundo da internet!']

# Criamos o socket e o conectamos ao servidor
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

# Mandamos a menssagem linha por linha
for linha in menssagem:
    sockobj.send(linha)

    # Depois de mandar uma linha esperamos uma resposta
    # do servidor
    data = sockobj.recv(1024)
    print('Cliente recebeu:', data)

# Fechamos a conexão
sockobj.close()