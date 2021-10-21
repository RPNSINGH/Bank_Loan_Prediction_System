
import sys
from tkinter import  *
from tkinter import messagebox
from tkinter.ttk import Combobox
import time
import random
#from PIL import ImageTk,Image
import pandas as pd
#import seaborn as sn
#import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
#from sklearn.metrics import confusion_matrix

l=LabelEncoder()
# *****************************    machine code    ***********************************
df=pd.read_csv('final_data.csv')
# ****************************        Data_Manipulation    *********************************
x=df.drop(["Loan_ID","Loan_Status"],axis=1)
y=df.Loan_Status
# #######################  Machine lerning models ############
def dt_loan_pred(gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area):
    from sklearn.tree import DecisionTreeClassifier
    dt=DecisionTreeClassifier(random_state=0)
    dt.fit(x,y)
    d=dt.predict([[gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area]])
    return d
def rf_loan_pred(gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area):
    from sklearn.ensemble import RandomForestClassifier
    rf=RandomForestClassifier( n_estimators=500)
    rf.fit(x,y)
    r=rf.predict([[gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area]])
    return r
# ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ TKINTER ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻   
m=Tk()
m.configure(background='#EBDEF0')
m.title('MY_PROJECT ')
m.geometry("1600x800+0+0")
# functions and variables
income=IntVar()
cinc=IntVar()
amount=IntVar()
term=IntVar()
####################   DECISION TREE WINDOW ##############
def dt_window():
    check=Toplevel()
    check.geometry("400x400+200+120")
    check.title("Approval_Status")
    l=Label(check,text="Loan_Approval_Status ↓↓",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw').pack(side=TOP)
    b1=Button(check,text="BACK",command=check.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',25,'bold'),          width=20).pack(side=BOTTOM)  
    t=Text(check,height=5,width=25)
    t.pack()
    income=int(e1.get())
    cinc=int(e2.get())
    amt=int(e3.get())
    term=int(e4.get())
    gender=v1.get()
    married=v2.get()
    dependent=int(vc.get())
    education=v4.get()
    credit_his=v5.get()
    proper_area=v6.get()
    slfemp=int(v7.get())
    
    pred=dt_loan_pred(gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area)
    pred=list(pred)[0]
    pred=int(pred)
    if pred==1:
        approve="Approved"
    else:
        approve="Not Approved"
    
    t.insert(END,approve)
####################   RANDOM FOREST ALGORITHOM WINDOW ##############   
def rfa_window():
    check=Toplevel()
    check.geometry("400x400+200+200")
    check.title("Approval_Status")
    l=Label(check,text="Loan_Approval_Status ↓↓",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw').pack(side=TOP)
    button=Button(check,text="BACK",command=check.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',25,'bold'),          width=20).pack(side=BOTTOM)  
    t=Text(check,height=5,width=25)
    t.pack()
    income=int(e1.get())
    cinc=int(e2.get())
    amt=int(e3.get())
    term=int(e4.get())
    gender=v1.get()
    married=v2.get()
    dependent=int(vc.get())
    education=v4.get()
    credit_his=v5.get()
    proper_area=v6.get()
    slfemp=int(v7.get())
    
    pred=rf_loan_pred(gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area)
    pred=list(pred)[0]
    pred=int(pred)
#     print(pred)
#     print("ra=",gender,married,dependent,education,slfemp,income,cinc,amt,term,credit_his,proper_area)
    if pred==1:
        approve="Approved"
    else:
        approve="Not Approved"
    
    t.insert(END,approve)
#################  BUTTON  COMMANDS  ####################
def reset():
    appno.set('')
    income.set('')
    amount.set('')
    term.set('')

def call():
    mess = messagebox.askyesno("चेतावनी", "क्या आपको यकीन है ?")
    if (mess):
        m.destroy()
################# MENU COMMANDS FOR NEW WINDOW
def introduction():
    intro=Toplevel()
    intro.geometry("800x600+120+100")
    intro.title("Introduction")
    button=Button(intro,text="BACK",command=intro.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',14,'bold'),          width=5).pack(side=BOTTOM)
def project():
    proj=Toplevel()
    proj.geometry("1500x750")
    proj.title("About_Project")
    button=Button(proj,text="BACK",command=proj.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',16,'bold'),          width=5).pack(side=BOTTOM)
def mentor():
    ment=Toplevel()
    ment.geometry("1200x650")
    ment.title("About_Mentor")
    button=Button(ment,text="BACK",command=ment.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',16,'bold'),          width=5).pack(side=BOTTOM)
def developers():
    dev=Toplevel()
    dev.geometry("1200x650")
    dev.title("About_Developers")
    button=Button(dev,text="BACK",command=dev.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',16,'bold'),          width=5).pack(side=BOTTOM)
def college():
    clg=Toplevel()
    clg.geometry("1600x800")
    clg.title("About_College")
    button=Button(clg,text="BACK",command=clg.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',16,'bold'),          width=5).pack(side=BOTTOM)
def gcet():
    gc=Toplevel()
    gc.geometry("1200x650")
    gc.title("GCET_GALLERY")
    button=Button(gc,text="BACK",command=gc.destroy,padx=4,pady=6,bd=6,fg='black',font=('arial',16,'bold'),          width=5).pack(side=BOTTOM)
#creating drop down menues.↓↓
main_menu=Menu(m)
m.config(menu=main_menu)
firstMenu=Menu(main_menu)
viewMenu=Menu(main_menu)
exitMenu=Menu(main_menu)

main_menu.add_cascade(label="Menu",menu=firstMenu)
firstMenu.add_command(label="Intro",font=('arial',12,'bold'),command=introduction)# here we can use (command=something) and we can derive something above.
firstMenu.add_separator()
about_menu=Menu(firstMenu)
firstMenu.add_cascade(label="About",font=('arial',12,'bold'),menu=about_menu)
about_menu.add_command(label="About_Project",font=('arial',10,'bold'),command=project)
about_menu.add_separator()
about_menu.add_command(label="About_Mentor",font=('arial',10,'bold'),command=mentor)
about_menu.add_separator()
about_menu.add_command(label="About_Developers",font=('arial',10,'bold'),command=developers)
about_menu.add_separator()
about_menu.add_command(label="About_College",font=('arial',10,'bold'),command=college)

main_menu.add_cascade(label="View",menu=viewMenu)
viewMenu.add_command(label="GCET",font=('arial',12,'bold'),command=gcet)

main_menu.add_cascade(label="Exit",command=call)

#********************  FRAMES    ***********************
top=Frame(m,height=40,width=1600,relief=SUNKEN,bg='#EBDEF0')
top.pack(side=TOP)
f1=Frame(m,height=750,width=1000,relief=SUNKEN,bg='#EBDEF0')
f1.pack(side=LEFT)
f2=Frame(m,height=750,width=600,relief=SUNKEN,bg='#EBDEF0')
f2.pack()
#********************   TIME    ***********************
#localtime=time.asctime(time.localtime(time.time()))
def get_time():
    time_string=time.strftime("%I:%M:%S %p")
    clock.config(text=time_string)
    clock.after(200,get_time)
clock=Label(top,font=("time",20,"bold"),bg="#EBDEF0")
get_time() 
#********************  title and time   ***********************
lblinfo=Label(top,font=('arial',50,'bold'),text="USER'S INPUT",              fg='Steel Blue',bg='#EBDEF0',anchor='w',bd=10)
lblinfo.grid(row=0)

clock.grid(row=1)
# lblinfo=Label(top,text=get_time(),\
#               anchor='w',bg='#EBDEF0')

########  ☺ ☻ labels  ♫  ↓↓
lblincome=Label(f1,text="Applicant's_Income :",font=('arial',16,'bold'),bd=10,            bg='#EBDEF0',anchor='w',fg='Steel Blue')
lblincome.grid(row=0,sticky='nw')
e1=Entry(f1,font=('arial',16,'bold'),bd=10,         justify='right',textvariable=income,insertwidth=4)
e1.grid(row=0,column=1)

lblcinc=Label(f1,text="CoApplicant's_Income :",font=('arial',16,'bold'),                bd=10, bg='#EBDEF0',anchor='nw',fg='Steel Blue')
lblcinc.grid(row=1,column=0,sticky='nw')
e2=Entry(f1,font=('arial',16,'bold'),bd=10,         justify='right',textvariable=cinc,insertwidth=4)
e2.grid(row=1,column=1)

lblamount=Label(f1,text='Loan_Amount :',font=('arial',16,'bold'),                bd=10, bg='#EBDEF0',anchor='nw',fg='Steel Blue')
lblamount.grid(row=2,column=0,sticky='nw')
e3=Entry(f1,font=('arial',16,'bold'),bd=10,         justify='right',textvariable=amount,insertwidth=4)
e3.grid(row=2,column=1)

lblterm=Label(f1,text='Loan_Amount_Term :',font=('arial',16,'bold'),                bd=10, bg='#EBDEF0',anchor='nw',fg='Steel Blue')
lblterm.grid(row=3,column=0,sticky='nw')
e4=Entry(f1,font=('arial',16,'bold'),bd=10 ,         justify='right',textvariable=term,insertwidth=4)
e4.grid(row=3,column=1)
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻   radio buttons   ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ 
v1=IntVar()
l1=Label(f1,text="Gender : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l1.grid(row=4,column=0,sticky='nw')
Radiobutton(f1,text="Male",variable=v1,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=4,column=1,sticky=W)
Radiobutton(f1,text="Female",variable=v1,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=4,column=2,sticky=W)
v2=IntVar()
l2=Label(f1,text="Married : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l2.grid(row=5,column=0,sticky='nw')
Radiobutton(f1,text="Yes",variable=v2,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=5,column=1,sticky=W)
Radiobutton(f1,text="No",variable=v2,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=5,column=2,sticky=W)

l3=Label(f1,text="Dependents : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l3.grid(row=6,column=0,sticky='nw')
Depen=list(range(0,10))
vc=IntVar()
combo=Combobox(f1,values=Depen,height=4,font=('arial',10,'bold'))
combo.set("Select")
combo.grid(row=6,column=1,sticky=W)
v4=IntVar()
l4=Label(f1,text="Education : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l4.grid(row=7,column=0,sticky='nw')
Radiobutton(f1,text="Graduated",variable=v4,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=7,column=1,sticky=W)
Radiobutton(f1,text="Non_Graduate",variable=v4,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=7,column=2,sticky=W)
v5=IntVar()
l5=Label(f1,text="Credit_History : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l5.grid(row=8,column=0,sticky='nw')
Radiobutton(f1,text="0",variable=v5,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=8,column=1,sticky=W)
Radiobutton(f1,text="1",variable=v5,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=8,column=2,sticky=W)
v6=IntVar()
l6=Label(f1,text="Property_Area : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l6.grid(row=9,column=0,sticky='nw')
Radiobutton(f1,text="Rural",variable=v6,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=9,column=1,sticky=W)
Radiobutton(f1,text="Urban",variable=v6,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=9,column=2,sticky=W)
v7=IntVar()
l7=Label(f1,text="Self_Employed : ",bg='#EBDEF0',font=('arial',16,'bold'), bd=10,anchor='nw',fg='Steel Blue')#.grid(row=8)
l7.grid(row=10,column=0,sticky='nw')
Radiobutton(f1,text="0",variable=v7,value=0,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=10,column=1,sticky=W)
Radiobutton(f1,text="1",variable=v7,value=1,bg='#EBDEF0',font=('arial',16,'bold'),fg='Steel Blue').grid(row=10,column=2,sticky=W)
# #####################  buttons##########################
breset=Button(f1,text='RESET',padx=4,pady=5,bd=6,fg='black',font=('arial',25,'bold'),          width=12,command=reset,bg='#F1C40F').grid(row=11,column=1,sticky="S")
bcheck1=Button(f2,text='DT',padx=4,pady=15,bd=20,fg='white',font=('arial',20,'bold'),          width=5,height=10,command=dt_window,bg='#4A6A12').grid(row=1,sticky="s")
bcheck2=Button(f2,text='RFA',padx=4,pady=15,bd=20,fg='white',font=('arial',20,'bold'),          width=5,height=10,command=rfa_window,bg='#4A6A12').grid(row=1,column=2,sticky="s")

m.mainloop()


# ## 
