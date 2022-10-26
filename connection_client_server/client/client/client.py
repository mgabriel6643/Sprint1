import socket


class Client:
    def __init__(self):
        self.host = 'Localhost'
        self.port = 30000
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicia o socket

    @staticmethod
    def path() -> str:
        """Asks the user for the path to the file that will be uploaded.

        Returns:
            file_path (str): The path of to the file being uploaded.
        """
        file_path: str = str(input('Caminho do arquivo > '))  # endereço de onde vai ser upado
        return file_path

    def connect_server(self) -> None:
        """Connects to the server.
        Returns:
            None.
        """
        self.socket_client.connect((self.host, self.port))  # conecta no servidor

    def send_byte(self, file_path: str) -> None:
        """Sends the file path to the server.
        Args:
            file_path (str): The path of to the file being uploaded.

        Returns:
            None.
        """
        self.socket_client.send(file_path.encode())  # pega o arquivo, transforma em bytes e envia

    def send_file(self, file_path: str):
        """Sends a file to the server using sockets.

        Args:
            file_path (str): The path of to the file being uploaded.

        Returns:
            None.
        """
        with open(file_path, 'rb') as file:
            while True:
                read_bytes: bytes = file.read(4096)
                if not read_bytes:
                    break
                self.socket_client.send(read_bytes)
            print('\nEnvio do arquivo concluído!')

    def main(self):
        file_path = Client.path()
        Client.connect_server(self)
        Client.send_byte(self, file_path)
        Client.send_file(self, file_path)


if __name__ == '__main__':
    client = Client()
    client.main()
