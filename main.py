from insert import insertdata
from delete import deletedata
from read import readdata
from update import updatedata
obj=insertdata()
obj1=deletedata()
obj2=readdata()
obj3=updatedata()

print("----------Student Management System--------------")

print(" Insert Press-1 \n Updation Press-2  \n Delete Press-3 \n Reading Press-4")


num=int(input("enter the number : "))

if num==1:
    print("Choose 1 for Student : \n Choose 2 for Course : \n Choose 3 for Transact : ")
    n=int(input("Enter the options : "))

    if n==1:
        sid=int(input("Enter ID : "))
        sname=input("Enter your name : ")
        email=input("Enter your Email : ")
        city=input("Enter yor city :  ")
        obj.insertstudent(sid,sname,email,city)

    if n==2:
        cid=int(input("Enter the course ID : "))
        course=input("Enter the Course : ")
        csid=int(input("Enter the csid : "))
        price=int(input("Enter the Price : "))

        obj.insertcourse(cid,course,csid,price)

    if n==3:
        tid=int(input("Enter ID : "))
        tsid=int(input("Enter your tsid : "))
        cid=int(input("Enter your cid : "))
        method=input("Enter yor method :  ")

        obj.trans(tid,tsid,cid,method)

if num == 2:
    print("Choose 1 for Student : \n Choose 2 for Course : \n Choose 3 for Transact : ")
    n = int(input("Enter the options : "))

    if n == 1:
        sid = int(input("Enter the StudentId you want to update : "))
        sname = input("Enter new name (leave blank to skip): ")
        email = input("Enter new Email (leave blank to skip): ")
        city = input("Enter new city (leave blank to skip): ")
        obj3.updatestudent(sid, sname,email,city)

    if n == 2:
        cid = int(input("Enter the CourseId you want to update : "))
        course = input("Enter new Course (leave blank to skip): ")
        csid = int(input("Enter new csid (leave blank to skip): "))
        price = int(input("Enter new Price (leave blank to skip): "))
        obj3.updatecourse(cid, course,csid,price)

    if n == 3:
        tid = int(input("Enter the TID you want to update : "))
        tsid = int(input("Enter new tsid (leave blank to skip): ") or 0)
        cid = int(input("Enter new cid (leave blank to skip): ") or 0)
        method = input("Enter new method (leave blank to skip): ")
        obj3.updatetransac(tid,tsid,cid,method)














if num==3:
    print("Choose 1 for Student : \n Choose 2 for Course : \n Choose 3 for Transact : ")
    n=int(input("Enter the options : "))
     


    if n==1:
         sid=int(input("Enter the StudentId you want to delete : "))
         obj1.deletestudent(sid) 

    if n==2:
        cid=int(input("Enter the courseid you want to delete"))
        obj1.deletecourse(cid)
    
    if n==3:
        tid=int(input("Enter the TID you want to delete"))
        obj1.deletetrans(tid)


if num==4:
    print("Choose 1 for Student : \n Choose 2 for Course : \n Choose 3 for Transact : ")
    
    n=int(input("Enter the options : "))

    if n==1:
        obj2.readstudents()
    
    if n==2:
        obj2.readcourse()

    if n==3:
        obj2.readtransac()
        




    
    
   








