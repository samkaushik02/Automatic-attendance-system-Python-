#made by sameer kaushik
from Tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import numpy as np
import sys
sys.path.insert(0,'./Resources/')
import entry

def main():        
    conn = sqlite3.connect(".\Resources\Database\data.db")
    c=conn.cursor()
    c.execute('SELECT User from Admin ')
    users=c.fetchall()
    u=[]
    for i in range(0,len(users)):
        u.append(users[i][0])

    c.execute('SELECT Password from Admin ')
    pswrd=c.fetchall()
    p=[]
    for i in range(0,len(pswrd)):
        p.append(pswrd[i][0])

    ########################################    
    root=Tk()
    root.attributes("-fullscreen", True)
    root.title("HOME")
    root.iconbitmap(".\Resources\Images\lo.ico")

    C_n = Canvas(root, bg="white", height=0, width=0)
    photo1 =ImageTk.PhotoImage(file=".\Resources\Images\h.jpg")
    background_label = Label(root, image=photo1,bg="#8B0000")
    background_label.place(x=0, y=0, relwidth=1, relheight=0.15)
    C_n.pack(side=TOP)

    ###############  FRAMES  #####################
    fl=Frame(root,width=800,height=700,relief=SUNKEN)
    fl.pack(side=BOTTOM)


    ################# ASK FOR DETAILS  ##############
    lbl=Label(fl,font=('Times',35,'bold'),text=" ADMIN LOGIN",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=20)

    usr_lb= Label(fl, font=('arial', 18, 'bold'),text=" USER  ID       : ",bd=16,anchor="w")
    usr_lb.grid(row=1, column=0)
    usr=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    usr.grid(row=1,column=1)

    pswd_lb= Label(fl, font=('arial', 18, 'bold'),text=" PASSWORD  : ",bd=16,anchor="w")
    pswd_lb.grid(row=2, column=0)
    pswd=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    pswd.grid(row=2,column=1)


    ########## FUNCTIONS  ###################
    def ex():
        root.destroy()
        quit()

    def check():    
        user=usr.get()
        password=pswd.get()
        if user in u:
            if (str(password)==str(p[u.index(user)])):
                root.destroy()
                entry.main()
            else:
                messagebox.showerror(" WRONG PASSWORD "," You have entered wrong password \n\n Please try again")

        else:
            messagebox.showerror(" WRONG USER ID "," No such admin found \n\n Please try again")
            

    ###############  BUTTONS  ###########################
    btnNw=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=12,text=" LOGIN ",bg="#00C957",activebackground="#00C957",relief="raised",overrelief="ridge", command=check).grid(row=3,column=1,padx=10,pady=5)
    btnUp=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',12,'bold'),width=12,text=" EXIT ",bg="#FF3030",activebackground= "#FF3030",command=ex,relief="raised",overrelief="ridge").grid(row=3,column=2,padx=25,pady=20)
    p1 =ImageTk.PhotoImage(file=".\Resources\Images\c3.jpg")
    btnUp=Button(fl,pady=5,bd=0,fg="black",font=('arial',20,'bold'),width=600,text="",image=p1).grid(row=4,column=1,pady=5)

    p2 =ImageTk.PhotoImage(file=".\Resources\Images\lo.ico")
    btnUp=Button(fl,pady=5,bd=0,fg="black",font=('arial',20,'bold'),width=150,text="",image=p2).grid(row=4,column=0,pady=5)
    p3 =ImageTk.PhotoImage(file=".\Resources\Images\lo.ico")
    btnUp=Button(fl,pady=5,bd=0,fg="black",font=('arial',20,'bold'),width=150,text="",image=p2).grid(row=4,column=2,pady=5)

    root.mainloop()
    
main()
#made by sameer kaushik
