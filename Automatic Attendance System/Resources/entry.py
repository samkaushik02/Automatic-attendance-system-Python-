from Tkinter import*
import random
import time
import datetime
from PIL import Image, ImageTk
import sys
sys.path.insert(0,'./Resources/')
import new_entry
import update_entry
import student_data
import admin_settings
import about
import calibrate_db

def main():
    
    root=Tk()
    root.attributes("-fullscreen", True)
    #root.configure(background='white')
    #root.geometry("1600x8000")
    root.title("STUDENT MANAGEMENT SYSTEM")
    root.iconbitmap(".\Resources\Images\lo.ico")

    C = Canvas(root, bg="white", height=0, width=0)
    photo1 =ImageTk.PhotoImage(file=".\Resources\Images\h.jpg")
    background_label = Label(root, image=photo1,bg="#8B0000")
    background_label.place(x=0, y=0, relwidth=1, relheight=0.15)
    C.pack(side=TOP)


    ###############  FUNCTIONS  ################
    def ne(): 
        new_entry.main()

    def ue():
        update_entry.main()
        
    def cdb():
        calibrate_db.main()

    def sd():
        student_data.main()

    def ast():
        admin_settings.main()

    def ab():
        about.main()

    def ex():
        root.destroy()
        
    ###############  FRAMES  #####################
    fl=Frame(root,width=800,height=700,relief=SUNKEN)
    fl.pack(side=BOTTOM)


    ################  TIME  ####################
    localtime=time.asctime(time.localtime(time.time()))


    ###########  LABEL AND BUTTON  ##############
    lblInfo=Label(fl,font=('Times',35,'bold'),text=" Student Management System ",bg="yellow",fg="#00008B",anchor='w')
    lblInfo.grid(row=0,column=1)

    lblInfo=Label(fl,font=('Times',15,'bold'),text=localtime,fg="#8B2500",anchor='w')
    lblInfo.grid(row=5,column=1,pady=15)

    lblInfo=Label(fl,font=('Times',15,'bold'),text=" Only for college purpose\n ",fg="#8B2500",anchor='w')
    lblInfo.grid(row=6,column=1)

    btnEx=Button(fl,padx=50,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=10,text="STUDENT \n DATA",bg="#009ACD",activebackground="#009ACD",command=sd,relief="raised",overrelief="ridge").grid(row=2,column=0,padx=80,pady=20)
    btnAb=Button(fl,padx=50,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=10,text="ADMIN \n SETTINGS",bg="#009ACD",activebackground="#009ACD",command=ast,relief="raised",overrelief="ridge").grid(row=3,column=0,padx=80,pady=20)

    btnNw=Button(fl,padx=100,pady=20,bd=15,fg="black",font=('arial',18,'bold'),width=12,text="NEW ENTRY",bg="#00C957" ,activebackground="#00C957",command=ne,relief="raised",overrelief="ridge").grid(row=1,column=1,padx=80,pady=20)
    btnUp=Button(fl,padx=100,pady=20,bd=15,fg="black",font=('arial',18,'bold'),width=12,text="UPDATE ENTRY",bg="#00C957",activebackground="#00C957",command=ue,relief="raised",overrelief="ridge").grid(row=2,column=1,padx=80,pady=20)
    btnVw=Button(fl,padx=100,pady=20,bd=15,fg="black",font=('arial',18,'bold'),width=12,text="CALIBRATE DATABASE",bg="#00C957",activebackground="#00C957",command=cdb,relief="raised",overrelief="ridge").grid(row=3,column=1,padx=80,pady=20)

    btnAb=Button(fl,padx=50,pady=10,bd=10,fg="black",font=('arial',12,'bold'),width=10,text="ABOUT",bg="#FF3030",activebackground="#FF3030",command=ab,relief="raised",overrelief="ridge").grid(row=2,column=2,padx=80,pady=20)
    btnEx=Button(fl,padx=50,pady=10,bd=10,fg="black",font=('arial',12,'bold'),width=10,text="EXIT",bg="#FF3030",activebackground="#FF3030",command=ex,relief="raised",overrelief="ridge").grid(row=3,column=2,padx=80,pady=20)

    root.mainloop()
