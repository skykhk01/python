from socket import *
from threading import Thread, Lock, Event
import datetime
import time

# 수신 스레드를 만들어야 하는데 생성 순서와 소멸 순서를 좀 더 고민해서 만들어야 한다!
class Client(Thread):
    def __init__(self, serverIP, port):
        Thread.__init__(self)
        self.serverIP = serverIP
        self.port = port

    def run(self):
        print("클라이언트 스레드가 시작됬다!")

        clntSock = socket(AF_INET, SOCK_STREAM)
        clntSock.connect((self.serverIP, self.port))

        clntID = input("채팅에 사용될 아이디를 입력하세요 >> ")
        clntST = ClientSendThread(clntSock, clntID)

        clntST.start()
        clntST.join()

        print("클라이언트 스레드가 끝났다!")


class ClientSendThread(Thread):
    def __init__(self, clntSock, clntID):
        Thread.__init__(self)
        self.clntSock = clntSock
        self.clntID = clntID

    def run(self):
        print("클라이언트가 메시지 전송을 시작했다!")

        while True:
            dt_now = datetime.datetime.now()
            clntMsg = dt_now.strftime("%Y%m%d%H%M%S.%f") + ',' + self.clntID + ','
            clntMsg += input(self.clntID + " >> ")

            if clntMsg == "exit":
                self.clntSock.send(("{0}님이 채팅을 종료하였습니다.".format(self.clntID)).encode('utf-8'))
                break

            else:
                self.clntSock.send(clntMsg.encode('utf-8'))
                print("전송 성공")

        print("클라이언트가 메시지 전송을 끝냈습니다!")


if __name__ == "__main__":
    pass
