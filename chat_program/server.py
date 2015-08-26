__author__ = 'Hwankyu'

'''
from socket import *
svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.bind(('127.0.0.1', 2000))
svrSock.listen(1)
conn, addr = svrSock.accept()

recvBuf = conn.recv(1024)
print(len(recvBuf))
print(recvBuf)
'''


'''
    우선 연결된 클라이언트 정보를 저장해서 allSend(가칭)를 구현해서 클라이언트도 대화내용을 알게해야한다!
    대화 내용을 allSend로 보낼 때 들어온 메세지가 시간 순서에 맞게 되는지 항상 확인한다(?) --> 이게 오늘의 과제였나?
'''
from socketserver import ThreadingTCPServer, StreamRequestHandler

PORT = 2000

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        conn = self.request
        print('connection form', self.client_address)
        buf = conn.recv(1024)
        if not buf:
            print('nothing')
        else:
            print(buf.decode('utf-8'))


server = ThreadingTCPServer(('127.0.0.1', 2000), MyRequestHandler)
print('listening on port', PORT)
server.serve_forever()          # 얘는 한번만 실행되고 끝난다. 이걸 반복시킬 방법을 찾아야 한다!
