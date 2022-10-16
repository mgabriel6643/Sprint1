# client.py

import socket

client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicia o socket

client.connect(('localhost', 30000))  # conecta no servidor

file_path: str = str(input('Caminho do arquivo > '))  # endereço de onde vai ser upado

client.send(file_path.encode())  # pega o arquivo, transforma em bytes e envia


def send_file(fp: str):
    """Sends a file to the server using sockets.

    Args:
        fp: The file path

    Returns:
        None
    """

    with open(fp, 'rb') as file:
        while True:
            read_bytes: bytes = file.read(4096)
            if not read_bytes:
                break
            client.send(read_bytes)
        print('\nEnvio do arquivo concluído!')


send_file(file_path)
