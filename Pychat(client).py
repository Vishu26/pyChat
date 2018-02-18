from tkinter import *
from tkinter import messagebox
import threading
import socket
import time
from itertools import cycle
from ast import literal_eval
import sqlite3

ad=False
serv_search=('127.0.0.1',5001)
serv_online=('127.0.0.1',5002)
serv_del=('127.0.0.1',5003)
serv_msg=('127.0.0.1',10101)

check=False
a=["#D2691E", "#D0661E", "#CE631F", "#CC601F", "#CA5E20", "#C85B20", "#C65821", "#C45521", "#C25322", "#C05022", "#BE4D23", "#BC4A23", "#BA4824", "#B84524", "#B64225", "#B43F25", "#B23D26", "#B03A26", "#AE3727", "#AC3427", "#AA3228", "#A82F28", "#A62C29", "#A52A2A", "#A0282E", "#9C2632", "#982436", "#94223A", "#90203E", "#8C1E42", "#881C46", "#841A4A", "#80184E", "#7C1652", "#781556", "#73135A", "#6F115E", "#6B0F62", "#670D66", "#630B6A", "#5F096E", "#5B0772", "#570576", "#53037A", "#4F017E", "#4B0082", "#47007C", "#440076", "#400070", "#3D006A", "#390064", "#36005E", "#330058", "#2F0052", "#2C004C", "#280046", "#250041", "#22003B", "#1E0035", "#1B002F", "#170029", "#140023", "#11001D", "#0D0017", "#0A0011", "#06000B", "#030005", "#000000", "#080401", "#110802", "#190D04", "#221105", "#2A1506", "#331A08", "#3C1E09", "#44220A", "#4D270C", "#552B0D", "#5E300F", "#673410", "#6F3811", "#783D13", "#804114", "#894515", "#924A17", "#9A4E18", "#A35219", "#AB571B", "#B45B1C", "#BD601E"]
ret=""
b=a[1:]+a[0:1]
c=a[2:]+a[0:2]
d=a[3:]+a[0:3]
e=a[4:]+a[0:4]
f=a[5:]+a[0:5]
g=a[6:]+a[0:6]
h=a[7:]+a[0:7]
def back(x,y,z):
       global check
       for i in cycle(range(len(a))):
              try:
                     if check==True:
                            return
                     y.config(bg=b[i])
                     x.itemconfig(z[0],fill=a[i])
                     x.itemconfig(z[1],fill=b[i])
                     x.itemconfig(z[2],fill=c[i])
                     x.itemconfig(z[3],fill=d[i])
                     x.itemconfig(z[4],fill=e[i])
                     x.itemconfig(z[5],fill=f[i])
                     x.itemconfig(z[6],fill=g[i])
                     x.itemconfig(z[7],fill=h[i])
                     if ret!="":
                            ret.config(bg=b[i])
                     time.sleep(0.3)
              except:
                     pass
     
