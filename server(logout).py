from threading import Thread
import socket
import os
import time
import sqlite3
from ast import literal_eval
class server:
       def __init__(self):
              self.host=socket.gethostbyname('0.0.0.0')
              self.port=10101
              self.con=""
              self.cur=""
              self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
              self.s.bind((self.host,self.port))
              self.s.setblocking(0)
              self.quitting=False
              print("Server has started")
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
       def seen(self,data,lastseen,addr):
              self.con=sqlite3.connect('server.db')
              self.cur=self.con.cursor()
              self.cur.execute("SELECT username FROM data WHERE addr=?",(addr,))
              line=self.cur.fetchone()
              print(line)
              self.cur.execute("UPDATE data SET lastseen=?,addr=null WHERE username=?",(lastseen,line[0],))
              self.cur.execute("SELECT addr FROM chat WHERE user2=?",(line[0],))
              take=self.cur.fetchall()
              if take:
                     for i in take:
                            a=literal_eval(i[0])
                            a[1]=int(a[1])
                            self.s.sendto(lastseen.encode('utf-8'),tuple(a))
              self.cur.execute("DELETE FROM chat WHERE user1=?",(line[0],))
              self.con.commit()
              self.con.close()
              print(os.path.isfile('database/'+line[0]+'.db'))
              with open('database/'+line[0]+'.db','wb') as file:
                     file.write(data)
       def run(self):
              while not self.quitting:
                     try:
                            data,addr=self.s.recvfrom(50000)
                            lastseen=time.ctime(time.time())
                            Thread(target=self.seen,args=(data,lastseen,str([addr[0],str(addr[1])]))).start()
                     except:
                            pass
c=server()
                            
