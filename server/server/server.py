# server.py

import socket
import os

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(('localhost', 30000))
server.listen(5)
print('Servidor rodando...')


def receive_file():
    """Receives file from the client using sockets.

    Returns:
        None
    """
    while True:
        socket_connection: socket.socket
        address: tuple
        socket_connection, address = server.accept() 

        path_file: str = socket_connection.recv(4096).decode() 
        file_name: str = path_file.split('\\')[-1]  

        print(f'Nome do arquivo: {file_name}') 
        path_directory: str = 'uploads/'
        if not os.path.exists(path_directory): 
            os.mkdir(path_directory)
        with open(path_directory + file_name, 'wb') as file:  
            while True:
                received_bytes: bytes = socket_connection.recv(4096)
                if not received_bytes:
                    break
                file.write(received_bytes)

        socket_connection.close()
        break


receive_file()
server.close()
print('Recebimento de arquivo concluído')
