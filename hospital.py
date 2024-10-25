
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
window=Tk()
window.geometry('1800x1200')

canvas=Canvas(window,width=1600,height=900)
image1=ImageTk.PhotoImage(Image.open("computer_engineer-compare-page.png"))
canvas.create_image(0,50,anchor=NW,image=image1)
canvas.place(x=0,y=50)

window.title("Hospital Management System")
frame=Frame(window,width=1600,height=100,bg="light blue")
frame.place(x=0,y=0)
l1=Label(window,text="HOSPITAL MANAGEMENT SYSTEM",bg="light blue",font=('calibre',40,'bold'))
l1.place(x=330,y=20)

l2=Label(window,text="USERNAME",font=('calibre',30,'bold'),bg="light blue")
l2.place(x=640,y=220)
global user,pwd
global e1,e2
user=StringVar()
pwd=StringVar()
e1=Entry(window,textvar='user',width=20,font=('Helvetica',20,'bold'))
e1.place(x=610,y=290)

l3=Label(window,text="PASSWORD",font=('calibre',30,'bold'),bg="light blue")
l3.place(x=640,y=360)
e2=Entry(window,textvar='pwd',width=20,font=('Helvetica',20,'bold'))
e2.place(x=610,y=430)


from tkinter import *
from wb import doctor
from wc import patient
from wd import appointment
from PIL import Image,ImageTk

def login():
    a=e1.get()
    b=e2.get()
    if a=="aman" and b=="1234":

        window1=Tk()
        window1.geometry('1600x1100')



        window1.title("Hospital Management System")
        frame1=Frame(window1,width=1600,height=100,bg="light blue")
        frame1.place(x=0,y=0)
        la=Label(window1,text="ADMIN PANEL",bg="light blue",font=('calibre',35,'bold'))
        la.place(x=620,y=20)


        b1=Button(window1,text="DOCTOR",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=doctor)
        b1.place(x=350,y=280)

        b2=Button(window1,text="PATIENT",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=patient)
        b2.place(x=900,y=280)

        b3=Button(window1,text="APPOINTMENT",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=appointment)
        b3.place(x=350,y=500)

        b4=Button(window1,text="ABOUT US",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15)
        b4.place(x=900,y=500)
        window.destroy()
    else:
        messagebox.showinfo("Information","Your Username and Password is Wrong")


b=Button(window,text="LOGIN",bg="light blue",bd=15,font=('calibre',18,'bold'),width=10,command=login)
b.place(x=660,y=510)


