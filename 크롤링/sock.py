import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#STREAM은 TCP통신
google_ip = socket.gethostbyname("google.com") 
#DNS(도메인 네임서버), 도메인을 아이피로 변환해주는 서버
sock.connect((google_ip, 80)) 
#address 인자는 host와 port 한쌍으로 받는 튜플형태 , 웹서버로 통신 80 port씀 
sock.send("GET / HTTP/1.1\n".encode())
# socket으로 통신하려면 모든 데이터는 바이너리 형식으로 들어와야함
sock.send("\n".encode())
# 데이터를 보냈고
buffer =sock.recv(4096)
buffer.decode().replace("\r\n","n")
#캐리지 리턴값을 파이썬으로 변형 
sock.close()
print(buffer)


