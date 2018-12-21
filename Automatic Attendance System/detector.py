#made by sameer kaushik
import cv2
import numpy as np
import time
import smtplib
import sqlite3

########## DATABASE  #################
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
        

mail_list=[]
present_list=[]
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=0,0,0,0,0,0,0,0,0,0
it_1,it_2,it_3,it_4,civil_1,civil_2,civil_3,civil_4,env_3,env_4=[],[],[],[],[],[],[],[],[],[]

c.execute('SELECT Email from Student_Data ')
ml=c.fetchall()

##########  MAIL  ###############    
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('your email','password')                      #enter your email and password

#cv2.namedWindow("Face",cv2.WND_PROP_FULLSCREEN)                                    #use these 2 lines to get a full screen face detector
#cv2.setWindowProperty("Face", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

faceDetect=cv2.CascadeClassifier('Resources/recognizer/haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

#cv2.namedWindow('Face',cv2.WINDOW_NORMAL)                  #use these 2 line to get a 500x500 face detector
#cv2.resizeWindow('Face', 500,500)

rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("Resources/recognizer/trainingData.yml")

id=1
name="  "
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

#============================
#   MAIN FUNCTION
#============================

def dt(id):
    rol=r_l[i_l.index(str(id))]
    name=fn_l[i_l.index(str(id))]
    eml=eml_l[i_l.index(str(id))]
    sem=sm_l[i_l.index(str(id))]
    br=br_l[i_l.index(str(id))]
    Subject="CBPGEC ATTENDANCE SYSTEM"
    a= "Subject:{}\nTo,\n".format(Subject)
    b="\nYou were present in the class on "
    c="\n\nNOTE:- You can use this e-mail as a proof of your attendance \n\nCBP Govt. Engg. College\nJaffarpur\nDelhi-110073\n"

    localtime=time.asctime(time.localtime(time.time()))
    if(ci==30):
        if (eml not in mail_list):
            content=a + name + b + localtime + c
            mail.sendmail('enter your email',str(eml),content)              # enter your email here
            mail_list.append(eml)
            present_list.append(id)


            #==========================
            # ENTERING ROLL NO INTO LIST
            #==========================

            if (br=="IT"):
                if (sem=="2"):
                    it_1.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO it_1  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="4"):
                    it_2.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO it_2  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="6"):
                    it_3.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO it_3  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="8"):
                    it_4.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO it_4  VALUES (?,?)',(rol,name))
                    conn.commit()

            elif(br=="Civil"):
                if (sem=="2"):
                    civil_1.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO civil_1  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="4"):
                    civil_2.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO civil_2  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="6"):
                    civil_3.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO civil_3  VALUES (?,?)',(rol,name))
                    conn.commit()

                elif (sem=="8"):
                    civil_4.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO civil_4  VALUES (?,?)',(rol,name))
                    conn.commit()

            else:
                if (sem=="6"):
                    env_3.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO env_3  VALUES (?,?)',(rol,name))
                    conn.commit()
                
                elif (sem=="8"):
                    env_4.append(rol)
                    c=conn.cursor()
                    c.execute('INSERT INTO env_4  VALUES (?,?)',(rol,name))
                    conn.commit()
        
        else:
            pass
    else:
        pass

    cv2.putText(img,str(name),(x,y-10),font,1.5,(0,0,255,1),2);
    cv2.putText(img,str(rol),(x,y+h+20),font,1,(0,0,255,1),1);
    cv2.putText(img,str("BRANCH:-"+str(br)),(x,y+h+50),font,1,(0,0,255,1),1);
    cv2.putText(img,str("SEMESTER:-"+str(sem)),(x,y+h+80),font,1,(0,0,255,1),1);


#=============================
#      DETECTOR
#=============================

    
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if id not in present_list:
            if(id==1):
                c1=c1+1
                ci=c1
                dt(1)
            elif(id==2):
                c2=c2+1
                ci=c2
                dt(2)
            elif(id==3):
                c3=c3+1
                ci=c3
                dt(3)
            elif(id==4):
                c4=c4+1
                ci=c4
                dt(4)
            elif(id==5):
                c5=c5+1
                ci=c5
                dt(5)

        else:
            pass
           
        
    cv2.imshow("Face",img)  
    if (cv2.waitKey(1)==27):
        break
    
mail.close()

cam.release()
cv2.destroyAllWindows()
#made by sameer kaushik
