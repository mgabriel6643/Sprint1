import socket
import os


class Server:
    def __init__(self):
        self.host = 'Localhost'
        self.port = 30000
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicialização do socket

    def server_init(self) -> None:
        """Initializes the server.
        Returns:
            None.
        """

        self.socket_server.bind((self.host, self.port))

    def server_listen(self) -> None:
        """Waits for the client to connect.
        Returns:
            None.
        """
        self.socket_server.listen(5)
        print('Servidor aguardando conexão.')

    def receive(self) -> (str, socket.socket):
        """Receives file from the client.
        Returns:
            file_name (str): The name of the file that being uploaded.
            socket_connection (socket.socket): Allows the connection to happen.
        """
        socket_connection: socket.socket
        address: tuple
        socket_connection, address = self.socket_server.accept()

        path_file: str = socket_connection.recv(4096).decode()
        file_name: str = path_file.split('\\')[-1]  # Recebendo o arquivo
        return file_name, socket_connection

    @staticmethod
    def create_directory(path_directory):
        """Creates a directory, if it doesn't already exist.

        Args:
            path_directory (str): The directory which the file will be located.

        Returns:
            None.
        """
        if not os.path.exists(path_directory):
            os.mkdir(path_directory)

    @staticmethod
    def writes(path_directory, file_name, socket_connection):
        """Writes the file received from the client on a directory.
        Args:
            path_directory (str): The directory which the file will be located.
            file_name (str): The name of the file that being uploaded.
            socket_connection (socket.socket): Allows the connection to happen.

        Returns:
            None.
        """
        with open(path_directory + file_name, 'wb') as file:  # Escrevendo o arquivo
            while True:
                received_bytes: bytes = socket_connection.recv(4096)
                if not received_bytes:
                    break
                file.write(received_bytes)
        socket_connection.close()

    def terminate(self):
        self.socket_server.close()

    def main(self):
        """Receives file from the client using sockets.
        """
        Server.server_init(self)
        Server.server_listen(self)
        while True:
            file_name, socket_connection = Server.receive(self)
            print(f'Nome do arquivo: {file_name}')
            path_directory: str = 'uploads/'  # Cria a pasta destino
            Server.create_directory(path_directory)
            Server.writes(path_directory, file_name, socket_connection)
            break
        Server.terminate(self)
        print('Arquivo recebido.')


if __name__ == '__main__':
    server = Server()
    server.main()
