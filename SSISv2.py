#Jonathan Tinoy
#BSSTAT
#Simple Student Information System version 2

from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not name.get():
        t1.insert(END,"<>Name is required<>\n")
        a=1
    if not idno.get():
        t1.insert(END,"<>Idno is required<>\n")
        b=1
    if not course.get():
        t1.insert(END,"<>Course is required<>\n")
        c=1
    if not coursecode.get():
        t1.insert(END,"<>CourseCode is requrired<>\n")
        d=1
    if not yearlevel.get():
        t1.insert(END,"<>Yearlevel is required<>\n")
        e=1
    if not gender.get():
        t1.insert(END,"<>Gender is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,IDNO INTEGER,COURSE TEXT,COURSECODE TEXT,YEARLEVEL INTEGER,GENDER TEXT)")
                cur.execute("insert into STUDENTS values(?,?,?,?,?,?)",(student_name.get(),int(idno.get()),course.get(),int(coursecode.get()),yearlevel.get(),gender.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?",(int(roll_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,IDNO=?,COURSE=?,COURSECODE=?,YEARLEVEL=?,GENDER=? where ID=?",(name.get(),int(idno.get()),course.get(),int(coursecode.get()),yearlevel.get(),gender.get(),int(idno.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Simple Student Information System Version 2")
     
    name=StringVar()
    idno=StringVar()
    course=StringVar()
    coursecode=StringVar()
    yearlevel=StringVar()
    gender=StringVar()
    
    label1=Label(root,text="Name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Idno:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Course:")
    label3.place(x=0,y=60)

    label4=Label(root,text="CourseCode:")
    label4.place(x=0,y=90)

    label5=Label(root,text="Yearlevel:")
    label5.place(x=0,y=120)

    label6=Label(root,text="Gender:")
    label6.place(x=0,y=150)

    e1=Entry(root,textvariable=name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=idno)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=course)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=coursecode)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=yearlevel)
    e5.place(x=100,y=120)

    e6=Entry(root,textvariable=gender)
    e6.place(x=100,y=150)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD STUDENT",command=add_student,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_student,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLOSE",command=clse,width=40)
    b5.grid(row=15,column=0)


    root.mainloop()
