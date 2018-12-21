from Tkinter import*
from PIL import Image, ImageTk
import numpy as np
import sys
sys.path.insert(0,'./Resources/')
import change_id_pass
import add_admin

def main():        
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title(" ADMIN  SETTINGS")
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
    lbl=Label(fl,font=('Times',35,'bold'),text=" ADMIN SETTINGS ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=10)

    lbl=Label(fl,font=('Times',15,'bold'),text=" ",fg="#00008B",anchor='w')
    lbl.grid(row=1,column=1,padx=10,pady=2)

    def chng():
        change_id_pass.main()

    def adadmin():
        add_admin.main()
 
    def ex():
        root.destroy()


    ###############  BUTTONS  ###########################
    btnNw=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=20,text=" CHANGE CREDENTIALS ",bg="#00C957",activebackground="#00C957",relief="raised",overrelief="ridge", command=chng).grid(row=2,column=1,padx=10,pady=10)
    btnNw=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',14,'bold'),width=20,text=" ADD ADMIN ",bg="#00C957",activebackground="#00C957",relief="raised",overrelief="ridge", command=adadmin).grid(row=3,column=1,padx=10,pady=10)

    lbl=Label(fl,font=('Times',15,'bold'),text=" ",fg="#00008B",anchor='w')
    lbl.grid(row=4,column=1,padx=5,pady=2)

    btnUp=Button(fl,padx=20,pady=10,bd=10,fg="black",font=('arial',12,'bold'),width=12,text=" BACK ",bg="#FF3030",activebackground= "#FF3030",command=ex,relief="raised",overrelief="ridge").grid(row=5,column=1,padx=25,pady=10)

    lbl=Label(fl,font=('Times',20,'bold'),text=" ",fg="#00008B",anchor='w')
    lbl.grid(row=6,column=1,padx=10,pady=10)

    p1 =ImageTk.PhotoImage(file=".\Resources\Images\lo.ico")
    btnUp=Button(fl,pady=5,bd=0,fg="black",font=('arial',20,'bold'),width=200,text="",image=p1).grid(row=7,column=1,pady=15)

    root.mainloop()

