# client.py

import socket

client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 30000))

file_path: str = str(input('Caminho do arquivo > '))

client.send(file_path.encode())


def send_file(fp: str):
    """Sends a file to the server using sockets.

    Args:
        fp (str): The file path.

    Returns:
        None.
    """

    with open(fp, 'rb') as file:
        while True:
            read_bytes: bytes = file.read(4096)
            if not read_bytes:
                break
            client.send(read_bytes)
        print('\nEnvio do arquivo concluído!')


send_file(file_path)
