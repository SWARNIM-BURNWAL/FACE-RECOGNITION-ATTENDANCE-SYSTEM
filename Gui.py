import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("")
my_w.title("ATTENDANCE DATA")
my_w.configure(background="white") 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  passwd="swarnim",
  database="attendance"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM attendance")
e=Label(my_w,width=10,text='FULLNAME',borderwidth=2, relief='ridge',anchor='n',fg='red')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='DATETIME',borderwidth=2, relief='ridge',anchor='n', fg='red')
e.grid(row=0,column=1)
i=1 
for attendance in mycursor: 
    for j in range(len(attendance)):
      
        e = Label(my_w,width=20, text=attendance[j],borderwidth=2.5,relief='sunken', anchor="n", font="timesnewroman", fg='black')
        
        
        
        e.grid(row=i, column=j) 
    i=i+1
my_w.mainloop()


