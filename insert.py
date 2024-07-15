import sqlite3

class insertdata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur=self.conn.cursor()
    
    def insertstudent(self,sid,sname,email,city):
        self.cur.execute(f'''
                         INSERT INTO STUDENT VALUES(
                         {sid},
                         "{sname}",
                         "{email}",
                         "{city}"
                         )

                        
                   ''')
        self.conn.commit()
        print("----------Added Sucessfully In Student Table------------")
    
    

    def insertcourse(self,sid,course,csid,price):
        self.cur.execute(f'''
                         INSERT INTO COURSE VALUES(
                         {sid},
                         "{course}",
                         {csid},
                         {price}
                         )

                        
                   ''')
        self.conn.commit()
        print("----------Added Sucessfully In Course Table------------")

        

    def trans(self,tid,tsid,cid,method):
        self.cur.execute(f'''
                         INSERT INTO TRANS VALUES(
                         {tid},
                         {tsid},
                         {cid},
                         "{method}"
                         )

                        
                   ''')
        self.conn.commit()
        print("----------Added Sucessfully In TransacTable------------")



   

        
