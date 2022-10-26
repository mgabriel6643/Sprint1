import unittest
from connection_client_server.client.client.client import Client
from connection_client_server.server.server.server import Server


class TestClient(unittest.TestCase):
    """Tests file transfers between client and server."""
    client_object: Client = None
    server_object: Server = None

    def setUp(self) -> None:
        self.client_object = Client()
        self.server_object = Server()

    def tearDown(self) -> None:
        self.server_object.terminate()

    def test_path(self):
        test_path = self.client_object.path()
        with self.subTest('Tests if return is a string.'):
            self.assertEqual(type(test_path), str)
        with self.subTest('Tests if return is equal to the string typed.'):
            text = 'ASDASDASD'
            self.assertEqual(test_path, text)

    def test_connect_server(self):
        """Tests raises if server is disconnect."""
        with self.assertRaises(ConnectionRefusedError):
            self.client_object.connect_server()

    def test_send_byte(self):
        with self.assertRaises(OSError):
            self.client_object.send_byte('D:/OneDrive/mgabr/Documents/Engenharia Civil/Semestre 10/'
                                         'Enfâse de Construção Civil/Ingrid/Caderno de encargos.pdf')

    def test_send_file(self):
        """Tests a path file that doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            self.client_object.send_file('')


if __name__ == '__main__':
    unittest.main()
