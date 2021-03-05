import cv2
import time
import scipy.misc
import face_recognition
"""
img = cv2.imread("C:\\Users\\hp\\Desktop\\frp\\photo.jpg", 0)

#print(type(img))
#print(img.shape)
resize = cv2.resize(img,(600,600))

cv2.imshow("laged",resize)
cv2.waitKey(2000)
cv2.destroyAllWindows()
"""
"""
fc =cv2.CascadeClassifier(  "C:\\Users\\hp\\Desktop\\frp\\haarcascade_frontalface_default.xml" )
img = cv2.imread("C:\\Users\\hp\\Desktop\\frp\\photo.jpg")


grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = fc.detectMultiScale(grey,scaleFactor = 1.05)#,miniNeighbors =5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img,(int(img.shape[1]/7),  int(img.shape[0]/7)))

cv2.imshow("laged",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a+1
    check,frame = video.read()
    #print(check)
    print(frame)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("image:",grey)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
   
print(a)
video.release()
cv2.destroyAllWindows()
"""
"""
# creating an test inage to test the data
test = face_recognition.load_image_file('photo.jpg')

test = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
faceloc = face_recognition.face_locations(test)[0]
encode = face_recognition.face_encodings(test)[0]
test = cv2.rectangle(test, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,255,0),3)
resized = cv2.resize(test,(int(test.shape[1]/4),  int(test.shape[0]/4)))
cv2.imshow("test",resized)
cv2.waitkey(2000)
cv2.destroyAllWindows()

"""
video = cv2.VideoCapture(0)  #open the camara
#fc =cv2.CascadeClassifier(  "C:\\Users\\hp\\Desktop\\frp\\haarcascade_frontalface_default.xml" )
test = face_recognition.load_image_file('photo.jpg')

test = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
#faceloc = face_recognition.face_locations(test)[0]
encodet = face_recognition.face_encodings(test)[0]
while True:
    check,frame = video.read()  # raed the image and save in frame
    # check return if the data is read or not;
    #print(frame)
    #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #faces = fc.detectMultiScale(grey,scaleFactor = 1.02)#,miniNeighbors =5)
   

    test = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceloc = face_recognition.face_locations(test)[0]
    encode = face_recognition.face_encodings(test)[0]
    result = face_recognition.compare_faces([encode],encodet)
    print(result)
    #faceloc = face_recognition.face_locations(frame)[0]
    """for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
    """
    frame = cv2.rectangle(frame, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,255,0),2)
    resized = cv2.resize(frame,(int(frame.shape[1]),  int(frame.shape[0])))
    cv2.imshow("image:",resized)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

