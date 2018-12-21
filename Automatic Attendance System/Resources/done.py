import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import time
import new_entry

def main():
    root=Toplevel()
    root.attributes("-fullscreen", True)
    #root.configure(background='white')
    #root.geometry("800x600")
    root.title("NEW ENTRY")
    root.iconbitmap(".\Resources\Images\lo.ico")
    
    def start():
        root.destroy()
        

    C_n = Canvas(root, bg="white", height=0, width=0)
    photo1 =ImageTk.PhotoImage(file=".\Resources\Images\done.jpg")
    background_label = Label(root, image=photo1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C_n.pack(side=TOP)
    ###############  FRAMES  #####################
    fl=Frame(root,width=800,height=700,relief=SUNKEN)
    fl.pack(side=BOTTOM)
    lbl_id= Label(fl, font=('arial', 14, 'bold'),text=" T A S K   C O M P L E T E D ",bd=16,anchor="w")
    lbl_id.grid(row=0, column=0)
    btn=Button(fl,padx=50,pady=8,bd=5,fg="black",font=('arial',12,'bold'),width=8,text="  O K  ",bg="#009ACD",command=start)
    btn.grid(row=1,column=0,padx=60,pady=10)
    root.mainloop()

    
    
