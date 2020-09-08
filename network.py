#네트워크 프로그래밍 
#%%
import socket 

#tcp 서버 객체
#소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#바인딩-> 
server_socket.bind(("",12000))
#접속대기
server_socket.listen(5)
print('wait connect')
#접속수락 
clent_socket, addr = server_socket.accept() #accpet에서 addr로 받음
print(f'connected{addr}')
#데이터 송수신 
print('wait data')
data = clent_socket,recv(1024)
print(f'received : {addr} : {data.decode()}')
#소켓 사용후 종료
clent_socket.close()
server_socket.close()
#%%
#tcp 클라이언트 객체 ->바인딩이 생략되고/ 접속 수락 불필요
# 소켓 생성 
client.socket = socket.socket(socket.AF_INET socket.SOCK_STREAM)
print('try to connect server...')
#접속시도 127.0.0.1 은 나 스스로를 가르키는 루프백 주소 
client_socket.connect(("127.0.0.1", 12000))
print('connected')
#데이터 송/수신 encode-> 소켓으로 주고받는 데이터 문자열 아니라 바이트 형태로 변환
print('sending message')
client _socket.sendall('안녕'.encode())
print('sending message ok')

print('wait message')
data = client_socket.recv(1024)
print(f'received : {data.decode()}')
#접속 종료
client_socket.close()
#%%
#프로그램-> 프로세스와 스레드로 동작, 
import time 

def 주문받기():
    for i in range(5):
        print("주문받기{}".format(i))
        time.sleep(1)
def 우편발송():
    for i in range(5):
        print("우편발송{}".format(i))
        time.sleep(0.5)
th1 =threading.Thread(target=주문받기)
th2 =threading.Thread(target=우편발송)

th1.daemon = True
th1.daemon = True

th1.start()
th2.start()
#%%
#믹스인 
class carMixIn:
    def ready(self):
        print("믹스인 레디")
    def start(self):
        print("{}가 {}속도로 달립니다".format(self.name, self.speed))
class Performance():
    def __init__(self, name, speed):
        self.name = name
        self.speed =speed
        self.ready() #Performance에는 없는 ready함수  SuperCar에 의해 믹스인됨 performance에서도 사용가능 
class SuperCar(carMixIn, Performance): #다중상속 
    def show_info(self): 
        print("{}는{}속도의 성능입니다".format(self.name, self.speed))
    
    #def start(self): -> carmixin 에서 쓰인 start 함수가 supercar에서 쓰이면 위에서 무효호 되어버림(오버라이딩)

s = SuperCar("람보르기니" ,300)
s.show_info()
s.start()      
