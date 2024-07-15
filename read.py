import sqlite3


class readdata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur=self.conn.cursor()
    

    def readstudents(self):
        self.cur.execute("SELECT * FROM STUDENT")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        
    
    def readcourse(self):
        self.cur.execute("SELECT * FROM COURSE")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
      
    
    def readtransac(self):
        self.cur.execute("SELECT * FROM TRANS")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
      