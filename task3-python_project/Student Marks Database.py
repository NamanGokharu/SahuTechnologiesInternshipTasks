
import MySQLdb
conn=MySQLdb.connect('localhost','root','','student marks')
cursor=conn.cursor()
def insert_details():
    name=input("Enter Student's Name: ")
    roll=input("Enter roll number: ")
    gender=input("Enter gender: ")
    contact=input("Enter Contact details: ")
    marks=int(input("Enter marks: "))
    email=input("Enter email id: ")
    grade=int(input("Enter grade: "))
    subjects=int(input("Enter total subjects"))
    per=marks/subjects
    tup1=(name,roll,gender,contact,marks,email,grade,per)
    s1="insert into `student marks`.`student`(`Name`, `Roll Number`, `Gender`, `Contact Details`, `Total Marks`, `Email`, `Grade`, `Percentage`) values(%s,%s,%s,%s,%s,%s,%s,%s);"
    try:
        cursor.execute(s1,tup1)
        conn.commit()
        print("Data successfully Inserted")
    except:
        conn.rollback()
        print("Insertion Error")

def delete_data():
    roll=input("Enter roll number: ")
    contact=input("Enter Contact details: ")
    s1="delete from `student marks`.`student` where `Roll Number`="+roll+" and `Contact Details`="+contact+";"
    try:
        cursor.execute(s1)
        conn.commit()
        print("Data successfully Deleted")
    except:
        conn.rollback()
        print("Deletion Error")

def update_data():
    name=input("Enter Student's Name: ")
    roll=input("Enter roll number: ")
    gender=input("Enter gender: ")
    contact=input("Enter Contact details: ")
    marks=int(input("Enter marks: "))
    email=input("Enter email id: ")
    grade=int(input("Enter grade: "))
    subjects=int(input("Enter total subjects"))
    per=marks/subjects
    s1="UPDATE `student` SET `Name`="+name+",`Gender`="+gender+",`Total Marks`="+marks+",`Email`="+email+",`Grade`="+grade+", `Percentage`="+per+" where `Roll Number`="+roll+" and `Contact Details`="+contact+";"
    try:
        cursor.execute(s1)
        conn.commit()
        print("Data successfully updated")
    except:
        conn.rollback()
        print("Updation Error")

choice=int(input("Enter \n 1. Insertion \n 2.Deletion on basis of Roll No. and contact number \n 3.Updation on basis of Roll No. and contact number"))
if(choice==1):
    insert_details()
elif(choice==2):
    delete_data()
elif(choice==3):
    update_data()

