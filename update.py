import sqlite3

class updatedata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()


    def updatestudent(self,sid, sname,email,city):
        self.cur.execute(f'''UPDATE STUDENT 
                         SET sid=?,sname=?,email=?,city=?;
                         ''',(sid,sname,email,city)                             
                         

        )
        self.conn.commit()
        print("student data updated ")
    
    def updatecourse(self,cid, course,csid,price):
        self.cur.execute(f'''UPDATE COURSE 
                         SET cid=?,coursename=?,sid=?,price=?;
                         ''',(cid,course,csid,price)                             
                         

        )
        self.conn.commit()
        print("course data updated ")

    def updatetransac(self,tid,tsid,cid,method):
        self.cur.execute(f'''UPDATE TRANS 
                         SET tid=?,sid=?,cid=?,method=?;
                         ''',(tid,tsid,cid,method)                             
                         

        )
        self.conn.commit()
        print("transaction data updated ")
        

    