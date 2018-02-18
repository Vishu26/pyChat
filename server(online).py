from threading import Thread
import socket
import sqlite3
class server:
       def __init__(self):
              self.host=socket.gethostbyname('0.0.0.0')
              self.port=5002
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
                            Thread(target=self.check,args=(data,addr,)).start()
                     except:
                            pass
              self.s.close()
       def check(self,data,addr):
              data=data.split(' ')
              print(data)
              self.con=sqlite3.connect('server.db')
              self.cur=self.con.cursor()
              self.cur.execute("INSERT INTO chat VALUES(?,?,?)",(data[0],data[1],str([addr[0],str(addr[1])]),))
              self.cur.execute("SELECT lastseen,addr FROM data WHERE username=? LIMIT 1",(data[1],))
              line=self.cur.fetchone()
              if line[1]==None:
                     self.s.sendto((line[0]).encode('utf-8'),addr)       
              else:
                     self.s.sendto((line[1]).encode('utf-8'),addr)
              self.con.commit()
              self.con.close()
c=server()
                            
              
