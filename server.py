import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
s.bind(('0.0.0.0', port))
print ('Socket binded to port 3125')
s.listen(3)
print ('socket is listening')

keygud = 'Confirmed'
notgud = 'Error'

def stop(self):
    self.running = False
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect( (self.hostname, self.port))
    self.socket.close()
    
    
def ukay():
	s = socket.socket()
	port = 3124
	s.connect(('localhost', port))
	s.sendall(keygud.encode())
    	
def nugud():
	s = socket.socket()
	port = 3124
	s.connect(('localhost', port))
	s.sendall(notgud.encode())

while True:
    c, addr = s.accept()
    print ('Got connection from ', addr)
    msg = c.recv(1024)
    c.close()
    print (msg)
    self.stop()
    
    #verify
    
keygud = 'Confirmed'
notgud = 'Error'
  
  #some fake key
keys = ['sium', 'siumm']
for swim in keys:
    if msg == 'sium':
    	print('good')
    	ukay()
    		
    else:
    	print('Error')
    	nugud()
