from tkinter import *
from tkinter import messagebox
import pymysql

def insert():
    nm = t1.get()
    rno = t2.get()
    m1 = t3.get()
    m2 = t4.get()
    m3 = t5.get() 
    rno = int(rno)
    m1 = int(m1)
    m2 = int(m2)
    m3 = int(m3)
    tot = m1 + m2 + m3
    avg = tot / 3
    if avg >= 60:
        remark = "First Class"
    elif avg >= 50:
        remark = "Pass"
    else:
        remark = "Fail"
    t6.delete(0, END)
    t6.insert(0, tot)
    t7.delete(0, END)
    t7.insert(0, avg)
    t8.delete(0, END)
    t8.insert(0, remark)
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    stmt = "INSERT INTO stude_res(stud_nm, stud_rno, stud_m1, stud_m2, stud_m3, stud_tot, stud_avg,stud_remark) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
    cursor.execute(stmt, (nm, rno, m1, m2, m3, tot, avg,remark))
    db.commit()
    cursor.close() 
    messagebox.showinfo("Insert Box", "Record Inserted Successfully")
    
def search():
    rno = t9.get()
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    stmt = "SELECT * FROM stude_res WHERE stud_rno = %s"
    cursor.execute(stmt, (rno,))
    row = cursor.fetchone()
    if row:
        clear()
        t1.insert(0, row[0])
        t2.insert(0, row[1])
        t3.insert(0, row[2])
        t4.insert(0, row[3])
        t5.insert(0, row[4])
        t6.insert(0, row[5])
        t7.insert(0, row[6])
        t8.insert(0, row[7])
        messagebox.showinfo("Search Box", "Record Successfully Found")
    else:
        clear()
        messagebox.showinfo("Search", "Record Not Found")
    cursor.close()
    
def update():
    nm = t1.get()
    rno = t2.get()
    remark = t3.get()
    rno = int(rno)
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    stmt = "UPDATE stude_res SET stud_nm=%s, stud_remark=%s WHERE stud_rno=%s"
    cursor.execute(stmt, (nm, remark, rno))
    db.commit()
    cursor.close()
    messagebox.showinfo("Update Box", "Record Updated Successfully")

def delete():
    rno = t2.get()
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM stude_res WHERE stud_rno=%s", (rno,))
    row = cursor.fetchone()
    if row:
        stmt = "DELETE FROM stude_res WHERE stud_rno=%s"
        cursor.execute(stmt, (rno,))
        db.commit()
        messagebox.showinfo("Delete Box", "Record Deleted Successfully")
    else:
        messagebox.showinfo("Delete Box", "Record Not Found")
    cursor.close()
    clear()

def clear():
    t1.delete(0, "end")
    t2.delete(0, "end")
    t3.delete(0, "end")
    t4.delete(0, "end")
    t5.delete(0, "end")
    t6.delete(0, "end")
    t7.delete(0, "end")
    t8.delete(0, "end")
    t9.delete(0, "end")

def cul():
    m1 = t3.get()
    m2 = t4.get()
    m3 = t5.get()
    m1 = int(m1)
    m2 = int(m2)
    m3 = int(m3)
    tot = m1 + m2 + m3
    avg = tot / 3
    if avg >= 60:
        remark = "First Class"
    elif avg >= 50:
        remark = "Pass"
    else:
        remark = "Fail"
    t6.delete(0, END)
    t6.insert(0, tot)
    t7.delete(0, END)
    t7.insert(0, avg)
    t8.delete(0, END)
    t8.insert(0, remark)

root = Tk()
root.title("Student Result")
label = Label(root, text="*Student Result*",fg='black',bg='wheat')
label.config(font=("Helvetica", 17, "bold"))
label.pack()
root.configure(background='wheat')
label_text=StringVar();
root.resizable(0, 0)
root.geometry("900x400+200+100")

l1 = Label(root, text="Name",bg='tan')
l1.place(x=140, y=36)
t1 = Entry(root, width=15)
t1.place(x=250, y=36)

l2 = Label(root, text="Roll No",bg='tan')
l2.place(x=140, y=60)
t2 = Entry(root, width=15)
t2.place(x=250, y=60)

l3 = Label(root, text="Marks1",bg='tan')
l3.place(x=140, y=85)
t3 = Entry(root, width=15)
t3.place(x=250, y=85)

l4 = Label(root, text="Marks2",bg='tan')
l4.place(x=140, y=110)
t4 = Entry(root, width=15)
t4.place(x=250, y=110)

l5 = Label(root, text="Marks3",bg='tan')
l5.place(x=140, y=135)
t5 = Entry(root, width=15)
t5.place(x=250, y=135)

l6 = Label(root, text="Total",bg='tan')
l6.place(x=140, y=160)
t6 = Entry(root, width=15)
t6.place(x=250, y=160)

l7 = Label(root, text="Average",bg='tan')
l7.place(x=140, y=185)
t7 = Entry(root, width=15)
t7.place(x=250, y=185)

l8 = Label(root, text="Remark",bg='tan')
l8.place(x=140, y=210)
t8 = Entry(root, width=15)
t8.place(x=250, y=210)


b1 = Button(root, text="Insert", width=7,bg='Orange',command=insert)
b1.place(x=140, y=240)

b2 = Button(root, text="Update", width=7,bg='Orange', command=update)
b2.place(x=240, y=240)

b3 = Button(root, text="Search", width=7,bg='Orange', command=search)
b3.place(x=340, y=240)
t9=Entry(root,width=8)
t9.place(x=340,y=280)


b4 = Button(root, text="Delete", width=7,bg='Orange', command=delete)
b4.place(x=440, y=240)

b5 = Button(root, text="Clear", width=7,bg='Orange', command=clear)
b5.place(x=540, y=240)

b6 = Button(root, text="Calculate", width=7,bg='Orange', command=cul)
b6.place(x=640, y=240)

root.mainloop()
