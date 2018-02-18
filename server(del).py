from threading import Thread
import socket
import sqlite3
class server:
       def __init__(self):
              self.host=socket.gethostbyname('0.0.0.0')
              self.port=5003
              self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
              self.con=""
              self.cur=""
              self.s.bind((self.host,self.port))
              self.s.setblocking(0)
              self.quitting=False
              print("Server has started")
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
       def run(self):
              while not self.quitting:
                     try:
                            data,addr=self.s.recvfrom(1024)
                            data=data.decode('utf-8')
                            Thread(target=self.check,args=(data,)).start()
                     except:
                            pass
              self.s.close()
       def check(self,data):
              self.con=sqlite3.connect('server.db')
              self.cur=self.con.cursor()
              self.cur.execute("DELETE FROM chat WHERE user1=?",(data,))
              self.con.commit()
              self.con.close()
              
c=server()
              
              
              
