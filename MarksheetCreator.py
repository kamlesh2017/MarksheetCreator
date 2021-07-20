from tkinter import *
import mysql.connector;
#creating main window object
root=Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry(str(width)+"x"+str(height))
root.title("MarkSheet Creator")
root.configure(bg="purple")
#connectin with database which has students marks 
cn=mysql.connector.connect(host="localhost",user="root",password="shree hari",database="mydb")
cn.commit()
#function for creating marksheet
def Result(evar, e):
    cn=mysql.connector.connect(host="localhost",user="root",password="shree hari",database="mydb")
    cr=cn.cursor()
    roln=e.get()
    cr.execute("select * from student where rol_no=%s"%roln)
    table=cr.fetchall()    
    if(len(table)==1):
            row=table[0]
            name=row[1]
            hm=row[2]
            em=row[3]
            sm=row[4]
            ssm=row[5]
            scm=row[6]
            mm=row[7]

            percentage=round((hm+em+sm+ssm+scm+mm)/6,2)

            marksheet = Toplevel()
            marksheet.geometry("410x420")
            marksheet.title("Mark Sheet")
            Label(marksheet, text="Government Secondary School Amer, Jaipur").grid(row=2, columnspan=3, ipadx=70)
            Label(marksheet, text="Name: " + name+"    Roll No: "+roln).grid(row=3, columnspan=3, ipadx=70)
            Label(marksheet, text="Class: 10th").grid(row=4, columnspan=3, ipadx=70)
            hl = Label(marksheet, text="Hindi").grid(row=5, column=0)
            el = Label(marksheet, text="English").grid(row=6, column=0)
            sl = Label(marksheet, text="Sanskrit").grid(row=7, column=0)
            ssl = Label(marksheet, text="Social Science").grid(row=8, column=0)
            scl = Label(marksheet, text="Science").grid(row=9, column=0)
            ml = Label(marksheet, text="Maths").grid(row=10, column=0)

            hml = Label(marksheet, text=str(row[2])).grid(row=5, column=2)
            eml = Label(marksheet, text=str(row[3])).grid(row=6, column=2)
            sml = Label(marksheet, text=str(row[4])).grid(row=7, column=2)
            ssml = Label(marksheet, text=str(row[5])).grid(row=8, column=2)
            scml = Label(marksheet, text=str(row[6])).grid(row=9, column=2)
            mml = Label(marksheet, text=str(row[7])).grid(row=10, column=2)
            Label(marksheet, text="Percentage: " + str(percentage)).grid(row=13, columnspan=3, ipadx=70)

            if percentage >= 60:
                Label(marksheet, text="Division: First").grid(row=14, columnspan=3, ipadx=70)
                Label(marksheet, text="Result: Pass").grid(row=15, columnspan=3, ipadx=70)
            elif percentage >= 47:
                Label(marksheet, text="Division: Second").grid(row=14, columnspan=3, ipadx=70)
                Label(marksheet, text="Result: Pass").grid(row=15, columnspan=3, ipadx=70)
            elif percentage >= 36:
                Label(marksheet, text="Division: Third").grid(row=14, columnspan=3, ipadx=70)
                Label(marksheet, text="Result: Pass").grid(row=15, columnspan=3, ipadx=70)
            else:
                Label(marksheet, text="Result: Fail").grid(row=14, columnspan=3, ipadx=70)
            evar.set("")
    else:
        top = Toplevel()
        top.title("Errror")
        Label(top, text="Roll Number does'nt Exists").pack()
    cr.close()
    cn.commit()
    return
#function for taking student's roll number and creating marksheet
def StudentResult():
    top=Toplevel()
    top.title("Details")
    top.geometry("300x300")
    Label(top,text="Roll Number:").grid(row=0,column=0)
    evar=StringVar()
    e=Entry(top,textvariable=evar)
    e.grid(row=0,column=1)
    b=Button(top,text="Result",command=lambda: Result(evar, e))
    b.grid(row=1,column=1)
    return
