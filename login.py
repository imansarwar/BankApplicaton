#Login System
from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import messagebox

class Login:
    def __init__ (self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("900x600+30+30")
        self.root.resizable(False,False)
        #Image
        self.bg=ImageTk.PhotoImage(file="images/check1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #Login Frame

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=40,y=100,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),bg="white",fg="#6f9eaf").place(x=90,y=30)
        desc=Label(Frame_login,text="Accountant Employee",font=("Goudy Old Style",15,"bold"),bg="white",fg="grey").place(x=90,y=100)

        #User text box
        lbl_user=Label(Frame_login,text="Username",font=("Goudy Old Style",15,"bold"),bg="white",fg="#6f9eaf").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

         #Password text box
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy Old Style",15,"bold"),bg="white",fg="#6f9eaf").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)


        forget_btn=Button(Frame_login,text="Forgot Password?",bg="white",fg="#6f9eaf",font=("times new roman",12),bd=0).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,text="Login",bg="#6f9eaf",fg="white",font=("times new roman",20)).place(x=240,y=420,width=140,height=40)
##        exit_btn=Button(Frame_login,command=close_window,text="Exit",bg="white",fg="#ee9595",font=("times new roman",12),bd=0).place(x=100,y=280)
##       button = Button(Frame_login, text="Open System",bg="white",fg="#6f9eaf",font=("times new roman",12), command=root.destroy).place(x=340,y=290)
        Register_btn=Button(self.root,command=root.destroy,text="Register",bg="#6f9eaf",fg="white",font=("times new roman",20)).place(x=390,y=420,width=140,height=40)
    
    
        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="Iman":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("LOGIN","You are successfully Logged In.")
            root.destroy()




            
root=Tk()

obj=Login(root)
root.mainloop()
