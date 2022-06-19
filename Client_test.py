import socket
import tkinter
from tkinter import *
import threading

class client_t:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Client')
        self.root.geometry("%dx%d+0+0" % (600,600))
        self.btn = tkinter.Button(self.root,text='Client On',command = self.tred)
        self.btn.pack()
        self.root.mainloop()

    def tred (self,event = None):
        self.th = threading.Thread(target = self.init_client)
        self.th.start()

    def init_client(self):
        print('Клиент вкл.')
        self.sock = socket.socket()
        self.sock.connect(('192.168.1.5', 10000))
        while True:
            self.p = self.sock.send('Client_1')
            print('Отправил : ',self.p)
            self.data = sock.recv(1024)

if __name__ == '__main__':
    client_t()