#function for entering a student's record in a record table student
def submit(namevar,rolvar,hm,em,sm,ssm,scm,mm,role,namee,he,ee,se,sse,sce,me):
    roln = int(role.get())
    name = namee.get()
    hmm = int(he.get())
    emm = int(ee.get())
    smm = int(se.get())
    ssmm = int(sse.get())
    scmm = int(sce.get())
    mmm = int(me.get())

    cn=mysql.connector.connect(host="localhost",user="root",password="shree hari",database="mydb")
    cr=cn.cursor()
    cr.execute("select * from student")
    table=cr.fetchall()
    flag=0;
    for row in table:
        if(row[0]==roln):
            flag=1
            break
    
    if flag==0:
        cr.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(roln,name,hmm,emm,smm,ssmm,scmm,mmm))
        cr.close()
        cn.commit()
    else:
        cr.close()
        cn.commit()
        top=Toplevel()
        top.title("Error")
        Label(top, text="Student Entry already Exists").pack()
    namevar.set("")
    rolvar.set("")
    hm.set("")
    em.set("")
    sm.set("")
    ssm.set("")
    scm.set("")
    mm.set("")
    return
#function for taking marks and other information by user about a student and Entry in student table
def StudentEntry():

    master=Toplevel()
    master.geometry("300x330")
    master.title("Student Entry")
    master.resizable(0,0)
    namel = Label(master, text="Name")
    namevar = StringVar()
    namee = Entry(master, textvariable=namevar)

    rol=Label(master,text="Roll Number")
    rolvar=StringVar()
    role=Entry(master,textvariable=rolvar)

    hl = Label(master, text="Hindi")
    el = Label(master, text="English")
    sl = Label(master, text="Sanskrit")
    ssl = Label(master, text="Social Science")
    scl = Label(master, text="Science")
    ml = Label(master, text="Maths")

    hm = StringVar()
    em = StringVar()
    sm = StringVar()
    ssm = StringVar()
    scm = StringVar()
    mm = StringVar()

    he = Entry(master, textvariable=hm)
    ee = Entry(master, textvariable=em)
    se = Entry(master, textvariable=sm)
    sse = Entry(master, textvariable=ssm)
    sce = Entry(master, textvariable=scm)
    me = Entry(master, textvariable=mm)

    sb = Button(master, text="Submit", command=lambda: submit(namevar,rolvar,hm,em,sm,ssm,scm,mm,role,namee,he,ee,se,sse,sce,me))

    namel.grid(row=0, column=0)
    rol.grid(row=1,column=0)
    hl.grid(row=2, column=0)
    el.grid(row=3, column=0)
    sl.grid(row=4, column=0)
    ssl.grid(row=5, column=0)
    scl.grid(row=6, column=0)
    ml.grid(row=7, column=0)

    namee.grid(row=0, column=1)
    role.grid(row=1, column=1)
    he.grid(row=2, column=1)
    ee.grid(row=3, column=1)
    se.grid(row=4, column=1)
    sse.grid(row=5, column=1)
    sce.grid(row=6, column=1)
    me.grid(row=7, column=1)

    sb.grid(row=8, column=1)
    return
#function for Edit a student's record in student record table
def Edit(namevar, rolvar, hm, em, sm, ssm, scm, mm, role, namee, he, ee, se, sse, sce, me):
    roln = int(role.get())
    name = namee.get()
    hmm = int(he.get())
    emm = int(ee.get())
    smm = int(se.get())
    ssmm = int(sse.get())
    scmm = int(sce.get())
    mmm = int(me.get())

    cn=mysql.connector.connect(host="localhost",user="root",password="shree hari",database="mydb")
    cr=cn.cursor()
    cr.execute("select * from student")
    table=cr.fetchall()
    flag=0;
    for row in table:
        if(row[0]==roln):
            flag=1
            break
    if(flag==1):
        cr.execute("update student set name=%s,hindi=%s,english=%s,sanskrit=%s,social_science=%s,science=%s,math=%s where rol_no=%s",(name,hmm,emm,smm,ssmm,scmm,mmm,roln)) 
        top=Toplevel()
        top.title("Message")
        Label(top,text="Student Entry Edited").pack()
    else:
        top = Toplevel()
        top.title("Message")
        Label(top, text="Student does'nt exists").pack()
    cr.close()
    cn.commit()
    namevar.set("")
    rolvar.set("")
    hm.set("")
    em.set("")
    sm.set("")
    ssm.set("")
    scm.set("")
    mm.set("")
    return
