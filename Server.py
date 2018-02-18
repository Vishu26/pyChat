from threading import Thread
import socket
import time
import sqlite3
import os
from ast import literal_eval
class server:
       def __init__(self):
              self.host=socket.gethostbyname('0.0.0.0')
              self.port=5000
              self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
              self.clients={}
              self.s.bind((self.host,self.port))
              self.s.setblocking(0)
              self.quitting=False
              self.con=""
              self.cur=""
              #self.cur.execute("CREATE TABLE IF NOT EXISTS data(username varchar(64) not null,password varchar(64),lastseen varchar(64),addr varchar(64),PRIMARY KEY (username))")
              #self.cur.execute("CREATE TABLE IF NOT EXISTS chat(user1 varchar(64) not null,user2 varchar(64) not null,addr varchar(64),PRIMARY KEY (user1))")              
              print("Server has started")
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
              Thread(target=self.run).start()
       def check(self,data,addr):
              if True:
                     print("HI")
                     self.con=sqlite3.connect('server.db')
                     self.cur=self.con.cursor()
                     data=data.split(' ')
                     data[3]=" ".join(data[3:])
                     user=(data[1],)
                     self.cur.execute("SELECT password FROM data WHERE username=? LIMIT 1",user)
                     line=self.cur.fetchone()
                    
                     if line:
                            if line[0]==data[3]:
                                   adr=(str([addr[0],str(addr[1])]),data[1],)
                                   self.cur.execute("UPDATE data SET lastseen='Online',addr=? WHERE username=?",adr)
                                   self.s.sendto("Success".encode('utf-8'),addr)
                                   print(line[0])
                                   """if os.path.isfile('database/'+data[1]+".db"):
                                          with open('database/'+data[1]+".db","rb") as file:
                                                 a=file.read()
                                          self.s.sendto(a,addr)"""
                            
                                   self.cur.execute("SELECT addr FROM chat WHERE user2=?",user)
                                   take=self.cur.fetchall()
                                   if take:
                                          for i in take:
                                                 a=literal_eval(i[0])
                                                 a[1]=int(a[1])
                                                 self.s.sendto(adr[0].encode('utf-8'),tuple(a))
                                   self.con.commit()
                                   self.con.close()
                            else:
                                   self.s.sendto("Failure".encode('utf-8'),addr)
                                   self.con.close()
                     else:
                            self.s.sendto("Failure".encode('utf-8'),addr)
                            self.con.close()
                            return
              
       def sign(self,data,addr):
              self.con=sqlite3.connect('server.db')
              self.cur=self.con.cursor()
              data=data.split(' ')
              data[2]=" ".join(data[2:])
              self.cur.execute("SELECT password FROM data WHERE username=? LIMIT 1",(data[1],))
              line=self.cur.fetchone()
              if line:
                     self.s.sendto("exists".encode('utf-8'),addr)
                     self.con.close()
              else:
                     self.cur.execute("INSERT INTO data VALUES(?,?,'Online',?)",(data[1],data[2],str([addr[0],str(addr[1])])))                    
                     self.s.sendto("Success".encode('utf-8'),addr)
              self.con.commit()
              self.con.close()
                     
              
       def run(self):
              while not self.quitting:
                     try:
                            data,addr=self.s.recvfrom(1024)
                            data=data.decode('utf-8')
                            if "User" in data:
                                   Thread(target=self.check,args=(data,addr,)).start()
                            elif "Signup" in data:
                                   Thread(target=self.sign,args=(data,addr,)).start()
                     except:
                            pass
              self.s.close()
c=server()
