import socket

s = socket.socket()
s.connect(("www.baidu.com", 80))
http = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"
s.sendall(http)
buf = s.recv(1024)
print(buf)
s.close()
