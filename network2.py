import socket 

#udp서버 
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind('',8284)#'127.0.0.1' 안써줘도 자기주소로 생각

print('bind port 8284')

_data , _rinfo = udp_socket.recvfrom(1024)

print(f'received : {_rinfo[0]}:{_rinfo[1]}:{_data.decode()}')

#%%
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print('init socket')
udp_socket.sendto ("hello".encode(),('',8284))
