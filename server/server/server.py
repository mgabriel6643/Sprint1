# server.py

import socket
import os

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicia o servidor

server.bind(('localhost', 30000))  # Associa a conexão socket ao meu endereço local
server.listen(5)  # Espera alguém se conectar → Permite aceitar conexões. (Número de conexões não aceitas)
print('Servidor rodando...')


def receive_file():
    """Receives file from the client using sockets.

    Returns:
        None
    """
    while True:
        socket_connection: socket.socket
        address: tuple
        socket_connection, address = server.accept()  # Aceita conexão, retorna um novo socket e o endereço do client

        path_file: str = socket_connection.recv(4096).decode()  # Recebe o arquivo de 4096Bytes por vez.
        file_name: str = path_file.split('\\')[-1]  # Pega o nome do arquivo

        print(f'Nome do arquivo: {file_name}')  # Mostra nome do arquivo
        path_directory: str = 'uploads/'
        if not os.path.exists(path_directory):  # Se o diretório não existe, ele o cria
            os.mkdir(path_directory)
        with open(path_directory + file_name, 'wb') as file:  # Recebe e escreve o arquivo em uploads/
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
