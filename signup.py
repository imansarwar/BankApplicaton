from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from login import Login
class registration:
    def __init__ (self,root):
        self.root=root
        self.root.title('REGISTRATION FORM')
        self.root.geometry("900x500")
        label_0 =Label(root,text="REGISTRATION FORM", width=20,font=("bold",20))
        label_0.place(x=90,y=60)


        label_1 =Label(root,text="FullName", width=20,font=("bold",10))
        label_1.place(x=70,y=130)

        entry_1=Entry(root)
        entry_1.place(x=240,y=130)

        label_3 =Label(root,text="Password", width=20,font=("bold",10))
        label_3.place(x=68,y=180)

        entry_3=Entry(root,show="*")
        entry_3.place(x=240,y=180)

        label_4 =Label(root,text="Gender", width=20,font=("bold",10))
        label_4.place(x=60,y=230)


        var=IntVar()

        Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
        Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)


        label_5=Label(root,text="Country",width=20,font=("bold",10))
        label_5.place(x=60,y=280)

        list_of_country=[ 'Pakistan' ,'Turkey' , 'UK' ,'Germany' ,'Australia']


        c=StringVar()
        droplist=OptionMenu(root,c, *list_of_country)
        droplist.config(width=20)
        c.set('Select your Country')
        droplist.place(x=230,y=270)

        label_6=Label(root,text="Language",width=20,font=('bold',10))
        label_6.place(x=65,y=330)


        var1=IntVar()

        Checkbutton(root,text="English", variable=var1).place(x=230,y=330)

        var2=IntVar()
        Checkbutton(root,text="Turkish", variable=var2).place(x=300,y=330)

       # button = Button(root,width=10 ,text="Open System",bg="#6f9eaf",fg='white', command=root.destroy).place(x=310,y=380)
        
        #Images
        self.img1=ImageTk.PhotoImage(file="imagesreg/img1.jpg")
        self.label_img1=Label(self.root,image=self.img1).place(x=450,y=60)
        self.img2=ImageTk.PhotoImage(file="imagesreg/img2.png")
        self.label_img2=Label(self.root,image=self.img2).place(x=750,y=200)



        def hello():
           messagebox.showinfo("Register", "You have registered successfully")
           root.destroy()
        B1=Button(root, text='Submit' , width=10,bg="#6f9eaf",fg='white',command=hello).place(x=230,y=380)
        
        #Animation Images
        self.img3=ImageTk.PhotoImage(file="imagesreg/img3.png")
        self.img4=ImageTk.PhotoImage(file="imagesreg/img4.jpg")
        self.img5=ImageTk.PhotoImage(file="imagesreg/img5.jpg")

        self.label_change_img=Label(self.root,bg="gray")
        self.label_change_img.place(x=760,y=225,width=84,height=150)

        self.animate()

    def animate(self):
        self.im=self.img3
        self.img3=self.img4
        self.img4=self.img5
        self.img5=self.im
        self.label_change_img.config(image=self.im)
        self.label_change_img.after(2000,self.animate)
            

        

root=Tk()
obj=registration(root)
root.mainloop()
