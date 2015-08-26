import MyChatModule



def menu():
    print(" Chatting program : Client ".center(60,'*'))
    print("0. Exit")
    print("1. Server")
    print("2. Client")

    while True:
        number = input("Select number >> ")
        if not number.isdigit():
            print("Please enter only Arabic numerals.")
        else:
            number = int(number)
            if number >= 3:
                print("Please enter 0 ~ 2")

            else:
                return number

# 서버 IP 주소와 포트 정보를 입력받게 해야한다!
# 위의 정보를 바탕으로 서버가 채팅 가능한지 확인하는 부분이 필요할 거 같다. (여기에 둘지 생성할 때 확인할지 고민해보자)
def chat_client():
    client = MyChatModule.Client('127.0.0.1', 2000)
    client.start()
    client.join()


#  server.py의 부분을 MyChatModule에 client처럼 chat_server에서 실행가능하게 해야한다!
while True:
    step = menu()
    if step==1:
        pass
        # chat_server()
    elif step==2:
        chat_client()
    else:
        break