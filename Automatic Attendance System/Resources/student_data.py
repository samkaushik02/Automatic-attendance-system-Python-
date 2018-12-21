import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import sqlite3
import time
import done
import view_st
from tkinter import messagebox

def main():
    conn = sqlite3.connect(".\Resources\Database\data.db")
    c=conn.cursor()
    c.execute('SELECT Id from Student_Data ')
    ids=c.fetchall()
    id_list=[]
    for i in range (0,len(ids)):
        id_list.append(ids[i][0])
    
    c.execute('SELECT Roll_Number from Student_Data ')
    rols=c.fetchall()
    rol_list=[]
    for i in range (0,len(rols)):
        rol_list.append(rols[i][0])

    c.execute('SELECT * from Student_Data ')
    data=c.fetchall()

    ########################################    
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title("UPDATE ENTRY")
    root.iconbitmap(".\Resources\Images\lo.ico")
    
    C_n = Canvas(root, bg="white", height=0, width=0)
    photo1 =ImageTk.PhotoImage(file=".\Resources\Images\h.jpg")
    background_label = Label(root, image=photo1,bg="#8B0000")
    background_label.place(x=0, y=0, relwidth=1, relheight=0.15)
    C_n.pack(side=TOP)

    ###############  FRAMES  #####################
    fl=Frame(root,width=800,height=700,relief=SUNKEN)
    fl.pack(side=BOTTOM)

    ############### SET DETAIL  ################

    def ex():
        root.destroy()

    def vw():
        id_g=id_txt.get()
        rol_g=rol_txt.get()

        if id_g in id_list:
            k=id_list.index(id_g)
            root.destroy()
            view_st.main(k)

        elif rol_g in rol_list:
            k=rol_list.index(rol_g)
            root.destroy()
            view_st.main(k)

        else:
            root.destroy()
            messagebox.showerror("DATA NOT FOUND", "No such data is found in the database\n\n Please try again with correct details")

        

        
        
    #################################


    ################# ASK FOR DETAILS  ##############
    lbl=Label(fl,font=('Times',35,'bold'),text=" STUDENT DETAILS ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=20)

    id_lbl= Label(fl, font=('arial', 16, 'bold'),text="Enter ID ",bd=16,anchor="w")
    id_lbl.grid(row=1, column=1,padx=10,pady=1)
    id_txt= Entry(fl, font=('arial',15),bd=5,insertwidth=4,bg="powder blue",justify='right')
    id_txt.grid(row=2, column=1,padx=10,pady=1)

    or_lbl= Label(fl, font=('arial', 20, 'bold'),text=" OR  ",bd=16,anchor="w")
    or_lbl.grid(row=3, column=1,padx=10,pady=5)

    rol_lbl= Label(fl, font=('arial', 16, 'bold'),text="Enter Roll No ",bd=16,anchor="w")
    rol_lbl.grid(row=4, column=1,padx=10,pady=1)
    rol_txt= Entry(fl, font=('arial',15),bd=5,insertwidth=4,bg="powder blue",justify='right')
    rol_txt.grid(row=5, column=1,padx=10,pady=1)

    g1= Label(fl, font=('arial', 10, 'bold'),text=" ",bd=16,anchor="w")
    g1.grid(row=6, column=1,padx=10,pady=2)
    g2= Label(fl, font=('arial', 16, 'bold'),text=" ",bd=16,anchor="w")
    g2.grid(row=8, column=1,padx=10,pady=10)

    ###########  BUTTONS  ############

    btnNw=Button(fl,padx=50,pady=20,bd=15,fg="black",font=('arial',12,'bold'),width=12,text=" VIEW  DETAILS ",bg="#00C957",command=vw).grid(row=7,column=0,padx=10,pady=10)
    btnUp=Button(fl,padx=25,pady=15,bd=15,fg="black",font=('arial',12,'bold'),width=12,text=" BACK ",bg="#FF3030", command=ex).grid(row=7,column=2,padx=10,pady=10)

    root.mainloop()
