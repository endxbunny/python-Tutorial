from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")

        # 1st image
        img1=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\1.jpg")#insert a image
        img1=img1.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=535,height=130)

        # 2nd image
        img2=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\3.jpg")#insert a image
        img2=img2.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=535,y=0,width=535,height=130)

        # 3rd image
        img3=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\2.jpg")#insert a image
        img3=img3.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1070,y=0,width=535,height=130)


        # bg image
        img4=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\bg2.jpg")#insert a image
        img4=img4.resize((1600,900))#resize((530,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1600,height=700)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        # student button
        img5=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\16.jpg")#insert a image
        img5=img5.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=200,y=280,width=180,height=40)

        # detect face button
        img6=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img6=img6.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=540,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=540,y=280,width=180,height=40)

        # Attendance Face button
        img7=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\5.jpg")#insert a image
        img7=img7.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=900,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=900,y=280,width=180,height=40)

        # help desk button
        img8=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\12.jpg")#insert a image
        img8=img8.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1260,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=1260,y=280,width=180,height=40)

        # train data button
        img9=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\18.jpg")#insert a image
        img9=img9.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=200,y=400,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=200,y=580,width=180,height=40)

        # Photos button
        img10=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img10=img10.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=540,y=400,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=540,y=580,width=180,height=40)

        # Developer button
        img11=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\10.jpg")#insert a image
        img11=img11.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=900,y=400,width=180,height=180)

        b1_1=Button(bg_img,text="Developer",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=900,y=580,width=180,height=40)

        # Exit button
        img12=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\Image-Processing-Project\project images\20.jpg")#insert a image
        img12=img12.resize((220,220))#resize((530,130),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1260,y=400,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",font=("times new roman",14,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=1260,y=580,width=180,height=40)


if _name=="__main_":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()