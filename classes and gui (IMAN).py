import tkinter as tk
import random
from tkinter import *
import time
from PIL import ImageTk
from signup import registration
import winsound
print("Welcome To System")
# winsound.PlaySound('filename', flag) 
winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME)  

gui=tk.Tk() 
gui.title('BANKING REGISTRY PANEL') 
gui.geometry('700x700+60+20')





#---------------------------------------------------------------------------------------------

def datasave():
    text=e1.get()+"\n"+e2.get()+"\n"+e3.get()+"\n"+e4.get()+"\n"+e5.get()+"\n"+e6.get()
    with open ("PRINT RECEIPT.txt",'w')as f:
        f.writelines(text)
text=Label(gui,text="BANKING REGISTRY PANEL",font=('Times New Roman','20'),width=50,fg='white',bg="#03506f")
text.grid(columnspan=50)

#---------------------------------------------------------------------------------------------

loanimg=ImageTk.PhotoImage(file="images/loanfinal.png")
loan_image=Label(gui,image=loanimg).place(x=600,y=300,width=85,height=85)

transactionimg=ImageTk.PhotoImage(file="images/transactionfinal.png")
transaction_image=Label(gui,image=transactionimg).place(x=500,y=300,width=85,height=85)

depositimg=ImageTk.PhotoImage(file="images/depositfinal.png")
deposit_image=Label(gui,image=depositimg).place(x=410,y=300,width=76,height=80)

#---------------------------------------------------------------------------------------------

#Graph Image


def graph():
      import matplotlib.pyplot as plt
      import pandas as pd
      df= pd.read_csv('currency_rates.csv')
      print (df)
      plt.title('Currency Rates')
      plt.xlabel('Countries')
      plt.ylabel('Rates')
      plt.xticks( rotation ='vertical')
      plt.plot(df.countries,df.rates,color='grey',marker="X",markerfacecolor='#03506f',linestyle='dashdot')
      plt.show()
      
ratesimg=ImageTk.PhotoImage(file="images/graph.png")
rates_image=Label(gui,image=ratesimg).place(x=460,y=500,width=150,height=170)

label_DataVis=Label(gui,text="Currency Rates Of Bank",font=("Goudy Old Style",15,"bold"),bg="#03506f",fg="white")
label_DataVis.place(x=460,y=430,width=220,height=50)

datagraph=Button(gui,padx=16,pady=8,bd=5,fg="black",font=('times' ,8,'bold'),width=3, text="Press", command=graph, activebackground='#79a3b1')
datagraph.place(x=620,y=500)

#---------------------------------------------------------------------------------------------

def analytics():
    
    import numpy as np
    import matplotlib.pyplot as plt


    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r**2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()

label_DataVis2=Label(gui,text="Individual Working Rates",font=("Goudy Old Style",15,"bold"),bg="#BDC8CC",fg="#03506f")
label_DataVis2.place(x=10,y=300,width=220,height=50)

datagraph2=Button(gui,padx=16,pady=8,bd=5,fg="black",font=('times' ,8,'bold'),width=3, text="Check", command=analytics, activebackground='#79a3b1')
datagraph2.place(x=250,y=300)


#---------------------------------------------------------------------------------------------
def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    # print(h,m,s)
    if int (h)>12 and int(m)>0:
        label_noon.config(text="PM")
    if int(h)>12:
        h=str((int(h)-12))
        
     
    label_hr.config(text=h)
    label_min.config(text=m)
    label_sec.config(text=s)

    label_hr.after(200,clock)

#---------------------------------------------------------------------------------------------------------
#Clock on page
    
label_hr=Label(gui,text="12",font=("Times new roman",15,"bold"),bg="#0875B7",fg="white")
label_hr.place(x=70,y=570,width=50,height=50)
              
label_hr2=Label(gui,text="HOUR",font=("Times new roman",10,"bold"),bg="#0875B7",fg="white")
label_hr2.place(x=70,y=630,width=50,height=30)

label_min=Label(gui,text="12",font=("Times new roman",15,"bold"),bg="#008ea4",fg="white")
label_min.place(x=130,y=570,width=50,height=50)
              
label_min2=Label(gui,text="MINUTE",font=("Times new roman",10,"bold"),bg="#008ea4",fg="white")
label_min2.place(x=130,y=630,width=50,height=30)

label_sec=Label(gui,text="12",font=("Times new roman",15,"bold"),bg="#0875B7",fg="white")
label_sec.place(x=190,y=570,width=50,height=50)
              
label_sec2=Label(gui,text="SECOND",font=("Times new roman",10,"bold"),bg="#0875B7",fg="white")
label_sec2.place(x=190,y=630,width=50,height=30)

label_noon=Label(gui,text="AM",font=("Times new roman",15,"bold"),bg="#df002a",fg="white")
label_noon.place(x=250,y=570,width=50,height=50)
              
label_sec2=Label(gui,text="NOON",font=("Times new roman",10,"bold"),bg="#df002a",fg="white")
label_sec2.place(x=250,y=630,width=50,height=30)
clock()

#--------------------------------------------------------------------------------------------------------- 


##labels and entry   2 
stuname=Label(gui,text="Name:",font=('times','16',),fg='black',bg="#BDC8CC")
stuname.grid(row=2,column=1,padx=20,sticky="w")
e1=Entry(gui,width=20,bd=2)
e1.grid(row=2,column=5)

