import socket
import threading

nickname = "Dr. Flávio Seixas"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 8080))

def receive():
    danger_counter = 0

    while True:
        try:
            message = server.recv(1024).decode()

            if message == 'NICK':
                server.send(nickname.encode())
            elif 'perigo!' in message:
                danger_counter += 1
                print(message)
                print(f'Contagem atual de pacientes em perigo: {danger_counter}')
            else:
                print(message)
        except:
            print('An error has ocurred!')
            server.close()
            break
    
def write():
    while True:
        message = nickname + ' diz: ' + input('')
        server.send(message.encode())

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
ClientMultiSocket = socket.socket()