class login:
       def __init__(self):
              global ret
              self.root=Tk()
              self.host='127.0.0.1'
              self.port=0
              self.server=('127.0.0.1',5000)
              self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
              self.s.bind((self.host,self.port))
              #self.root.bind("<Key>",self.d)
              self.username=""
              self.cp=""
              self.cpp=""
              self.rett=""
              self.lab=""
              self.labb=""
              self.window=Canvas(self.root,width=800,height=600)
              self.user=Entry(self.window,width=30,fg="#D3D3D3",font=("",12))
              self.user.insert(0,"Username")
              self.window.create_window(400,300,window=self.user)
              self.user.bind("<Button-1>",self.d)
              self.pas=Entry(self.window,width=30,fg="#D3D3D3",font=("",12))
              self.window.create_window(400,340,window=self.pas)
              self.pas.insert(0,"Password")
              self.pas.bind("<Button-1>",self.p)
              self.log=Button(self.window,text="Log in",width=25,fg="#D3D3D3",command=self.logg)
              self.login=self.window.create_window(400,380,window=self.log)
              self.tri=[]
              self.tri.append(self.window.create_polygon([0,0,0,150,200,0],fill="blue"))
              self.tri.append(self.window.create_polygon([0,150,0,300,400,0,200,0]))
              self.tri.append(self.window.create_polygon([0,300,0,450,600,0,400,0]))
              self.tri.append(self.window.create_polygon([0,450,0,600,800,0,600,0]))
              self.tri.append(self.window.create_polygon([0,600,200,600,800,150,800,0]))
              self.tri.append(self.window.create_polygon([200,600,400,600,800,300,800,150]))
              self.tri.append(self.window.create_polygon([400,600,600,600,800,450,800,300]))
              self.tri.append(self.window.create_polygon([600,600,800,600,800,450]))
              self.window.pack()
              self.window.create_text(400,250,text="PyChat",fill="white",font=("Helvetica",24))
              self.text=self.window.create_text(400,550,text="New User? Sign up.",font=("",14),fill="#D3D3D3")
              self.window.tag_bind(self.text,"<Button-1>",self.si)
              threading.Thread(target=back,args=(self.window,self.log,self.tri,)).start()
       def logg(self):
              global check
              user=self.user.get()
              pas=self.pas.get()
              print(user+" "+pas)
              msg="User "+user+" Pass "+pas
              self.s.sendto(msg.encode('utf-8'),self.server)
              data=""
              while data=="":
                     data,addr=self.s.recvfrom(1024)
                     data=str(data.decode('utf-8'))
              if data=="Success":
                     self.username=user
                     line,addr=self.s.recvfrom(50000)
                     with open('user.db','wb') as file:
                            file.write(line)
                            
                     self.window.pack_forget()
                     check=True
                     c=chat(self)
              else:
                     if self.lab=="":
                            self.lab=Label(self.window,text="Username or Password not correct",bg='red',fg='white')
                            self.labb=self.window.create_window(0,0,window=self.lab,width=804,anchor=N+W)
                     else:
                            self.lab.config(text="Username or Password not correct")
                     return
                     
       def d(self,event):
              if self.user.get()=="Username":
                     self.user.delete(0,END)
                     self.user.config(fg="black")
       def si(self,event):
              global ret
              self.window.delete(self.login)
              self.cp=Entry(self.window,width=30,fg="#D3D3D3",font=("",12))
              self.cp.insert(0,"Confirm Password")
              self.cp.bind("<Button-1>",self.cnf)
              self.cpp=self.window.create_window(400,380,window=self.cp)
              self.log.config(text="Signup",command=self.up)
              self.login=self.window.create_window(400,420,window=self.log)
              ret=Button(self.window,text="Back",width=25,fg="#D3D3D3",command=self.retn)
              self.rett=self.window.create_window(400,460,window=ret)
              self.window.delete(self.text)
              self.pas.delete(0,END)
              self.pas.config(fg="#D3D3D3",show="")
              self.pas.insert(0,"Password")
              if self.lab!="":
                     self.window.delete(self.labb)
                     self.lab=""
       def up(self):
              global check
              user=self.user.get()
              pas=self.pas.get()
              cnf=self.cp.get()
              if " " in user:
                     if self.lab=="":
                            self.lab=Label(self.window,text="Username cannot contain spaces",bg='red',fg='white')
                            self.labb=self.window.create_window(0,0,window=self.lab,width=804,anchor=N+W)
                     else:
                            self.lab.config(text="Username cannot contain spaces")
                     return
              elif pas!=cnf:
                     if self.lab=="":
                            self.lab=Label(self.window,text="Password does not match",bg='red',fg='white')
                            self.labb=self.window.create_window(0,0,window=self.lab,width=804,anchor=N+W)
                     else:
                            self.lab.config(text="Password does not match")
                     return
              else:
                     global check
                     user=self.user.get()
                     pas=self.pas.get()
                     print(user+" "+pas)
                     msg="Signup"+" "+user+" "+pas
                     self.s.sendto(msg.encode('utf-8'),self.server)
                     data=""
                     while data=="":
                            data,addr=self.s.recvfrom(1024)
                            data=str(data.decode('utf-8'))
                     if data=="Success":
                            self.username=user
                            self.window.pack_forget()
                            check=True
                            c=chat(self)
                     else:
                            if self.lab=="":
                                   self.lab=Label(self.window,text="Username already exists",bg='red',fg='white')
                                   self.labb=self.window.create_window(0,0,window=self.lab,width=804,anchor=N+W)
                            else:
                                   self.lab.config(text="Username already exists")
                            return
                            
                     
       def retn(self):
              global ret
              if self.lab!="":
                     self.window.delete(self.labb)
                     self.lab=""
              self.window.delete(self.cpp)
              self.window.delete(self.login)
              self.window.delete(self.rett)
              self.pas.delete(0,END)
              self.pas.config(fg="#D3D3D3",show="")
              self.pas.insert(0,"Password")
              ret=""
              self.log.config(text="Log in",command=self.logg)
              self.login=self.window.create_window(400,380,window=self.log)
              self.text=self.window.create_text(400,550,text="New User? Sign up.",font=("",14),fill="#D3D3D3")
              self.window.tag_bind(self.text,"<Button-1>",self.si)
              
       def cnf(self,event):
              if self.cp.get()=="Confirm Password":
                     self.cp.delete(0,END)
                     self.cp.config(fg="black",show="*")
       
       def p(self,event):
              if self.pas.get()=="Password":
                     self.pas.delete(0,END)
                     self.pas.config(fg="black",show="*")

