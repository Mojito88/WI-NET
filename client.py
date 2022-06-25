import socket

s = socket.socket()
port = 3125
s.connect(('localhost', port))
z = 'Your string'
s.sendall(z.encode())    
wait
