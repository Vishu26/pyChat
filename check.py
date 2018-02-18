import sqlite3
con=sqlite3.connect('server.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data(username varchar(64) not null,password varchar(64),lastseen varchar(64),addr varchar(64),PRIMARY KEY (username))")
cur.execute("CREATE TABLE IF NOT EXISTS chat(user1 varchar(64) not null,user2 varchar(64) not null,addr varchar(64),PRIMARY KEY (user1))")              
print(cur.execute("DELETE FROM chat").fetchall())
con.commit()
con.close()
