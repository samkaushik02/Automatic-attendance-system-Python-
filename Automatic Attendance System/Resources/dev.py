from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import webbrowser

def main():
    root=Toplevel()
    root.attributes("-fullscreen", True)
    root.title(" DEVELOPER TEAM ")
    root.iconbitmap(".\Resources\Images\lo.ico")
    
    C_n = Canvas(root, bg="white", height=0, width=0)
    photo1 =ImageTk.PhotoImage(file=".\Resources\Images\h.jpg")
    background_label = Label(root, image=photo1,bg="#8B0000")
    background_label.place(x=0, y=0, relwidth=1, relheight=0.15)
    C_n.pack(side=TOP)
    
    
    ###############  FRAMES  #####################
    fl=Frame(root,width=800,height=700,relief=SUNKEN)
    fl.pack(side=BOTTOM)

    ############### FUNCTION  ################

    def ex():
        root.destroy()

    def lin():
        return webbrowser.open("https://www.linkedin.com/in/sameerkaushik02/")

    def git():
        return webbrowser.open("https://github.com/samkaushik02")

    def ytb():
        return webbrowser.open("https://www.youtube.com/channel/UC9oQqSOA6QhL4UczFMBocPA?view_as=subscriber")

        
    #################################

    lbl=Label(fl,font=('Times',50,'bold'),text=" DEVELOPER  ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=5)

    lbl_id= Label(fl, font=('arial', 18, 'bold'),text=" \n",bd=16,anchor="w",fg="#006400")
    lbl_id.grid(row=1, column=1)

    lbl_id= Label(fl, font=('arial', 30, 'bold'),text="  SAMEER KAUSHIK  \n\n",bd=16,anchor="w",fg="#8B0000")
    lbl_id.grid(row=2, column=1)

    btnUp=Button(fl,padx=10,pady=10,bd=10,fg="black",font=('arial',10,'bold'),width=10,text=" Linkedin ",bg="skyblue", command=lin).grid(row=3,column=0,padx=20,pady=10)
    btnUp=Button(fl,padx=10,pady=10,bd=10,fg="black",font=('arial',10,'bold'),width=10,text=" Github ",bg="skyblue", command=git).grid(row=3,column=1,padx=20,pady=10)
    btnUp=Button(fl,padx=10,pady=10,bd=10,fg="black",font=('arial',10,'bold'),width=10,text=" Youtube ",bg="skyblue", command=ytb).grid(row=3,column=2,padx=20,pady=10)

    lbl_id= Label(fl, font=('arial', 18, 'bold'),text=" ",bd=16,anchor="w",fg="#006400")
    lbl_id.grid(row=4, column=1, padx=20, pady=10)

    #################### BUTTONS  #####################

    btnUp=Button(fl,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=20,text=" BACK ",bg="#FF3030", command=ex).grid(row=5,column=1,padx=20,pady=10)

    root.mainloop()
