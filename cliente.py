"""
Lado do cliente: Usa sockets para mandar data para o servidor, e imprime
a resposta do servidor para cada linha na mensagem. Podemos colocar o 
host como sendo localhost para indicar que o servidor está na mesma máquina.
Para rodar através da internet é preciso colocar o servidor em outra
máquina e passar para o nome do host o endereço de IP ou o nome do
domínio.
"""

import random
from socket import *
from base64 import *
import time

class Paciente:
    def __init__(self, nome, idade, batimentos):
        self.nome = nome
        self.idade = idade
        self.batimentos = batimentos

        return None


def geradorPaciente():
    array_de_nomes = ["Miguel", "Denerson", "Heitor", "Theo", "Gabriel", "Bernardo", "Samuel", "Mairon", "Helena", "Luana", "Laura", "Maria_Alice", "Poli", "Luisa", "Maria_Clara", "Maria_Cecilia", "Maria_Julia"]
    array_de_sobrenomes = ["Silva", "Azevedo", "Oliveira", "Tobias", "Rodrigues", "Ferreira", "Berudio",  "Pereira", "Lima", "Leal", "Ribeiro"]


    batimentos = []

    nome = array_de_nomes[random.randint(0, 16)]
    sobrenome = array_de_sobrenomes[random.randint(0, 9)]
    idade = random.randint(45, 90)

    open(f'infos_{nome}-{sobrenome}.txt', "x")
    document = open(f'infos_{nome}-{sobrenome}.txt', "w")
    document.write(nome + " " + sobrenome)
    document.write("\n" + f'{idade}')

    for i in range(0, 50):
        batimentos.append(random.randint(30, 120))

    document.write("\n" + f'{batimentos}')

    paciente = Paciente(nome + " " + sobrenome, idade, batimentos)
    return paciente

# Configurações de conexão do servidor
# O nome do servidor pode ser o endereço de
# IP ou o domínio (ola.python.net)
serverHost = 'localhost'
serverPort = 50007

pacienteExemplo = geradorPaciente()

# Menssagem a ser mandada condificada em bytes
mensagem = 'Paciente '.encode('utf-8') + pacienteExemplo.nome.encode('utf-8') + ' conectado!'.encode('utf-8')



# Criamos o socket e o conectamos ao servidor
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

# Mandamos a menssagem linha por linha
sockobj.send(mensagem)

for i in pacienteExemplo.batimentos:
    if i < 60 or i > 80:
        sockobj.send(f'O paciente {pacienteExemplo.nome} está em perigo! batimento neste minuto passado: {i} bpm'.encode('utf-8'))
    time.sleep(3)
# Depois de mandar uma linha esperamos uma resposta
# do servidor
data = sockobj.recv(1024)
print('Cliente recebeu:', data.decode('utf-8'))

# Fechamos a conexão
sockobj.close()