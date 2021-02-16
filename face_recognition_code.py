import cv2
import numpy as np
import face_recognition as fr  #for face_recognition to work you must first install cmake and dlib package
#because the founder had written the code of pakage in c++ instid of c
import time
import os

#hear i had imported all the nessisaery pakages
# need to get all the images
imagesPath='images' 
images=[]
imagesName=[]

myList=os.listdir(imagesPath) #the folder images in which all images are present. 
#print(myList)
for x in myList:  # to get the images from folder and save it in the images list and the discription on imagesName.
    p = cv2.imread(f'{imagesPath}\\{x}')
    #print(p)
    images.append(p)
    imagesName.append(os.path.splitext(x)[0])

print(imagesName)
#print(images)
# to get the encoded test list to use in compare
def imagesEncodedList(image):  #function return the encoded images. 
    encodedList=[]
    for frame in image:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  # needed to convert the images from bgr to rgb (don't now why, I think it help in identifing the eyes location)
        frame = fr.face_encodings(frame)[0]
        encodedList.append(frame)
    return encodedList
encodedTestList = imagesEncodedList(images)
print(len(encodedTestList))

def attendance(name): # funtion to get  the name of the persion in front of camera.
    pass
    

def go():   # function uses cv2 and face_recognition's function's to open camera and detect and compare faces.
    video = cv2.VideoCapture(0)  # open the camera "0" mean the main camera by changing the value you can shift from one camera to other.

    while True:
        check,frame = video.read()  #it will read the frame(a numpy array) return video frame and chack(boolean).
        film=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #bgr to rgb
        faceloc = fr.face_locations(film)   # give 4 values in return that is the location of faces in frame.
        encode = fr.face_encodings(film,faceloc)  

        for encoded,faceLoc in zip(encode,faceloc):
            result = fr.compare_faces(encodedTestList,encoded)  #compare the faces
            faceDis = fr.face_distance(encodedTestList,encoded)  # give the face correct probablity(lower the value higher the probablity) .
            print(faceDis)
            index = np.argmin(faceDis)
            if result[index]:
                attName=imagesName[index]
                print(attName)
                w,x,y,h=faceLoc
                cv2.rectangle(frame, (x,y),(h,w),(0,255,0),2)  # to display rectangle on the fave location.
                cv2.rectangle(frame, (x,w-35),(h,w),(0,255,0),cv2.FILLED)
                cv2.putText(frame,attName, (x-146,w-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
                attendance(attName)
    

        resized = cv2.resize(frame,(int(frame.shape[1]),  int(frame.shape[0])))
        cv2.imshow("THW ATTENDENCE RECORD",resized)  # to isplay the frames.
        key = cv2.waitKey(1)  # displayed after every 1 milli secound.
        if key == ord('e'):   # if you pres e key in your keyboard the program will stop executing(get out of while loop). 
            break

    video.release() # relise all the windows
    cv2.destroyAllWindows()



go()















        