from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
def doctor():
    global window3
    window3=Tk()
    window3.geometry('1800x1200')
    window3.title("Hospital Management System")
    frame2=Frame(window3,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window3,text="MANAGE DOCTOR",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lc=Label(window3,text="NAME",font=('calibre',20,'bold'))
    lc.place(x=280,y=200)

    ld=Label(window3,text="SPECIALIZATION",font=('calibre',20,'bold'))
    ld.place(x=280,y=250)

    le=Label(window3,text="CONTACT",font=('calibre',20,'bold'))
    le.place(x=280,y=300)

    lf=Label(window3,text="ADDRESS",font=('calibre',20,'bold'))
    lf.place(x=1200,y=200)

    global Name, specialization,contact,address
    Name=StringVar()
    specialization=StringVar()
    contact=StringVar()
    address=StringVar()
    global ea,eb,ec,ed
    ea=Entry(window3,textvar="Name",width=20,font=('calibre',18,'bold'))
    ea.place(x=550,y=200)

    eb=Entry(window3,textvar="specialization",width=20,font=('calibre',18,'bold'))
    eb.place(x=550,y=250)

    ec=Entry(window3,textvar="contact",width=20,font=('calibre',18,'bold'))
    ec.place(x=550,y=300)

    ed=Entry(window3,textvar="address",width=20,font=('calibre',18,'bold'))
    ed.place(x=900,y=200)





    ba=Button(window3,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    ba.place(x=0,y=1)

    bb=Button(window3,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=doctor1)
    bb.place(x=300,y=500)

    bc=Button(window3,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bc.place(x=530,y=500)

    bd=Button(window3,text="UPDATE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=update)
    bd.place(x=760,y=500)

    be=Button(window3,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    be.place(x=990,y=500)
    window3.mainloop()




def back():
    window3.destroy()




def doctor1():
    a=ea.get()
    b=eb.get()
    c=ec.get()
    d=ed.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO doctor(name,specialization,contact,address)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ea.delete(first=0,last=20)
    eb.delete(first=0,last=20)
    ec.delete(first=0,last=20)
    ed.delete(first=0,last=20)


def show():

    window6=Tk()
    window6.geometry('1800x1200')

    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.column("1",width=200)
    tree.column("2",width=200)
    tree.column("3",width=200)
    tree.column("4",width=200)

    tree.heading(1,text="Name")
    tree.heading(2,text="Specialization")
    tree.heading(3,text="Contact")
    tree.heading(4,text="Address")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Doctors",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM doctor")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)




def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")

    b=ea.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM doctor WHERE name=%s"
    val=(b,)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()


def update():
    b=ea.get()
    c=ec.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="UPDATE doctor SET contact=%s WHERE name=%s"
    val=(c,b)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()

from tkinter import *
import mysql.connector
from tkinter import messagebox
def patient():
    global window4
    window4=Tk()
    window4.geometry('1800x1200')
    window4.title("Hospital Management System")
    frame2=Frame(window4,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window4,text="MANAGE PATIENT",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window4,text="NAME",font=('calibre',20,'bold'))
    lg.place(x=280,y=200)

    lh=Label(window4,text="GENDER",font=('calibre',20,'bold'))
    lh.place(x=280,y=250)

    li=Label(window4,text="CONTACT",font=('calibre',20,'bold'))
    li.place(x=280,y=300)

    lj=Label(window4,text="ADDRESS",font=('calibre',20,'bold'))
    lj.place(x=280,y=350)

    lk=Label(window4,text="SEARCH",font=('calibre',20,'bold'))
    lk.place(x=1200,y=200)


    global Name,Gender,Contact,Address,Search
    Name=StringVar()
    Gender=StringVar()
    Contact=StringVar()
    Address=StringVar()
    Search=StringVar()
    global ef,eg,eh,ei,ej

    ef=Entry(window4,textvar="Name",width=20,font=('calibre',18,'bold'))
    ef.place(x=550,y=200)

    eg=Entry(window4,textvar="Gender",width=20,font=('calibre',18,'bold'))
    eg.place(x=550,y=250)

    eh=Entry(window4,textvar="Contact",width=20,font=('calibre',18,'bold'))
    eh.place(x=550,y=300)


    ei=Entry(window4,textvar="Address",width=20,font=('calibre',18,'bold'))
    ei.place(x=550,y=350)

    ej=Entry(window4,textvar="Search",width=20,font=('calibre',18,'bold'))
    ej.place(x=900,y=200)




    bf=Button(window4,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    bf.place(x=0,y=1)

    bg=Button(window4,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=patient1)
    bg.place(x=300,y=500)

    bh=Button(window4,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bh.place(x=530,y=500)

    bi=Button(window4,text="SEARCH",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=search)
    bi.place(x=760,y=500)

    bj=Button(window4,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    bj.place(x=990,y=500)


def back():
    window4.destroy()

def patient1():
    a=ef.get()
    b=eg.get()
    c=eh.get()
    d=ei.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO patient(Name,gender,contact,address)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ef.delete(first=0,last=20)
    eg.delete(first=0,last=20)
    eh.delete(first=0,last=20)
    ei.delete(first=0,last=20)
def show():

    window6=Tk()
    window6.geometry('1800x1200')
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.heading(1,text="Name")
    tree.heading(2,text="Gender")
    tree.heading(3,text="Contact")
    tree.heading(4,text="Address")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Patient",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM patient")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)



def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")
    b=ef.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM patient WHERE Name=%s"
    val=(b,)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()

def search():
    s=ej.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="SELECT * FROM patient WHERE Name=%s "
    val=(s,)
    cs.execute(sql,val)
    rows=cs.fetchall()
    for x in rows:
        a=x[0]
        b=x[1]
        c=x[2]
        d=x[3]
    if s==a:
        ef.insert(0,a)
        eg.insert(0,b)
        eh.insert(0,c)
        ei.insert(0,d)

    ej.delete(first=0,last=20)

from tkinter import *
import mysql.connector
from tkinter import messagebox
def appointment():
    global window5
    window5=Tk()
    window5.geometry('1800x1200')
    window5.title("Hospital Management System")
    frame2=Frame(window5,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window5,text="MANAGE APPOINTMENT",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window5,text="DOCTOR NAME",font=('calibre',20,'bold'))
    lg.place(x=280,y=200)

    lh=Label(window5,text="PATIENT NAME",font=('calibre',20,'bold'))
    lh.place(x=280,y=250)

    li=Label(window5,text="DATE",font=('calibre',20,'bold'))
    li.place(x=280,y=300)

    lj=Label(window5,text="TIME",font=('calibre',20,'bold'))
    lj.place(x=280,y=350)

    lk=Label(window5,text="SEARCH",font=('calibre',20,'bold'))
    lk.place(x=1200,y=200)


    global e1,e2,e3,ei,ek
    global search,doctor,patient,date,time
    doctor=StringVar()
    patient=StringVar()
    date=StringVar()
    time=StringVar()
    search=StringVar()
    e1=Entry(window5,textvar="doctor",width=20,font=('calibre',18,'bold'))
    e1.place(x=550,y=200)

    e2=Entry(window5,textvar="patient",width=20,font=('calibre',18,'bold'))
    e2.place(x=550,y=250)

    e3=Entry(window5,textvar="date",width=20,font=('calibre',18,'bold'))
    e3.place(x=550,y=300)

    ei=Entry(window5,textvar="time",width=20,font=('calibre',18,'bold'))
    ei.place(x=550,y=350)

    ek=Entry(window5,textvar="search",width=20,font=('calibre',18,'bold'))
    ek.place(x=900,y=200)




    bf=Button(window5,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    bf.place(x=0,y=1)

    bg=Button(window5,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=appointment1)
    bg.place(x=300,y=500)

    bh=Button(window5,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bh.place(x=530,y=500)

    bi=Button(window5,text="SEARCH",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=bitch)
    bi.place(x=760,y=500)

    bj=Button(window5,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    bj.place(x=990,y=500)


def back():
    window5.destroy()


def appointment1():

    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=ei.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO appointment(doctor,patient,date,time)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    e1.delete(first=0,last=20)
    e2.delete(first=0,last=20)
    e3.delete(first=0,last=20)
    ei.delete(first=0,last=20)

def show():
    window6=Tk()
    window6.geometry('1800x1200')
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.heading(1,text="Doctor")
    tree.heading(2,text="Patient")
    tree.heading(3,text="Date")
    tree.heading(4,text="Time")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Appointments",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM appointment")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)


def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")
    b=e2.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM appointment WHERE patient=%s"
    val=(b,)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()

def bitch():
    messagebox.askquestion("Confirmation","Are you sure want to search?")
    z=ek.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="SELECT * FROM appointment WHERE patient=%s "
    val=(z,)
    cs.execute(sql,val)
    rows=cs.fetchall()
    for x in rows:
        p=x[0]
        q=x[1]
        r=x[2]
        s=x[3]
    if z==q:
        e1.insert(0,p)
        e2.insert(0,q)
        e3.insert(0,r)
        ei.insert(0,s)