from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from GUI import geton
from PIL import Image, ImageTk

def on():
    root.mainloop()
    geton()

root = Tk()
root.geometry("400x250")
root.title("STARTING WINDOW")
root.configure(bg = "lightyellow")
root.resizable(False, False)
images=Image.open('p.png')
images = images.resize((202 ,100), Image.ANTIALIAS)
images = ImageTk.PhotoImage(images)

frame1 = Frame(root, bd =2,relief = RIDGE, bg="lightyellow" )
frame1.place(x =20 , y=20,height = 150, width = 360)
f1=Label(frame1, image=images,bg = "black",foreground = "white" )
f1.place(x =0 , y=0,height = 150, width = 360)
f2=Label(root, text = "ATTENDANCE WITH FACE-RECOGNITION", font = "Verdana 11 bold" ,bg = "white",foreground = "black" )
f2.place(x =20 , y=165,height = 40, width = 360)

startit = Button(root, text="START"  , bg = "blue",height = 1,fg='yellow',width = 24, command = on).place(x=20,y=210)
stats = Button(root, text="STATISTICS" ,bg = "blue",height = 1,fg='yellow',width = 24).place(x=200,y=210)

