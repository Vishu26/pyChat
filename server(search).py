from threading import Thread
import socket
import sqlite3
class server:
       def __init__(self):
              self.host=socket.gethostbyname('0.0.0.0')
              self.port=5001
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
       def add(self,data,addr):
              print(data)
              self.con=sqlite3.connect('server.db')
              self.cur=self.con.cursor()
              self.cur.execute("SELECT username FROM data WHERE username=? LIMIT 1",(data,))
              line=self.cur.fetchone()
              if line:
                     self.s.sendto(data.encode('utf-8'),addr)
                     self.con.close()
                     return
              self.s.sendto("no".encode('utf-8'),addr)
              self.con.close()
       def run(self):
              while not self.quitting:
                     try:
                            data,addr=self.s.recvfrom(1024)
                            data=data.decode('utf-8')
                            Thread(target=self.add,args=(data,addr,)).start()
                     except:
                            pass
              self.s.close()
c=server()
