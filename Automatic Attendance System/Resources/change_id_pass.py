import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import sqlite3
import time
import done
from tkinter import messagebox

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

    c.execute('SELECT Admin_id from Admin ')
    admins=c.fetchall()
    ad_i=[]
    for i in range(0,len(admins)):
        ad_i.append(admins[i][0])

    ########################################    
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title(" CHANGE ID AND PASSWORD")
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
    lbl=Label(fl,font=('Times',35,'bold'),text=" CHANGE\n ID AND PASSWORD ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=2)

    g1=Label(fl,font=('Times',10,'bold'),text=" ",fg="#00008B",anchor='w')
    g1.grid(row=1,column=1,padx=10,pady=10)
    
    u1_l= Label(fl, font=('arial', 18, 'bold'),text=" OLD USER  ID : ",bd=16,anchor="w")
    u1_l.grid(row=2, column=0)
    u1_t=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    u1_t.grid(row=2,column=1)

    p1_l= Label(fl, font=('arial', 18, 'bold'),text=" OLD PASSWORD : ",bd=16,anchor="w")
    p1_l.grid(row=3, column=0)
    p1_t=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    p1_t.grid(row=3,column=1)

    g2=Label(fl,font=('Times',10,'bold'),text=" ",fg="#00008B",anchor='w')
    g2.grid(row=4,column=1,padx=10,pady=5)

    u2_l= Label(fl, font=('arial', 18, 'bold'),text=" NEW USER ID : ",bd=16,anchor="w")
    u2_l.grid(row=5, column=0)
    u2_t=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    u2_t.grid(row=5,column=1)

    p2_l= Label(fl, font=('arial', 18, 'bold'),text=" NEW PASSWORD : ",bd=16,anchor="w")
    p2_l.grid(row=6, column=0)
    p2_t=Entry(fl, font=('arial',16),bd=10,insertwidth=4,bg="powder blue",justify='right')
    p2_t.grid(row=6,column=1)

    g3=Label(fl,font=('Times',10,'bold'),text=" ",fg="#00008B",anchor='w')
    g3.grid(row=7,column=1,padx=10,pady=5)

    g4=Label(fl,font=('Times',10,'bold'),text=" ",fg="#00008B",anchor='w')
    g4.grid(row=9,column=1,padx=10,pady=5)

    ########## FUNCTIONS  ###################
    def ex():
        root.destroy()
        

    def change():
        u1=u1_t.get()
        p1=p1_t.get()
        u2=u2_t.get()
        p2=p2_t.get()

        if(str(u1) in u):
            if(str(p1) in p):
                if u.index(str(u1))==p.index(str(p1)):
                    ad_id=ad_i[int(u.index(str(u1)))]
                    c=conn.cursor()
                    c.execute('UPDATE Admin SET User=?,Password=? WHERE Admin_id=?',(u2,p2,int(ad_id)))
                    conn.commit()
                    root.destroy()
                    done.main()

                else:
                    messagebox.showerror("ERROR"," ID and password does not match\n\n Please try again with right credentials")
            else:
                messagebox.showerror("ERROR"," Wrong password\n\n Please try again")
        else:
            messagebox.showerror("ERROR"," No such user id found\n\n Please try again")
 

                
        
    ######  BUTTONS  ###############

    btnNw=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=12,text=" UPDATE ",bg="#00C957",activebackground="#00C957",command=change,relief="raised",overrelief="ridge").grid(row=8,column=1,padx=10,pady=5)
    btnUp=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',12,'bold'),width=12,text=" BACK ",bg="#FF3030",activebackground= "#FF3030",command=ex,relief="raised",overrelief="ridge").grid(row=8,column=2,padx=25,pady=20)

    root.mainloop()