#function for taking marks and other informetion of a student and edit it in a table
def EditEntry():
    master = Toplevel()
    master.geometry("300x330")
    master.title("Student Entry")
    master.resizable(0, 0)

    namel = Label(master, text="Name")
    namevar = StringVar()
    namee = Entry(master, textvariable=namevar)

    rol = Label(master, text="Roll Number")
    rolvar = StringVar()
    role = Entry(master, textvariable=rolvar)

    hl = Label(master, text="Hindi")
    el = Label(master, text="English")
    sl = Label(master, text="Sanskrit")
    ssl = Label(master, text="Social Science")
    scl = Label(master, text="Science")
    ml = Label(master, text="Maths")

    hm = StringVar()
    em = StringVar()
    sm = StringVar()
    ssm = StringVar()
    scm = StringVar()
    mm = StringVar()

    he = Entry(master, textvariable=hm)
    ee = Entry(master, textvariable=em)
    se = Entry(master, textvariable=sm)
    sse = Entry(master, textvariable=ssm)
    sce = Entry(master, textvariable=scm)
    me = Entry(master, textvariable=mm)

    sb = Button(master, text="Edit",command=lambda: Edit(namevar, rolvar, hm, em, sm, ssm, scm, mm, role, namee, he, ee, se, sse, sce, me))

    namel.grid(row=0, column=0)
    rol.grid(row=1, column=0)
    hl.grid(row=2, column=0)
    el.grid(row=3, column=0)
    sl.grid(row=4, column=0)
    ssl.grid(row=5, column=0)
    scl.grid(row=6, column=0)
    ml.grid(row=7, column=0)

    namee.grid(row=0, column=1)
    role.grid(row=1, column=1)
    he.grid(row=2, column=1)
    ee.grid(row=3, column=1)
    se.grid(row=4, column=1)
    sse.grid(row=5, column=1)
    sce.grid(row=6, column=1)
    me.grid(row=7, column=1)

    sb.grid(row=8, column=1)
    return

#function for deliting a student's record 
def Delete(evar,e):
    roln=e.get()
    cn=mysql.connector.connect(host="localhost",user="root",password="shree hari",database="mydb")
    cr=cn.cursor()
    cr.execute("select * from student where rol_no=%s"%roln)
    table=cr.fetchall()
    if len(table)==1:
        cr.execute("delete from student where rol_no=%s"%roln)
        top=Toplevel()
        top.title("Message")
        Label(top,text="Student Entry Deleted").pack()
    else:
        top = Toplevel()
        top.title("Message")
        Label(top, text="Please enter the correct Roll Number").pack()
    evar.set("")
    cr.close()
    cn.commit()
    return
#function for taking student roll number and delete the student record
def DeleteEntry():
    top = Toplevel()
    top.title("")
    top.geometry("300x300")
    Label(top, text="Roll Number:").grid(row=0, column=0)
    evar = StringVar()
    e = Entry(top, textvariable=evar)
    e.grid(row=0, column=1)
    b = Button(top, text="Delete", command=lambda: Delete(evar, e))
    b.grid(row=1, column=1)
    return

def CallAbout():
    top=Toplevel()
    top.title("")
    top.geometry("500x220")
    message=Message(top,text='''
    This is a simple application for ceating the marksheets of students of a class.
    All data of class' students is given by user such as student name, roll number and marks in all subjects.
    This all data is internally stored in a database "mydb" by this application otomatically for storing students' data for long time period.
    User can make marksheet of any student by student's roll number which has been registered in "mydb" database by user.
    ''')
    message.pack()
    return

b1=Button(root, text="Student Result", bg="green", fg="white",width=20,height=1,font=("Arial Bold", 20), command=StudentResult, highlightcolor="blue")
b2=Button(root, text="Student Entry",bg="green", fg="white",width=20,height=1,font=("Arial Bold", 20),command=StudentEntry)
b3=Button(root, text="Edit Student Entry", bg="green", fg="white",width=20,height=1,font=("Arial Bold", 20),command=EditEntry)
b4=Button(root, text="Delete Student Entry", bg="green", fg="white",width=20,height=1,font=("Arial Bold", 20),command=DeleteEntry)
b5=Button(root, text="Exit", bg="green", fg="white",width=20,height=1,font=("Arial Bold", 20),command=root.destroy)

b1.place(relx=0.35, rely=0.2)
b2.place(relx=0.35, rely=0.3)
b3.place(relx=0.35, rely=0.4)
b4.place(relx=0.35, rely=0.5)
b5.place(relx=0.35, rely=0.6)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Entry',command=StudentEntry)
filemenu.add_command(label='Result',command=StudentResult)
filemenu.add_command(label='Edit Entry', command=EditEntry)
filemenu.add_command(label='Delete Entry',command=DeleteEntry)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=CallAbout)

root.mainloop()
