import threading
import socket
import time

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

def broadcast(message, client):
    try:
        client.send(message)
    except:
        print("Médico não encontrado!")

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
            if 'perigo!' in message:
                message_to_doctor = "Um paciente está em perigo!"
                message_to_patient = "Seus batimentos não estão regulares, o médico já foi acionado!"
                broadcast(message_to_doctor.encode(), clients[0])
                broadcast(message_to_patient.encode(), clients.pop())
            else:
                message_to_patient = "Seus batimentos estão ótimos!"
                broadcast(message_to_patient.encode(), clients.pop())
        except:
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()

        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        clients.append(client)

        print(nickname + ' conectou-se ao servidor!')
        client.send(f'Seja bem vindo(a) à plataforma, {nickname}!'.encode())
        time.sleep(1)
        if len(clients) > 1:
            client.send('Será feita uma leitura dos seus batimentos...'.encode())
            time.sleep(1)

        thread = threading.Thread(target = handle, args = (client,))
        thread.start()

print('Server is listening...')
receive()