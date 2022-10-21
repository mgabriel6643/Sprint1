import unittest
from socket import socket
import client.client as client
import server.server as server


class TestClient(unittest.TestCase):
    """Tests file transfers between client and server.
    """
    def setUp(self) -> None:
        server.receive_file()
    def tearDown(self) -> None:
    def test_connect_server(self):
        test_socket = client.connect_server('D:\OneDrive\mgabr\Pictures\Surf\DSC08162.JPG')
        self.assertEqual(type(test_socket), socket)  # add assertion here


if __name__ == '__main__':
    unittest.main()
