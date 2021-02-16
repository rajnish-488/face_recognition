import cv2
import numpy as np
import face_recognition as fr
import time
import os
# need to get all the images
imagesPath='images'
images=[]
imagesName=[]

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
    pass
    

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
            print(faceDis)
            index = np.argmin(faceDis)
            if result[index]:
                attName=imagesName[index]
                print(attName)
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















        
