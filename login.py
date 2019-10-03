import tkinter
from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import ttk
import check
import main
import moviepy_test




class lis(Frame):
    def __init__(self,li,master=NONE):
        Frame.__init__(self,master)
        self.li=li
        self.pack(padx=80,pady=20)
        self.createWidget2()
    def createWidget2(self):
        for i in range(len(self.li)):
            Label(self,text=self.li[i]).grid(row=i,column=0,pady=8)



class login(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack(padx=60,pady=60)
        self.createwidget()

    def createwidget(self):

        self.imgHi=ImageTk.PhotoImage(Image.open(r"D:\python\minor1\chat.ico"))
        self.HiLabel=Label(self,image=self.imgHi).grid(row=0,column=0,padx=20,pady=20)

        self.number=StringVar()
        self.comboBox=ttk.Combobox(self)
        self.comboBox['values']=("User","Admin")
        self.comboBox.current(0)
        self.comboBox.grid(row=0,column=1,columnspan=1,padx=10,pady=10)

        def funcSmileyImgEntry(event):
            self.imgCool = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\cool2.ico"))
            self.ImgLabel2 = Label(self, image=self.imgCool,borderwidth=4,bg="lavender")
            self.ImgLabel2.grid(row=0, column=2, padx=20, pady=20)

        self.img = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\cool4.ico"))
        self.ImgLabel = Button(self, text=":)",borderwidth=4)
        self.ImgLabel.grid(row=0, column=2, padx=20, pady=20)
        self.ImgLabel.bind("<Enter>",funcSmileyImgEntry)


        self.Username=Label(self,text="Enter username:",bg="antiquewhite")
        self.Username.grid(row=1,column=0,columnspan=2,sticky=W,padx=20,pady=20)
        self.userEntryvar=StringVar()
        self.userEntryvar.set("Enter_username")
        self.userEntry=Entry(self,textvariable=self.userEntryvar)
        self.userEntry.grid(row=1,column=2,columnspan=2,sticky=E,padx=20,pady=20)

        self.pwd = Label(self, text="Enter password:",bg="antiquewhite")
        self.pwd.grid(row=2, column=0,columnspan=2,sticky=W,padx=20,pady=20)
        self.userpwdvar = StringVar()
        self.userpwdvar.set("Enter_password")
        self.userPwd = Entry(self, textvariable=self.userpwdvar,show="*")
        self.userPwd.grid(row=2,column=2,columnspan=2,sticky=E,padx=20,pady=20)

        def loginBtnEntry(event):
            self.loginBtn.config(bg="lavender")
            self.loginBtn.config(borderwidth=4)

        def loginBtnLeave(event):
            self.loginBtn.config(bg="antiquewhite")
            self.loginBtn.config(borderwidth=2)


        self.loginBtn=Button(self,text="Login",command=self.funcBtnLogin,width=8,borderwidth=2)
        self.loginBtn.grid(row=3,column=2,columnspan=2,pady=20,padx=20)
        self.loginBtn.bind("<Enter>",loginBtnEntry)
        self.loginBtn.bind("<Leave>",loginBtnLeave)

        self.orLabel=Label(self,text="OR",bg="antiquewhite").grid(row=4,column=0,columnspan=2,padx=20,pady=20)

        def funcFbBtnEntry(event):
            self.FbLoginBtn.config(bg="lavender")
            self.FbLoginBtn.config(borderwidth=4)

        def funcFbBtnLeave(event):
            self.FbLoginBtn.config(bg="antiquewhite")
            self.FbLoginBtn.config(borderwidth=2)

        self.FbLabel=Label(self,text="Login With Facebook:",bg="antiquewhite").grid(row=5,column=0,padx=20,pady=20,sticky=W)

        self.imgfb = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\facebook.ico"))
        self.FbLoginBtn = Button(self, image=self.imgfb, command=self.funcFbBtn,borderwidth=2)
        self.FbLoginBtn.grid(row=5, column=2,sticky=E,padx=20,pady=20)
        self.FbLoginBtn.bind("<Enter>",funcFbBtnEntry)
        self.FbLoginBtn.bind("<Leave>",funcFbBtnLeave)


    def funcBtnLogin(self):

        if(check.check(self.comboBox.get(),self.userEntryvar.get(),self.userpwdvar.get())==True):
            if(self.comboBox.get()=='User'):

                self.top=Toplevel()
                self.top.title("Hello:"+self.userEntryvar.get())
                self.top.configure(background="#D5D8DC")
                self.top.wm_iconbitmap(r"D:\python\minor1\Icon2.ico")

                def uploadBtnEntry(event):
                    self.ImgUplaodBtn.config(bg="lavender")
                    self.ImgUplaodBtn.config(borderwidth=4)

                def uploadBtnLeave(event):
                    self.ImgUplaodBtn.config(bg="antiquewhite")
                    self.ImgUplaodBtn.config(borderwidth=2)

                def nearbyBtnEntry(event):
                    self.ImgNearbyBtn.config(bg="lavender")
                    self.ImgNearbyBtn.config(borderwidth=4)

                def nearbyBtnLeave(event):
                    self.ImgNearbyBtn.config(bg="antiquewhite")
                    self.ImgNearbyBtn.config(borderwidth=2)

                def playBtnEntry(event):
                    self.ImgPlayBtn.config(bg="lavender")
                    self.ImgPlayBtn.config(borderwidth=4)

                def playBtnLeave(event):
                    self.ImgPlayBtn.config(bg="antiquewhite")
                    self.ImgPlayBtn.config(borderwidth=2)

                def funcUploadLabelEntry(event):
                    self.uploadLabel.config(bg="lavender")

                def funcUploadLabelLeave(event):
                    self.uploadLabel.config(bg="antiquewhite")

                def funcNearbyLabelEntry(event):
                    self.nearbyLabel.config(bg="lavender")

                def funcNearbyLabelLeave(event):
                    self.nearbyLabel.config(bg="antiquewhite")

                def funcPlayLabelEntry(event):
                    self.playLabel.config(bg="lavender")

                def funcPlayLabelLeave(event):
                    self.playLabel.config(bg="antiquewhite")


                self.uploadLabel = Label(self.top, text="Upload:")
                self.uploadLabel.grid(row=0, column=0,padx=20,pady=20,sticky=W)
                self.uploadLabel.bind("<Enter>",funcUploadLabelEntry)
                self.uploadLabel.bind("<Leave>", funcUploadLabelLeave)

                # self.imgUpOld = Image.open(r"D:\python\minor1\bt_up.ico") #resizing images
                # self.imgUp=self.imgUpOld.resize((50,50), Image.ANTIALIAS) #resizing images
                self.imgUpload=ImageTk.PhotoImage(Image.open(r"D:\python\minor1\bt_up.ico"))
                self.ImgUplaodBtn = Button(self.top, image=self.imgUpload, command=self.funcBtnUpload,borderwidth=2)
                self.ImgUplaodBtn.grid(row=0, column=1, padx=20, pady=20)
                self.ImgUplaodBtn.bind("<Enter>", uploadBtnEntry)
                self.ImgUplaodBtn.bind("<Leave>", uploadBtnLeave)

                self.nearbyLabel = Label(self.top, text="Nearby:")
                self.nearbyLabel.grid(row=1, column=0, padx=20, pady=20, sticky=W)
                self.nearbyLabel.bind("<Enter>", funcNearbyLabelEntry)
                self.nearbyLabel.bind("<Leave>", funcNearbyLabelLeave)

                self.imgNearby = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\places.ico"))
                self.ImgNearbyBtn = Button(self.top, image=self.imgNearby, borderwidth=2, command=self.funcNearbyBtn)
                self.ImgNearbyBtn.grid(row=1, column=1, padx=20, pady=20)
                self.ImgNearbyBtn.bind("<Enter>", nearbyBtnEntry)
                self.ImgNearbyBtn.bind("<Leave>", nearbyBtnLeave)

                self.playLabel = Label(self.top, text="Play:")
                self.playLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
                self.playLabel.bind("<Enter>", funcPlayLabelEntry)
                self.playLabel.bind("<Leave>", funcPlayLabelLeave)

                self.imgPlay = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\play.ico"))
                self.ImgPlayBtn = Button(self.top, image=self.imgPlay, borderwidth=2, command=self.funcPlayBtn)
                self.ImgPlayBtn.grid(row=2, column=1, padx=20, pady=20)
                self.ImgPlayBtn.bind("<Enter>", playBtnEntry)
                self.ImgPlayBtn.bind("<Leave>", playBtnLeave)

            else:
                self.top = Toplevel()
                self.top.title("Hello:" + self.userEntryvar.get())
                self.top.configure(background="#D5D8DC")
                self.top.wm_iconbitmap(r"D:\python\minor1\Icon2.ico")

                def uploadBtnEntry(event):
                    self.ImgUplaodBtn.config(bg="lavender")
                    self.ImgUplaodBtn.config(borderwidth=4)

                def uploadBtnLeave(event):
                    self.ImgUplaodBtn.config(bg="antiquewhite")
                    self.ImgUplaodBtn.config(borderwidth=2)

                def nearbyBtnEntry(event):
                    self.ImgNearbyBtn.config(bg="lavender")
                    self.ImgNearbyBtn.config(borderwidth=4)

                def nearbyBtnLeave(event):
                    self.ImgNearbyBtn.config(bg="antiquewhite")
                    self.ImgNearbyBtn.config(borderwidth=2)

                def playBtnEntry(event):
                    self.ImgPlayBtn.config(bg="lavender")
                    self.ImgPlayBtn.config(borderwidth=4)

                def playBtnLeave(event):
                    self.ImgPlayBtn.config(bg="antiquewhite")
                    self.ImgPlayBtn.config(borderwidth=2)

                def updateBtnEntry(event):
                    self.ImgUpdateBtn.config(bg="lavender")
                    self.ImgUpdateBtn.config(borderwidth=4)

                def updateBtnLeave(event):
                    self.ImgUpdateBtn.config(bg="antiquewhite")
                    self.ImgUpdateBtn.config(borderwidth=2)

                def funcUploadLabelEntry(event):
                    self.uploadLabel.config(bg="lavender")

                def funcUploadLabelLeave(event):
                    self.uploadLabel.config(bg="antiquewhite")

                def funcNearbyLabelEntry(event):
                    self.nearbyLabel.config(bg="lavender")

                def funcNearbyLabelLeave(event):
                    self.nearbyLabel.config(bg="antiquewhite")

                def funcPlayLabelEntry(event):
                    self.playLabel.config(bg="lavender")

                def funcPlayLabelLeave(event):
                    self.playLabel.config(bg="antiquewhite")

                def funcUpdateLabelEntry(event):
                    self.updateLabel.config(bg="lavender")

                def funcUpdateLabelLeave(event):
                    self.updateLabel.config(bg="antiquewhite")


                self.uploadLabel = Label(self.top, text="Upload:")
                self.uploadLabel.grid(row=0, column=0, padx=20, pady=20, sticky=W)
                self.uploadLabel.bind("<Enter>", funcUploadLabelEntry)
                self.uploadLabel.bind("<Leave>", funcUploadLabelLeave)

                self.imgUpload = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\bt_up.ico"))
                self.ImgUplaodBtn = Button(self.top, image=self.imgUpload, command=self.funcBtnUpload, borderwidth=2)
                self.ImgUplaodBtn.grid(row=0, column=1, padx=20, pady=20)
                self.ImgUplaodBtn.bind("<Enter>", uploadBtnEntry)
                self.ImgUplaodBtn.bind("<Leave>", uploadBtnLeave)

                self.nearbyLabel = Label(self.top, text="Nearby:")
                self.nearbyLabel.grid(row=1, column=0, padx=20, pady=20, sticky=W)
                self.nearbyLabel.bind("<Enter>", funcNearbyLabelEntry)
                self.nearbyLabel.bind("<Leave>", funcNearbyLabelLeave)

                self.imgNearby = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\places.ico"))
                self.ImgNearbyBtn = Button(self.top, image=self.imgNearby, borderwidth=2,command=self.funcNearbyBtn)
                self.ImgNearbyBtn.grid(row=1, column=1, padx=20, pady=20)
                self.ImgNearbyBtn.bind("<Enter>", nearbyBtnEntry)
                self.ImgNearbyBtn.bind("<Leave>", nearbyBtnLeave)

                self.playLabel = Label(self.top, text="Play:")
                self.playLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
                self.playLabel.bind("<Enter>", funcPlayLabelEntry)
                self.playLabel.bind("<Leave>", funcPlayLabelLeave)

                self.imgPlay = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\play.ico"))
                self.ImgPlayBtn = Button(self.top, image=self.imgPlay, borderwidth=2, command=self.funcPlayBtn)
                self.ImgPlayBtn.grid(row=2, column=1, padx=20, pady=20)
                self.ImgPlayBtn.bind("<Enter>", playBtnEntry)
                self.ImgPlayBtn.bind("<Leave>", playBtnLeave)

                self.updateLabel = Label(self.top, text="Update:")
                self.updateLabel.grid(row=3, column=0, padx=20, pady=20, sticky=W)
                self.updateLabel.bind("<Enter>", funcUpdateLabelEntry)
                self.updateLabel.bind("<Leave>", funcUpdateLabelLeave)

                self.imgUpdate = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\update.ico"))
                self.ImgUpdateBtn = Button(self.top, image=self.imgUpdate, borderwidth=2 , command=self.funcUpdateBtn)
                self.ImgUpdateBtn.grid(row=3, column=1, padx=20, pady=20)
                self.ImgUpdateBtn.bind("<Enter>", updateBtnEntry)
                self.ImgUpdateBtn.bind("<Leave>", updateBtnLeave)

        else:
            tkinter.messagebox.showinfo('Error','Not recognized!!')


    def funcBtnUpload(self):
        self.path=filedialog.askopenfile()
        self.final_name = main.get_name(self.path.name)
        tkinter.messagebox.showinfo('Know your position', message='You are in--' + str(self.final_name))

    def funcNearbyBtn(self):
        self.li = main.recommend(self.final_name)
        self.root2 = Toplevel()
        # print(self.li)
        self.window_v2 = lis(self.li, self.root2)

    def funcPlayBtn(self):
        moviepy_test.vid_play(self.final_name)

    def funcUpdateBtn(self):
        boole = main.update()
        if (boole):
            tkinter.messagebox.showinfo(message='Updated successfully!')

    def funcFbBtn(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\pathak\AppData\Local\Programs\Python\Python36\Scripts") #chromedriver for chrome browsing (path only required if chromedriver.exe not in default directoy)
        driver.get("https://www.facebook.com/") #url of site
        driver.find_element_by_xpath("//input[@id='email']").send_keys(self.userEntryvar.get()) #matching elements with their x_paths in original page
        driver.find_element_by_xpath("//input[@id='pass']").send_keys(self.userpwdvar.get()) #x_path = xml path(//tag_name[@attribute="value"]])
        driver.find_element_by_xpath("//input[starts-with(@id, 'u_0_')][@value='Log In']").click() #send_keys = entering data send to login page
        #.click() = moves to next page
        if("Log" in driver.title):
            tkinter.messagebox.showinfo("Oops!","Sorry,Wrong Credentials!")
            driver.close()
        else:
            tkinter.messagebox.showinfo("Info!","Logged in successfully!")
            driver.close()
            if (check.check(self.comboBox.get(), self.userEntryvar.get(), self.userpwdvar.get()) == False):

                self.top = Toplevel()
                self.top.title("Hello:" + self.userEntryvar.get())
                self.top.configure(background="#D5D8DC")
                self.top.wm_iconbitmap(r"D:\python\minor1\Icon2.ico")

                def uploadBtnEntry(event):
                    self.ImgUplaodBtn.config(bg="lavender")
                    self.ImgUplaodBtn.config(borderwidth=4)

                def uploadBtnLeave(event):
                    self.ImgUplaodBtn.config(bg="antiquewhite")
                    self.ImgUplaodBtn.config(borderwidth=2)

                def nearbyBtnEntry(event):
                    self.ImgNearbyBtn.config(bg="lavender")
                    self.ImgNearbyBtn.config(borderwidth=4)

                def nearbyBtnLeave(event):
                    self.ImgNearbyBtn.config(bg="antiquewhite")
                    self.ImgNearbyBtn.config(borderwidth=2)

                def playBtnEntry(event):
                    self.ImgPlayBtn.config(bg="lavender")
                    self.ImgPlayBtn.config(borderwidth=4)

                def playBtnLeave(event):
                    self.ImgPlayBtn.config(bg="antiquewhite")
                    self.ImgPlayBtn.config(borderwidth=2)

                def funcUploadLabelEntry(event):
                    self.uploadLabel.config(bg="lavender")

                def funcUploadLabelLeave(event):
                    self.uploadLabel.config(bg="antiquewhite")

                def funcNearbyLabelEntry(event):
                    self.nearbyLabel.config(bg="lavender")

                def funcNearbyLabelLeave(event):
                    self.nearbyLabel.config(bg="antiquewhite")

                def funcPlayLabelEntry(event):
                    self.playLabel.config(bg="lavender")

                def funcPlayLabelLeave(event):
                    self.playLabel.config(bg="antiquewhite")

                self.uploadLabel = Label(self.top, text="Upload:")
                self.uploadLabel.grid(row=0, column=0, padx=20, pady=20, sticky=W)
                self.uploadLabel.bind("<Enter>", funcUploadLabelEntry)
                self.uploadLabel.bind("<Leave>", funcUploadLabelLeave)

                self.imgUpload = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\bt_up.ico"))
                self.ImgUplaodBtn = Button(self.top, image=self.imgUpload, command=self.funcBtnUpload, borderwidth=2)
                self.ImgUplaodBtn.grid(row=0, column=1, padx=20, pady=20)
                self.ImgUplaodBtn.bind("<Enter>", uploadBtnEntry)
                self.ImgUplaodBtn.bind("<Leave>", uploadBtnLeave)

                self.nearbyLabel = Label(self.top, text="Nearby:")
                self.nearbyLabel.grid(row=1, column=0, padx=20, pady=20, sticky=W)
                self.nearbyLabel.bind("<Enter>", funcNearbyLabelEntry)
                self.nearbyLabel.bind("<Leave>", funcNearbyLabelLeave)

                self.imgNearby = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\places.ico"))
                self.ImgNearbyBtn = Button(self.top, image=self.imgNearby, borderwidth=2)
                self.ImgNearbyBtn.grid(row=1, column=1, padx=20, pady=20)
                self.ImgNearbyBtn.bind("<Enter>", nearbyBtnEntry)
                self.ImgNearbyBtn.bind("<Leave>", nearbyBtnLeave)

                self.playLabel = Label(self.top, text="Play:")
                self.playLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
                self.playLabel.bind("<Enter>", funcPlayLabelEntry)
                self.playLabel.bind("<Leave>", funcPlayLabelLeave)

                self.imgPlay = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\play.ico"))
                self.ImgPlayBtn = Button(self.top, image=self.imgPlay, borderwidth=2)
                self.ImgPlayBtn.grid(row=2, column=1, padx=20, pady=20)
                self.ImgPlayBtn.bind("<Enter>", playBtnEntry)
                self.ImgPlayBtn.bind("<Leave>", playBtnLeave)

            else:
                self.top = Toplevel()
                self.top.title("Hello:" + self.userEntryvar.get())
                self.top.configure(background="#D5D8DC")
                self.top.wm_iconbitmap(r"D:\python\minor1\Icon2.ico")

                def uploadBtnEntry(event):
                    self.ImgUplaodBtn.config(bg="lavender")
                    self.ImgUplaodBtn.config(borderwidth=4)

                def uploadBtnLeave(event):
                    self.ImgUplaodBtn.config(bg="antiquewhite")
                    self.ImgUplaodBtn.config(borderwidth=2)

                def nearbyBtnEntry(event):
                    self.ImgNearbyBtn.config(bg="lavender")
                    self.ImgNearbyBtn.config(borderwidth=4)

                def nearbyBtnLeave(event):
                    self.ImgNearbyBtn.config(bg="antiquewhite")
                    self.ImgNearbyBtn.config(borderwidth=2)

                def playBtnEntry(event):
                    self.ImgPlayBtn.config(bg="lavender")
                    self.ImgPlayBtn.config(borderwidth=4)

                def playBtnLeave(event):
                    self.ImgPlayBtn.config(bg="antiquewhite")
                    self.ImgPlayBtn.config(borderwidth=2)

                def updateBtnEntry(event):
                    self.ImgUpdateBtn.config(bg="lavender")
                    self.ImgUpdateBtn.config(borderwidth=4)

                def updateBtnLeave(event):
                    self.ImgUpdateBtn.config(bg="antiquewhite")
                    self.ImgUpdateBtn.config(borderwidth=2)

                def funcUploadLabelEntry(event):
                    self.uploadLabel.config(bg="lavender")

                def funcUploadLabelLeave(event):
                    self.uploadLabel.config(bg="antiquewhite")

                def funcNearbyLabelEntry(event):
                    self.nearbyLabel.config(bg="lavender")

                def funcNearbyLabelLeave(event):
                    self.nearbyLabel.config(bg="antiquewhite")

                def funcPlayLabelEntry(event):
                    self.playLabel.config(bg="lavender")

                def funcPlayLabelLeave(event):
                    self.playLabel.config(bg="antiquewhite")

                def funcUpdateLabelEntry(event):
                    self.updateLabel.config(bg="lavender")

                def funcUpdateLabelLeave(event):
                    self.updateLabel.config(bg="antiquewhite")

                self.uploadLabel = Label(self.top, text="Upload:")
                self.uploadLabel.grid(row=0, column=0, padx=20, pady=20, sticky=W)
                self.uploadLabel.bind("<Enter>", funcUploadLabelEntry)
                self.uploadLabel.bind("<Leave>", funcUploadLabelLeave)

                self.imgUpload = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\bt_up.ico"))
                self.ImgUplaodBtn = Button(self.top, image=self.imgUpload, command=self.funcBtnUpload, borderwidth=2)
                self.ImgUplaodBtn.grid(row=0, column=1, padx=20, pady=20)
                self.ImgUplaodBtn.bind("<Enter>", uploadBtnEntry)
                self.ImgUplaodBtn.bind("<Leave>", uploadBtnLeave)

                self.nearbyLabel = Label(self.top, text="Nearby:")
                self.nearbyLabel.grid(row=1, column=0, padx=20, pady=20, sticky=W)
                self.nearbyLabel.bind("<Enter>", funcNearbyLabelEntry)
                self.nearbyLabel.bind("<Leave>", funcNearbyLabelLeave)

                self.imgNearby = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\places.ico"))
                self.ImgNearbyBtn = Button(self.top, image=self.imgNearby, borderwidth=2)
                self.ImgNearbyBtn.grid(row=1, column=1, padx=20, pady=20)
                self.ImgNearbyBtn.bind("<Enter>", nearbyBtnEntry)
                self.ImgNearbyBtn.bind("<Leave>", nearbyBtnLeave)

                self.playLabel = Label(self.top, text="Play:")
                self.playLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
                self.playLabel.bind("<Enter>", funcPlayLabelEntry)
                self.playLabel.bind("<Leave>", funcPlayLabelLeave)

                self.imgPlay = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\play.ico"))
                self.ImgPlayBtn = Button(self.top, image=self.imgPlay, borderwidth=2)
                self.ImgPlayBtn.grid(row=2, column=1, padx=20, pady=20)
                self.ImgPlayBtn.bind("<Enter>", playBtnEntry)
                self.ImgPlayBtn.bind("<Leave>", playBtnLeave)

                self.updateLabel = Label(self.top, text="Update:")
                self.updateLabel.grid(row=3, column=0, padx=20, pady=20, sticky=W)
                self.updateLabel.bind("<Enter>", funcUpdateLabelEntry)
                self.updateLabel.bind("<Leave>", funcUpdateLabelLeave)

                self.imgUpdate = ImageTk.PhotoImage(Image.open(r"D:\python\minor1\update.ico"))
                self.ImgUpdateBtn = Button(self.top, image=self.imgUpdate, borderwidth=2)
                self.ImgUpdateBtn.grid(row=3, column=1, padx=20, pady=20)
                self.ImgUpdateBtn.bind("<Enter>", updateBtnEntry)
                self.ImgUpdateBtn.bind("<Leave>", updateBtnLeave)






window=Tk()
window.configure(background="#1C2833")
window.title("Welcome")
window.wm_iconbitmap(r"D:\python\minor1\Icon2.ico")
lf=login(window)
window.mainloop()