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
class facerek:

    def __init__(self,root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("GANDUA KA LIYA ATTENDENCE")
        self.root.configure(bg = "lightyellow")
        self.root.resizable(False, False)
        
        """ self.frame1 = Frame(self.root, bd =2,relief = RIDGE, bg="lightyellow" )
        self.frame1.place(x =10 , y=140,height = 200, width = 637)
        self.f1=Label(self.frame1, text = " YOUTUBE VIDEO TITLE  ", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
        self.f1.place(x=0, y=0 ,width = 635,height = 200)"""
        self.serch = Button(self.root, text="TAKE ATTENDEBCE" , command = self.putData , bg = "blue",height = 1,fg='yellow',width = 20).place(x=130,y=200)
    def attendance(name):
        #aname= name
        if(name not in a):
            a.append(name)
            print(a)

    def putData(self):
        print(a)
        current_time = time.strftime("%H:%M:%S")
        dateToday= date.today()
        file=open("att.text", "a")
        for x in a:
            file.write(x+"\t"+current_time+"\t"+str(dateToday))
            file.write("\n")
        file.close()
        a.clear()
        print(a)

    def clearList():
        a.clear()
        print(a)
        
       


def put():
    root = Tk()
    yo = facerek(root)
    root.mainloop()
u=int(input("enter"))    
for i in range(u):
    p=str(input())
    a.append(p)
print()                   
put()
'''
def start():
    
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

    def attendance(name):
        #aname= name
        if(name not in a):
            a.append(name)
            print(a)
    
    def getName():
        return a
    def getname():
        return aname
    def clear():
        a=[]
    

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
                    facerek.attendance(attName)
    

            resized = cv2.resize(frame,(int(frame.shape[1]),  int(frame.shape[0])))
            cv2.imshow("THW ATTENDENCE RECORD",resized)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()



    go()



Thread(target = start).start() 
Thread(target = put).start()


'''






    
