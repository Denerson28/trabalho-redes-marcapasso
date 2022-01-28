import socket
import threading
import random

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

def diagnostic():
    maior_freq = max(paciente_exemplo[2])
    menor_freq = min(paciente_exemplo[2])

    message = f'\nNome do paciente: {nickname}\nIdade do paciente: {paciente_exemplo[1]}\nBatimento mais alto registrado na última hora: {maior_freq}\nBatimento mais baixo registrado na última hora: {menor_freq}'

    if (maior_freq > 80) or (menor_freq < 60):
        message += f'\nO paciente: {nickname} está em perigo!'
    else:
        message += f'\nO paciente: {nickname} encontra-se bem!'
    
def write():
    message = diagnostic()
    server.send(message.encode())

def pacient_generator():
    array_de_nomes = ["Miguel", "Denerson", "Heitor", "Theo", "Gabriel", "Bernardo", "Samuel", "Mairon", "Helena", "Luana", "Laura", "Maria Alice", "Poli", "Luisa", "Maria Clara", "Maria Cecilia", "Maria Julia"]
    array_de_sobrenomes = ["Silva", "Azevedo", "Oliveira", "Tobias", "Rodrigues", "Ferreira", "Berudio",  "Pereira", "Lima", "Leal", "Ribeiro"]

    infos = []
    batimentos = []

    nome = str(array_de_nomes[random.randint(0, 16)]) + " " + str(array_de_sobrenomes[random.randint(0, 9)])
    idade = random.randint(45, 90)

    for _ in range(0, 60):
        batimentos.append(random.randint(50, 90))

    infos.append(nome)
    infos.append(idade)
    infos.append(batimentos)
    return infos

paciente_exemplo = pacient_generator()
nickname = paciente_exemplo[0]

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
ClientMultiSocket = socket.socket()