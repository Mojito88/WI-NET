import socket
import sys
from tkinter import * 
import tkinter as tk
window = tk.Tk()

#title
window.title('WI-NET')

#px
window.geometry('450x550')  
#window color
window.configure(bg='#23252e') 
#resize
window.resizable(False,False)




#Body




l = Label(window, text = "Enter your key:", font = ('calibre',10,'normal'))
l.place(relx = 0, rely = 0.5, anchor = 'center')
l.pack()
port = 3124

def get_key():
	
	
		key = E1.get()
		print("sending to server key: "+ key)
		
		s = socket.socket()
		port = 3125
		s.connect(('localhost', port))
		s.sendall(key.encode())
		recive()
	
		
		
	    
	


	
b1 = Button(window, text = "Enter", command=get_key, font = ('calibre',10,'normal'))
b1.pack()
b1.place(x=350, y=50, in_=window)



E1 = Entry(window, bd =5, font = ('calibre',10,'normal'), show = '*')
E1.pack(side = RIGHT)
E1.place(x=130, y=50, in_=window)

def recive():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', port))
	s.listen(3)
	while True:
	    c, addr = s.accept()
	    print ('Got connection from ', addr)
	    msg = c.recv(1024)
	    c.close()
	    print (msg)




window.mainloop()
