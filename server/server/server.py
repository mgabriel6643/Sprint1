import socket

HOST = 'localhost' #coloca o host do servidor
PORT = 57000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(1)
arq = open('/home/departamentos/financeiro/financeiro.tar.gz', 'r')

for i in arq.readlines():
    s.send(i)

arq.close()
s.close()
