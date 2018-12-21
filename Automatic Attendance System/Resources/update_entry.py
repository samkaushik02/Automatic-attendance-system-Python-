import sys
sys.path.insert(0,'./Resources/')
from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import sqlite3
import time
import done
import cv2
from tkinter import messagebox


def main():
    conn = sqlite3.connect(".\Resources\Database\data.db")
    c=conn.cursor()
    c.execute('SELECT Id from Student_Data ')
    ids=c.fetchall()
    i_list=[]
    for i in range (0,len(ids)):
        i_list.append(ids[i][0])

        
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
        
    #################################


    ################# ASK FOR DETAILS  ##############
    lbl=Label(fl,font=('Times',30,'bold'),text=" UPDATE ENTRY ",bg="yellow",fg="#00008B",anchor='w')
    lbl.grid(row=0,column=1,padx=10,pady=10)

    lbl_id= Label(fl, font=('arial', 16, 'bold'),text=" ID                   : ",bd=16,anchor="w")
    lbl_id.grid(row=1, column=0)
    txt_id= Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_id.grid(row=1, column=1)

    lbl_roll= Label(fl, font=('arial', 16, 'bold'),text=" ROLL NO       : ",bd=16,anchor="w")
    lbl_roll.grid(row=2, column=0)
    txt_roll=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_roll.grid(row=2,column=1)

    lbl_Fn= Label(fl, font=('arial', 16, 'bold'),text=" FIRST NAME  : ",bd=16,anchor="w")
    lbl_Fn.grid(row=3, column=0)
    txt_Fn=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_Fn.grid(row=3,column=1)

    lbl_Ln= Label(fl, font=('arial', 16, 'bold'),text=" LAST NAME   : ",bd=16,anchor="w")
    lbl_Ln.grid(row=4, column=0)
    txt_Ln=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_Ln.grid(row=4,column=1)

    lbl_Sm= Label(fl, font=('arial', 16, 'bold'),text=" SEMESTER    : ",bd=16,anchor="w")
    lbl_Sm.grid(row=5, column=0)
    txt_Sm=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_Sm.grid(row=5,column=1)

    lbl_Br= Label(fl, font=('arial', 16, 'bold'),text=" BRANCH        : ",bd=16,anchor="w")
    lbl_Br.grid(row=6, column=0)
    txt_Br=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_Br.grid(row=6,column=1)

    lbl_Eml= Label(fl, font=('arial', 16, 'bold'),text=" EMAIL            : ",bd=16,anchor="w")
    lbl_Eml.grid(row=7, column=0)
    txt_Eml=Entry(fl, font=('arial',15),bd=10,insertwidth=4,bg="powder blue",justify='right')
    txt_Eml.grid(row=7,column=1)

    ############################################################

    def take():
        id=str(txt_id.get())
        roll=str(txt_roll.get())
        Fn=str(txt_Fn.get())
        Ln=str(txt_Ln.get())
        Sm=str(txt_Sm.get())
        Br=str(txt_Br.get())
        Eml=str(txt_Eml.get())

        if id in i_list:                
            faceDetect=cv2.CascadeClassifier('Resources/recognizer/haarcascade_frontalface_default.xml');
            cam=cv2.VideoCapture(0);
            t=0
            for i in range(0,150):
                ret,img=cam.read();
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=faceDetect.detectMultiScale(gray,1.3,5);
                for(x,y,w,h) in faces:
                    cv2.imwrite("Resources/dataset/user."+str(id)+"."+str(t)+".jpg",gray[y:y+h,x:x+w])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    #print(t)
                    t=t+1
                    cv2.waitKey(100);
                cv2.imshow("Face",img)
                cv2.waitKey(1);
                #print(str(i)+"    "+str(t))
                
                if(t==20):
                    c=conn.cursor()
                    c.execute('UPDATE Student_Data SET First_Name=?,Last_Name=?,Semester=?,Branch=?,Email=? WHERE Id=?',(Fn,Ln,Sm,Br,Eml,id))
                    conn.commit()
                    #print("\nData added to database")
                    cam.release()
                    cv2.destroyAllWindows()
                    break
                
                else:
                    pass

            ex()
            done.main()

        else:
            messagebox.showerror("ID NOT FOUND", "No such id found in database\n\n Try again with correct id")

    #################### BUTTONS  #####################
    btnNw=Button(fl,padx=50,pady=20,bd=15,fg="black",font=('arial',10,'bold'),width=12,text=" UPDATE \n AND \n TAKE PHOTO ",bg="#00C957",command=take).grid(row=8,column=1,padx=30,pady=20)
    btnUp=Button(fl,padx=10,pady=20,bd=15,fg="black",font=('arial',10,'bold'),width=12,text=" BACK ",bg="#FF3030", command=ex).grid(row=8,column=2,padx=30,pady=20)


    root.mainloop()

