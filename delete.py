import sqlite3


class deletedata:
    def __init__(self):
        self.conn=sqlite3.connect('sms.db')

        self.cur=self.conn.cursor()



    def deletestudent(self, sid):
        
        self.cur.execute('''
            DELETE FROM STUDENT 
            WHERE SID = ?
        ''', (sid,))  
                            
                  
        self.conn.commit()
        print("The data has been deleted sucessfully")
    
    def deletecourse(self, cid):
        
        self.cur.execute('''
            DELETE FROM COURSE 
            WHERE CID = ?
        ''', (cid,))  
                            
                  
        self.conn.commit()
        print("The data has been deleted sucessfully")
    
    def deletetrans(self, tid):
        
        self.cur.execute('''
            DELETE FROM TRANS 
            WHERE TID = ?
        ''', (tid,))  
                            
                  
        self.conn.commit()
        print("The data has been deleted sucessfully")
