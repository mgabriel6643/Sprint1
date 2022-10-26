import unittest
from connection_client_server.client.client.client import Client
from connection_client_server.server.server.server import Server


class TestServer(unittest.TestCase):
    """Tests file transfers between client and server.
    """
    
    def setUp(self) -> None:
        self.client_object: Client = Client()
        self.server_object: Server = Server()
    
    def tearDown(self) -> None:
        self.server_object.terminate()
    
    def test_something(self):
        self.server_object.receive()
        self.client_object.send_byte('D:\OneDrive\mgabr\Documents\Engenharia Civil\Semestre 10\Administração e Empreendedorismo\Plano de Marketing(Passo a passo)1.pdf')
        self.assertEqual(True, False)  # add assertion here



if __name__ == '__main__':
    unittest.main()