class chat:
       def __init__(self,other):
              self.lock=threading.Lock()
              self.other=other
              self.root=other.root
              self.tx=""
              self.con=""
              self.cur=""
              self.window=Canvas(self.root,width=800,height=600,background="white")
              self.temp=""
              self.lab=Label(self.window,text="PyChat",fg="green",bg="#D3D3D3",font=("",20))
              self.window.create_window(0,39,window=self.lab,anchor=S+W,width=810)
              self.fr=Frame(self.window)
              self.window.create_window(0,39,window=self.fr,anchor=N+W,width=804,height=524)
              self.can=Canvas(self.fr,width=804,height=524)
              self.frame=Frame(self.can,bg="blue")
              #self.window.create_rectangle(0,35,800,0,fill="#D3D3D3")
              #self.out=self.window.create_text(50,20,text="PyChat",fill="green",font=("",20))
              self.scrollbar=Scrollbar(self.can,orient=VERTICAL,command=self.can.yview)
              self.can.configure(yscrollcommand=self.scrollbar.set)
              self.scrollbar.pack(side=RIGHT,fill=Y)
              self.lab.bind("<Button-1>",self.page)
              self.root.protocol("WM_DELETE_WINDOW",self.ask)
              self.can.pack(side=RIGHT,fill=BOTH,expand=True)
              self.can.create_window(0,0,window=self.frame,anchor=N+W)
              self.search=Entry(self.window,width=20,font=("",12))
              self.window.create_window(400,580,window=self.search)
              self.window.create_text(240,580,text="Add Username:",fill="green",font=("",12))
              self.sbut=Button(self.window,text="ADD",font=("",12),command=self.add)
              self.window.create_window(530,580,window=self.sbut)
              self.window.pack()
              self.frame.bind("<Configure>", self.onFrameConfigure)
              self.chats=[]
              self.warn=""
              self.warnn=""
              self.status=""
              threading.Thread(target=self.msg).start()
              threading.Thread(target=self.msg).start()
              threading.Thread(target=self.msg).start()
              threading.Thread(target=self.msg).start()
              threading.Thread(target=self.load).start()
       def load(self):
              for i in self.chats:
                     i.pack_forget()
                     i.destroy()
              self.chats=[]
              self.con=sqlite3.connect('user.db')
              self.cur=self.con.cursor()
              self.cur.execute("CREATE TABLE IF NOT EXISTS buddy(user varchar(64) not null,msg INT,num INT,PRIMARY KEY(user))")
              self.cur.execute("CREATE TABLE IF NOT EXISTS data(user varchar(64) not null,msg varchar(10000))")
              self.cur.execute("SELECT user FROM buddy ORDER BY num ASC")
              line=self.cur.fetchall()
              print(line)
              if line:
                     for i in line:
                            l=Label(self.frame,text=i,font=("",20),width=50,justify=RIGHT)
                            self.chats.append(l)
                            l.bind("<Button-1>",lambda x,t=l["text"]:self.texting(t))
                            l.pack()
              self.con.commit()
              self.con.close()
              
       def onFrameConfigure(self, event):
              self.can.configure(scrollregion=self.can.bbox("all"))
       def add(self):
              global ad
              global serv_search
              #ad=True
              if self.search.get()!=self.other.username:
                     self.other.s.sendto((self.search.get()).encode('utf-8'),serv_search)
              self.search.delete(0,END)
       def texting(self,m):
              print(m)
              self.other.s.sendto((self.other.username+" "+m).encode('utf-8'),serv_online)
              self.window.pack_forget()
              self.tx=text(self,m)
       #def ba(self):
              #global serv_del
              #self.other.s.sendto(self.other.username.encode('utf-8'),serv_del)
              #self.temp.pack_forget()
              #self.window.pack()
       def update(self,data):
              self.lock.acquire()
              con=sqlite3.connect('user.db')
              cur=con.cursor()
              cur.execute("UPDATE buddy SET num=num+1")
              cur.execute("INSERT INTO buddy VALUES(?,0,1)",(data,))
              con.commit()
              con.close()
              self.lock.release()
       def rem(self,num=0):
              if num==0:
                     self.window.delete(self.warnn)
              else:
                     self.tx.window.delete(self.warnn)
       def msg(self):
              global serv_search
              global serv_online
              data=""
              while not ad:
                     data,addr=self.other.s.recvfrom(1024)
                     data=data.decode('utf-8')
                     if addr==serv_search:
                            if data!="no":
                                   for i in self.chats:
                                          if i["text"]==data[0]:
                                                 return
                                   threading.Thread(target=self.update,args=(data,)).start()
                                   threading.Thread(target=self.load).start()
                            else:
                                   self.warn=Label(self.window,text="Username does not exists",bg='red',fg='white')
                                   self.warnn=self.window.create_window(0,0,window=self.warn,width=804,anchor=N+W)
                                   self.root.after(4000,self.rem)                   
                     elif addr==serv_online:
                            if data[0]!="[":
                                   while not hasattr(self.tx,'lab'):
                                          pass
                                   self.tx.lab.config(text=self.tx.name+"  -  "+str(data))
                                   self.tx.addr=""
                                                        #self.status=self.temp.create_text(200,200,text=str(data),font=("",20))
                            else:
                                   while not hasattr(self.tx,'lab'):
                                          pass
                                   self.tx.lab.config(text=self.tx.name+"  -  Online")
                                   self.tx.addr=literal_eval(data)
                                   self.tx.addr[1]=int(self.tx.addr[1])
                                   self.tx.addr=tuple(self.tx.addr)
                     elif addr==serv_msg:
                            if data[0]!="[":
                                   self.tx.lab.config(text=self.tx.name+"  -  "+str(data))
                                   self.tx.addr=""
                            else:
                                   self.tx.lab.config(text=self.tx.name+"  -  Online")
                                   self.tx.addr=literal_eval(data)
                                   self.tx.addr[1]=int(self.tx.addr[1])
                                   self.tx.addr=tuple(self.tx.addr)
                     else:
                            data=data.split(':::::')
                            if self.tx!="" and addr==self.tx.addr: 
                                   Label(self.tx.frame,text=data[1],font=("",14),width=50,bg="red",anchor=W,wraplength=300).pack()
                                   threading.Thread(target=self.save,args=(self.tx.name,data[1],)).start()
                            elif self.tx!="":
                                   self.warn=Label(self.tx.window,text=data[0]+": "+data[1],bg='red',fg='white')
                                   self.warnn=self.tx.window.create_window(0,0,window=self.warn,width=804,anchor=N+W)
                                   self.root.after(4000,self.rem)
                                   for i in self.chats:
                                          if i["text"]==data[0]:
                                                 threading.Thread(target=self.save,args=(data[0],data[1],)).start()
                                                 return

                                   threading.Thread(target=self.update,args=(data[0],)).start()
                                   threading.Thread(target=self.save,args=(data[0],data[1],)).start()
              
                            else:
                                   self.warn=Label(self.window,text=data[0]+": "+data[1],bg='red',fg='white')
                                   self.warnn=self.window.create_window(0,0,window=self.warn,width=804,anchor=N+W)
                                   self.root.after(4000,self.rem)
                                   for i in self.chats:
                                          if i["text"]==data[0]:
                                                 threading.Thread(target=self.save,args=(data[0],data[1],)).start()
                                                 if self.chats[0]["text"]!=data[0]:
                                                        threading.Thread(target=self.load).start()
                                                 return
                                                 
                                   #threading.Thread(target=self.update,args=(data[0],)).start()
                                   con=sqlite3.connect('user.db')
                                   cur=con.cursor()
                                   cur.execute("UPDATE buddy SET num=num+1")
                                   cur.execute("INSERT INTO buddy VALUES(?,0,1)",(data[0],))
                                   con.commit()
                                   con.close()
                                   threading.Thread(target=self.save,args=(data[0],data[1],)).start()
                                   threading.Thread(target=self.load).start()
                                   
                                          
                                          
       def page(self,event):
              global check
              check=False
              self.window.pack_forget()
              self.other.window.pack()
              threading.Thread(target=back,args=(self.other.window,self.other.log,self.other.tri)).start()
       #def ad(self,event):
              #print("Add")
       def ask(self):
              global serv_msg
              if messagebox.askokcancel("Quit","Do you want to quit?"):
                     #self.other.s.sendto(("Out "+self.other.username).encode('utf-8'),self.other.server)
                     with open("user.db","rb") as file:
                            line=file.read()
                     self.other.s.sendto(line,serv_msg)
                     self.root.destroy()
       def save(self,name,msg):
              self.lock.acquire()
              con=sqlite3.connect('user.db')
              cur=con.cursor()
              if name!=self.other.username:
                     cur.execute("SELECT num FROM buddy WHERE user=?",(name,))
                     p=cur.fetchone()
                     cur.execute("UPDATE buddy SET num=num+1 WHERE num<?",p)
                     cur.execute("UPDATE buddy SET msg=msg+1,num=1 WHERE user=?",(name,))
                     cur.execute("SELECT msg FROM buddy WHERE user=?",(name,))
                     p=cur.fetchone() 
                     cur.execute("INSERT INTO data VALUES(?,?)",(name+":"+self.other.username+":"+str(p[0]),msg,))
              else:
                     
                     cur.execute("SELECT num FROM buddy WHERE user=?",(self.tx.name,))
                     p=cur.fetchone()
                     cur.execute("UPDATE buddy SET num=num+1 WHERE num<?",p)
                     cur.execute("UPDATE buddy SET msg=msg+1,num=1 WHERE user=?",(self.tx.name,))
                     cur.execute("SELECT msg FROM buddy WHERE user=?",(self.tx.name,))
                     p=cur.fetchone()
                     cur.execute("INSERT INTO data VALUES(?,?)",(self.other.username+":"+self.tx.name+":"+str(p[0]),msg,))
              con.commit()
              con.close()
              self.lock.release()
                     
