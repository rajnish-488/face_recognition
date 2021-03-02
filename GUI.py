from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import cv2
import numpy as np
import face_recognition as fr
import time
import os
import time
from datetime import date

a=[]
lena=0

       
def attendance(name):
    #aname= name
    if(name not in a):
        a.append(name)
        print(a)
        #put.putlabel()

'''def put():
    root = Tk()
    yo = facerek(root)
    root.mainloop()'''
def put():

    
    #time()    
    
        
    def putData():
        print(a)
        current_time = time.strftime("%H:%M:%S")
        dateToday= date.today()
        file=open("att.text", "a")
        for x in a:
            file.write(x+"\t"+current_time+"\t"+str(dateToday)+ "\t"+"CHECK IN")
            file.write("\n")
        file.close()
        f1.config(text = a)
        #a.clear()
        #print(a)

    def outData():
        print(a)
        current_time = time.strftime("%H:%M:%S")
        dateToday= date.today()
        file=open("att.text", "a")
        for x in a:
            file.write(x+"\t"+current_time+"\t"+str(dateToday)+ "\t"+"CHECK OUT")
            file.write("\n")
        file.close()
        f1.config(text = a)
        #a.clear()
        #print(a)    

    def clearList():
        a.clear()
        print(a)
        f1.config(text = a)
    
    root = Tk()
    root.geometry("400x300")
    root.title("GANDUA KA LIYA ATTENDENCE")
    root.configure(bg = "lightyellow")
    root.resizable(False, False)
    frame1 = Frame(root, bd =2,relief = RIDGE, bg="lightyellow" )
    frame1.place(x =20 , y=20,height = 180, width = 200)
    f1=Label(frame1, text = "NAME", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
    f1.place(x =0 , y=0,height = 180, width = 200)
    checkin = Button(root, text="CHECK IN" , command = putData , bg = "blue",height = 1,fg='yellow',width = 24).place(x=200,y=210)
    checkout = Button(root, text="CHECK OUT" , command = outData , bg = "blue",height = 1,fg='yellow',width = 24).place(x=20,y=250)
    clear = Button(root, text="CLEAR" , command = clearList , bg = "blue",height = 1,fg='yellow',width = 24).place(x=20,y=210)
    stats = Button(root, text="STATISTICS" ,bg = "blue",height = 1,fg='yellow',width = 24).place(x=200,y=250)  # we have to include statistics command over hear
    clock=Label(root, text = " YOUTUBE VIDEO TITLE", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
    clock.place(x =227 , y=20,height = 50, width = 150)
    dateto=Label(root, text = str(date.today()), font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
    dateto.place(x =227 , y=85,height = 50, width = 150)
    wether=Label(root, text = "WEATHER", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
    wether.place(x =227 , y=150,height = 50, width = 150)

    def times():
        current_time = time.strftime("%H:%M:%S")  #to take the currnt time from system
        clock.config(text=str(current_time))
        clock.after(200,times)
    Thread(target = times).start()
    
    root.mainloop()

   
'''u=int(input("enter"))    
for i in range(u):
    p=str(input())
    a.append(p)
    
print()                
put()
'''
def starts():
    
    imagesPath='images'
    images=[]
    imagesName=[]
    #a=[]
    aname=""
    
    myList=os.listdir(imagesPath)
    #print(myList)
    for x in myList:
        p = cv2.imread(f'{imagesPath}\\{x}')
        #print(p)
        images.append(p)
        imagesName.append(os.path.splitext(x)[0])

    print(imagesName)
    #print(images)
    # to get the encoded test list to use in compare
    def imagesEncodedList(image):
        encodedList=[]
        for frame in image:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = fr.face_encodings(frame)[0]
            encodedList.append(frame)
        return encodedList
    encodedTestList = imagesEncodedList(images)
    print(len(encodedTestList))

   
    

    def go():
        video = cv2.VideoCapture(0)

        while True:
            check,frame = video.read()
            film=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            faceloc = fr.face_locations(film)
            encode = fr.face_encodings(film,faceloc)

            for encoded,faceLoc in zip(encode,faceloc):
                result = fr.compare_faces(encodedTestList,encoded)
                faceDis = fr.face_distance(encodedTestList,encoded)
                #print(faceDis)
                index = np.argmin(faceDis)
                if result[index]:
                    attName=imagesName[index]
                    #print(attName)
                    w,x,y,h=faceLoc
                    cv2.rectangle(frame, (x,y),(h,w),(0,255,0),2)
                    cv2.rectangle(frame, (x,w-35),(h,w),(0,255,0),cv2.FILLED)
                    cv2.putText(frame,attName, (x-146,w-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
                    attendance(attName)
    

            resized = cv2.resize(frame,(int(frame.shape[1]),  int(frame.shape[0])))
            cv2.imshow("THW ATTENDENCE RECORD",resized)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()



    go()


def geton():
    Thread(target = starts).start() 
    Thread(target = put).start()









    