##labels and entry   3
fatname=Label(gui,text="Total Amount:",font=('times','16',),fg='black',bg="#BDC8CC")
fatname.grid(row=3,column=1,padx=20,sticky="w")
e2=Entry(gui,width=20,bd=2)
e2.grid(row=3,column=5)

##labels and entry   4
rolnum=Label(gui,text="Loan Amount:",font=('times','16',),fg='black',bg="#BDC8CC")
rolnum.grid(row=4,column=1,padx=20,sticky="w")
e3=Entry(gui,width=20,bd=2)
e3.grid(row=4,column=5)

##labels and entry   5
sec=Label(gui,text="Deposit Amount:",font=('times','16',),fg='black',bg="#BDC8CC")
sec.grid(row=5,column=1,padx=20,sticky="w")
e4=Entry(gui,width=20,bd=2)
e4.grid(row=5,column=5)

##labels and entry   6
dob=Label(gui,text="CNIC:",font=('times','16',),fg='black',bg="#BDC8CC")
dob.grid(row=6,column=1,padx=20,sticky="w")
e5=Entry(gui,width=20,bd=2)
e5.grid(row=6,column=5)

##labels and entry   7
email=Label(gui,text="Email:",font=('times','16',),fg='black',bg="#BDC8CC")
email.grid(row=7,column=1,padx=20,sticky="w")
e6=Entry(gui,width=20,bd=2)
e6.grid(row=7,column=5)

# OK button 
ok=Button(gui,text="OK",font=('Times','10'),command=datasave,relief=SUNKEN,width=5,activebackground='green')
ok.grid(row=8,column=5,padx=40,sticky="w")

# QUIT button 
ex=Button(gui,text="EXIT",font=('Times','10'),relief=SUNKEN,width=5,activebackground='red',command=gui.destroy)
ex.grid(row=8,column=5,padx=75,sticky="w")
gui.configure(bg="#BDC8CC") #background color





#--------------------------------------------------------------------
def loan():
    loan = Tk()
    loan.geometry("600x220+0+0")
    loan.title("LOAN DETAILS")
    loan.configure(bg="#6f9eaf")
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="LOAN", fg="black",bg="#6f9eaf", bd=5)
    labeldesc.grid(row=0, column=0)
    labeldesc = Label(loan, font=('aria', 15,'bold'), text="_____________", fg="#6f9eaf",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=2)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="DETAILS", fg="black",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=3)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="LOAN ALLOTED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=0)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="10,000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=3)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="DATED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=0)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="1/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=3)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="RETURN DATE", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=0)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="10/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=3)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="AMOUNT RETURNED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=0)
    labeldesc = Label(loan, font=('aria', 15, 'bold'), text="5000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=3)
    loan.mainloop()

btnprice=Button(gui,padx=16,pady=8, bd=10 ,fg="black",font=('times' ,10,'bold'),width=5, text="Loan", command=loan,activebackground='#79a3b1')
btnprice.grid(row=20, column=14)



#--------------------------------------------------------------------

def Transaction():
    Transaction = Tk()
    Transaction.geometry("600x220+0+0")
    Transaction.title("Transaction DETAILS")
    Transaction.configure(bg="#6f9eaf")
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="Transaction", fg="black",bg="#6f9eaf", bd=5)
    labeldesc.grid(row=0, column=0)
    labeldesc = Label(Transaction, font=('aria', 15,'bold'), text="_____________", fg="#6f9eaf",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=2)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="DETAILS", fg="black",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=3)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="Transaction Amount", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=0)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="30,000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=3)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="DATED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=0)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="1/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=3)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="RETURN DATE", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=0)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="10/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=3)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="AMOUNT RETURNED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=0)
    labeldesc = Label(Transaction, font=('aria', 15, 'bold'), text="5000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=3)
    Transaction.mainloop()

btnprice=Button(gui,padx=16,pady=8, bd=10 ,fg="black",font=('times' ,10,'bold'),width=5, text="Transaction", command=Transaction,activebackground='#79a3b1')
btnprice.grid(row=20, column=12)

#--------------------------------------------------------------------

def Deposit():
    Deposit = Tk()
    Deposit.geometry("600x220+0+0")
    Deposit.title("Deposit DETAILS")
    Deposit.configure(bg="#6f9eaf")
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="Deposit", fg="black",bg="#6f9eaf", bd=5)
    labeldesc.grid(row=0, column=0)
    labeldesc = Label(Deposit, font=('aria', 15,'bold'), text="_____________", fg="#6f9eaf",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=2)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="DETAILS", fg="black",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=0, column=3)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="Deposit Amount", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=0)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="50,000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=1, column=3)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="DATED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=0)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="1/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=2, column=3)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="RETURN DATE", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=0)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="10/1/2021", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=3, column=3)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="AMOUNT RETURNED", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=0)
    labeldesc = Label(Deposit, font=('aria', 15, 'bold'), text="5000", fg="white",bg="#6f9eaf", anchor=W)
    labeldesc.grid(row=4, column=3)
    Deposit.mainloop()

btnprice=Button(gui,padx=16,pady=8, bd=10 ,fg="black",font=('times' ,10,'bold'),width=5, text="Deposit", command=Deposit,activebackground='#79a3b1')
btnprice.grid(row=20, column=10)



#--------------------------------------------------------------------
gui.mainloop() #closing line important
