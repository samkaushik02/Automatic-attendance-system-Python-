import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import time
import dev

def main():
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title(" ABOUT US ")
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

    def develop():
        dev.main()
    #################################


    ################# ASK FOR DETAILS  ##############
    lbl=Label(fl,font=('Times',35,'bold'),text=" ABOUT US ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=5,pady=15)

    lbl_id= Label(fl, font=('arial', 10, 'bold'),text='''Chaudhary Brahm Prakash Government Engineering College (CBPGEC) is a premier government engineering institute located in Delhi, India.
It was established by the Department of Training and Technical Education, Government of National Capital Territory of Delhi in 2007
and was named after the first Chief Minister of Delhi, Chaudhary Brahm Prakash. The aim of the Government of NCT of Delhi is to develop
this college as a centre of excellence in Civil engineering and Environmental engineering. The college is affiliated to Guru Gobind Singh
Indraprastha University, a state university established by the Government of NCT of Delhi.

The institute is amongst the only four government institutes (IIT , DTU , Jamia Millia Islamia) in Delhi which offer Civil engineering.
It is the only college in Delhi after Delhi technological university to provide Btech in environmental engineering''',bd=16,anchor="w")
    lbl_id.grid(row=1, column=1,pady=10)
    btnUp=Button(fl,padx=5,pady=15,bd=10,fg="black",font=('arial',10,'bold'),width=20,text="\n DEVELOPER \n",bg="#009ACD",activebackground="#009ACD",command=develop,relief="raised",overrelief="ridge" ).grid(row=2,column=0,padx=10,pady=20)
    p1 =ImageTk.PhotoImage(file=".\Resources\Images\c3.jpg")
    btnUp=Button(fl,pady=5,bd=2,bg="black",font=('arial',20,'bold'),width=600,text="",image=p1).grid(row=2,column=1,pady=20)
    
    btnUp=Button(fl,padx=5,pady=15,bd=10,fg="black",font=('arial',10,'bold'),width=20,text="\nBACK\n",bg="#FF3030",relief="raised",overrelief="ridge", command=ex).grid(row=2,column=2,padx=10,pady=20)


    root.mainloop()
