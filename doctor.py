import socket
import threading

nickname = "Dr. Hans Chucrute"

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
            print('Ocorreu um erro!')
            server.close()
            break

receive_thread = threading.Thread(target = receive)
receive_thread.start()

ClientMultiSocket = socket.socket()