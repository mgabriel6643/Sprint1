import socket


def client_config(file_path: str) -> socket.socket:
    """Executes the configuration needed for transfer.

    Args:
        file_path (str): The name of the file being uploaded.

    Returns:
        None.
    """
    client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicia o socket
    client.connect(('localhost', 30000))  # conecta no servidor
    client.send(file_path.encode())  # pega o arquivo, transforma em bytes e envia
    return client


def send_file(fp: str, client):
    """Sends a file to the server using sockets.

        Args:
            fp (str): The file path.
            client (socket.socket): Initializes socket connection.

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


def main():
    file_path: str = str(input('Caminho do arquivo > '))  # endereço de onde vai ser upado
    client = client_config(file_path)
    send_file(file_path, client)


if __name__ == '__main__':
    main()
