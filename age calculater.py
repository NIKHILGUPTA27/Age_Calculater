from tkinter import*
from datetime import datetime
HU=Tk()
HU.title("My Page")
def age_cal():
    dob=E1.get()
    dob=datetime.strptime(dob, "%d %m %Y")
    difference=datetime.now() - dob
    days=difference.days
    year=days//365
    month=(days % 365)//30
    day=(days % 365)%30
    result1.set(year)
    result2.set(month)
    result3.set(day)
    
B1=Button(HU,text=" Date of Birth:- ",font=("calibri",15,"bold"),bg="pink",fg="red",bd=8,width=13,command=age_cal)
B1.grid(row=1,column=0)

E1=Entry(HU,font=("calibri",22,"bold"),bg="pink",fg="Blue",bd=8,width=20)
E1.grid(row=1,column=1)

L1=Label(HU,text=" Year:- ",font=("calibri",20,"bold"),fg="green")
L1.grid(row=2,column=0)

L2=Label(HU,text=" Month:- ",font=("calibri",20,"bold"),fg="green")
L2.grid(row=3,column=0)

L3=Label(HU,text=" Days:- ",font=("calibri",20,"bold"),fg="green")
L3.grid(row=4,column=0)

result1 = StringVar()
result2 = StringVar()
result3 = StringVar()


Result1=Entry(HU,textvariable=result1,font=("calibri",22,"bold"),bg="pink",fg="blue",bd=10,width=20)
Result1.grid(row=2,column=1)
Result2=Entry(HU,textvariable=result2,font=("calibri",22,"bold"),bg="pink",fg="blue",bd=10,width=20)
Result2.grid(row=3,column=1)
Result3=Entry(HU,textvariable=result3,font=("calibri",22,"bold"),bg="pink",fg="blue",bd=10,width=20)
Result3.grid(row=4,column=1)
HU.mainloop()