class text:
       def __init__(self,other,m):
              self.root=other.root
              self.other=other
              self.obj=self.other.chats
              self.name=m
              self.window=Canvas(self.root,width=800,height=600,background="white")
              self.temp=""
              self.addr=""
              self.lab=Label(self.window,text=m,fg="green",bg="#D3D3D3",font=("",20))
              self.window.create_window(0,39,window=self.lab,anchor=S+W,width=810)
              self.lab.bind("<Button-1>",self.ba)
              self.fr=Frame(self.window)
              self.window.create_window(0,39,window=self.fr,anchor=N+W,width=804,height=524)
              self.can=Canvas(self.fr,width=804,height=524)
              self.frame=Frame(self.can)
              self.scrollbar=Scrollbar(self.can,orient=VERTICAL,command=self.can.yview)
              self.can.configure(yscrollcommand=self.scrollbar.set)
              self.scrollbar.pack(side=RIGHT,fill=Y)
              self.search=Entry(self.window,width=40,font=("",12))
              self.window.create_window(300,580,window=self.search)
              self.sbut=Button(self.window,text="Send",font=("",12),command=self.send)
              self.window.create_window(530,580,window=self.sbut)
              self.can.pack(side=RIGHT,fill=BOTH,expand=True)
              self.can.create_window(0,0,window=self.frame,anchor=N+W)
              self.window.pack()
              self.frame.bind("<Configure>", self.onFrameConfigure)
              threading.Thread(target=self.load).start()
       def onFrameConfigure(self, event):
              self.can.configure(scrollregion=self.can.bbox("all"))
       def ba(self,e):
              global serv_del
              self.other.other.s.sendto(self.other.other.username.encode('utf-8'),serv_del)
              self.window.pack_forget()
              self.other.window.pack()
              if self.obj!=self.other.chats:
                     threading.Thread(target=self.other.load).start()
              self.other.tx=""
       def send(self):
              if self.addr!="":
                     msg=self.search.get()
                     self.other.other.s.sendto((self.other.other.username+":::::"+msg).encode('utf-8'),self.addr)
                     self.search.delete(0,END)
                     Label(self.frame,text=msg,font=("",14),width=50,anchor=E,bg="blue",wraplength=300).pack()
                     threading.Thread(target=self.other.save,args=(self.other.other.username,msg,)).start()
              """else:
                     msg=self.search.get()
                     self.other.other.s.sendto(msg.encode('utf-8'),serv_msg)
                     self.search.delete(0,END)
                     Label(self.frame,text=i[1],font=("",14),width=90,justify=RIGHT,wraplength=300).pack()
                     threading.Thread(target=self.save,args=(self.other.other.username,msg,)).start()"""
       def load(self):
              self.con=sqlite3.connect('user.db')
              self.cur=self.con.cursor()
              self.cur=self.cur.execute("SELECT * FROM data WHERE (user LIKE ? OR user LIKE ?)",(self.name+"%",self.other.other.username+":"+self.name+"%",))
              line=self.cur.fetchall()
              if line:
                     for i in line:
                            if i[0].startswith(self.name):
                                   Label(self.frame,text=i[1],font=("",14),pady=20,width=50,bg="red",anchor=W,wraplength=300).pack()
                            else:
                                   Label(self.frame,text=i[1],font=("",14),pady=20,width=50,bg="blue",anchor=E,wraplength=300).pack()
       
l=login()
l.root.resizable(0,0)
l.root.mainloop()    
