import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import sqlite3
import time
import done
import student_data

def main(k):
    conn = sqlite3.connect(".\Resources\Database\data.db")
    c=conn.cursor()

    c.execute('SELECT Id from Student_Data ')
    ids=c.fetchall()
    i_l=[]
    for i in range (0,len(ids)):
        i_l.append(ids[i][0])

    c.execute('SELECT Roll_Number from Student_Data ')
    rols=c.fetchall()
    r_l=[]
    for i in range (0,len(rols)):
        r_l.append(rols[i][0])

    c.execute('SELECT First_Name from Student_Data ')
    fns=c.fetchall()
    fn_l=[]
    for i in range (0,len(fns)):
        fn_l.append(fns[i][0])

    c.execute('SELECT Last_Name from Student_Data ')
    lns=c.fetchall()
    ln_l=[]
    for i in range (0,len(lns)):
        ln_l.append(lns[i][0])

    c.execute('SELECT Semester from Student_Data ')
    sms=c.fetchall()
    sm_l=[]
    for i in range (0,len(sms)):
        sm_l.append(sms[i][0])

    c.execute('SELECT Branch from Student_Data ')
    brs=c.fetchall()
    br_l=[]
    for i in range (0,len(brs)):
        br_l.append(brs[i][0])

    c.execute('SELECT Email from Student_Data ')
    emls=c.fetchall()
    eml_l=[]
    for i in range (0,len(emls)):
        eml_l.append(emls[i][0])
        
    ########################################    
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title("STUDENT DATA")
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
        student_data.main()
        
    #################################


    ################# ASK FOR DETAILS  ##############
    lbl=Label(fl,font=('Times',28,'bold'),text=" STUDENT DATA ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=10)

    lbl_id= Label(fl, font=('arial', 14, 'bold'),text=" ID                   : ",bd=16,anchor="w")
    lbl_id.grid(row=1, column=0)
    txt_id= Label(fl, font=('arial', 14, 'bold'),text=str(i_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_id.grid(row=1, column=1)

    lbl_roll= Label(fl, font=('arial', 14, 'bold'),text=" ROLL NO       : ",bd=16,anchor="w")
    lbl_roll.grid(row=2, column=0)
    txt_roll=Label(fl, font=('arial', 14, 'bold'),text=str(r_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_roll.grid(row=2,column=1)

    lbl_Fn= Label(fl, font=('arial', 14, 'bold'),text=" FIRST NAME  : ",bd=16,anchor="w")
    lbl_Fn.grid(row=3, column=0)
    txt_Fn=Label(fl, font=('arial', 14, 'bold'),text=str(fn_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_Fn.grid(row=3,column=1)

    lbl_Ln= Label(fl, font=('arial', 14, 'bold'),text=" LAST NAME   : ",bd=16,anchor="w")
    lbl_Ln.grid(row=4, column=0)
    txt_Ln=Label(fl, font=('arial', 14, 'bold'),text=str(ln_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_Ln.grid(row=4,column=1)

    lbl_Sm= Label(fl, font=('arial', 14, 'bold'),text=" SEMESTER    : ",bd=16,anchor="w")
    lbl_Sm.grid(row=5, column=0)
    txt_Sm=Label(fl, font=('arial', 14, 'bold'),text=str(sm_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_Sm.grid(row=5,column=1)

    lbl_Br= Label(fl, font=('arial', 14, 'bold'),text=" BRANCH        : ",bd=16,anchor="w")
    lbl_Br.grid(row=6, column=0)
    txt_Br=Label(fl, font=('arial', 14, 'bold'),text=str(br_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_Br.grid(row=6,column=1)

    lbl_Eml= Label(fl, font=('arial', 14, 'bold'),text=" EMAIL            : ",bd=16,anchor="w")
    lbl_Eml.grid(row=7, column=0)
    txt_Eml=Label(fl, font=('arial', 14, 'bold'),text=str(eml_l[int(k)]),fg="#228B22",bd=16,anchor="w")
    txt_Eml.grid(row=7,column=1)

    lbl_Eml= Label(fl, font=('arial', 14, 'bold'),text=" PHOTO           : ",bd=16,anchor="w")
    lbl_Eml.grid(row=8, column=0)
    #################### BUTTONS  #####################
    ide=str(i_l[int(k)])
    p2 =ImageTk.PhotoImage(file=".\Resources\dataset\user."+str(ide)+".19.jpg")
    btnUp=Button(fl,pady=1,bd=2,fg="black",font=('arial',15,'bold'),width=150,text="",bg="black",image=p2).grid(row=8,column=1,pady=1)
    
    btnUp=Button(fl,padx=10,pady=20,bd=15,fg="black",font=('arial',10,'bold'),width=12,text=" BACK ",bg="#FF3030", command=ex).grid(row=8,column=2,padx=30,pady=20)


    root.mainloop()
