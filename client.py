import socket
import threading
import random
import time

class Paciente:
    def __init__(self, nome, idade, batimentos):
        self.nome = nome
        self.idade = idade
        self.batimentos = batimentos

        return None

nickname = " "

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 8080))

def receive():
    while True:
        try:
            message = server.recv(1024).decode()
            if message == 'NICK':
                server.send(nickname.encode())
            else:
                print(message)
        except:
            print('An error has ocurred!')
            server.close()
            break
    
def write():
    maior_freq = max(pacienteExemplo[2])
    menor_freq = min(pacienteExemplo[2])
    message = f'\nNome do paciente: {nickname}\nIdade do paciente: {pacienteExemplo[1]}\nBatimento mais alto registrado na última hora: {maior_freq}\nBatimento mais baixo registrado na última hora: {menor_freq}'

    if (maior_freq > 80) or (menor_freq < 60):
        message += f'\nO paciente: {nickname} está em perigo!'
    else:
        message += f'\nO paciente: {nickname} encontra-se bem!'

    server.send(message.encode())


def pacientGenerator():
    array_de_nomes = ["Miguel", "Denerson", "Heitor", "Theo", "Gabriel", "Bernardo", "Samuel", "Mairon", "Helena", "Luana", "Laura", "Maria Alice", "Poli", "Luisa", "Maria Clara", "Maria Cecilia", "Maria Julia"]
    array_de_sobrenomes = ["Silva", "Azevedo", "Oliveira", "Tobias", "Rodrigues", "Ferreira", "Berudio",  "Pereira", "Lima", "Leal", "Ribeiro"]

    infos = []
    batimentos = []

    nome = str(array_de_nomes[random.randint(0, 16)]) + " " + str(array_de_sobrenomes[random.randint(0, 9)])
    idade = random.randint(45, 90)

    for i in range(0, 60):
        batimentos.append(random.randint(50, 90))

    infos.append(nome)
    infos.append(idade)
    infos.append(batimentos)

    return infos

pacienteExemplo = pacientGenerator()
nickname = pacienteExemplo[0]

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
ClientMultiSocket = socket.socket()