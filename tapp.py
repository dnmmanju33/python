from tkinter import *

def loginwind():
    win=Tk()
    win.title('Wellcome to Mtrade')
tapp=Tk()

#================================title=======window==========================================#
tapp.title("MTRADE APP")
width = 400
height = 450
screen_width = tapp.winfo_screenwidth()
screen_height = tapp.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
tapp.geometry("%dx%d+%d+%d" % (width, height, x, y))
tapp.resizable(0, 0)


#==========================================LogoImage============================================#       
logo=PhotoImage(file='C:\\Users\\ADMIN\\Desktop\\download.png')
Label(tapp, image=logo, bg='red').grid(row=0, column=1)
tapp.configure(background="white")


#==========Spacing===============================================================================#
aa0 = Label(tapp, bg='white').grid(row=3,column=0)
aa1 = Label(tapp, bg='white').grid(row=4,column=0)


#==========================lables=================================================================#
a1 = Label(tapp ,text="Username/Client ID", bg='white').grid(row=5,column=0, sticky=E)
b1 = Label(tapp ,text="Password",bg='white').grid(row=6,column=0, sticky=E)
e1 = Entry(tapp).grid(row=5,column=1)
f1 = Entry(tapp,show="*").grid(row=6,column=1)
username_guess = Entry(tapp)
password_guess = Entry(tapp, show="*")


#==========================Button=================================================================#
c1 = Button(tapp, text="LOGIN", command=loginwind).grid(row=7,column=1)

#============================Checkbox=============================================================#
tapp.checkbox = Checkbutton(tapp, text="Keep me logged in", bg='white')
tapp.checkbox.grid(columnspan=1)



d1 = Button(tapp, text="Forget your password?").grid(row=10, column=0, sticky=E)

##============================Spacings===========================================================#
aa2 = Label(tapp, bg='white').grid(row=11,column=0)
aa3 = Label(tapp, bg='white').grid(row=12,column=0)


#===============================Labels/Buttons==================================================#
e1 = Label(tapp, text="or",bg="white", font=10).grid(row=13,column=1)
f1= Label(tapp, text="Create New Account", bg='white').grid(row=14,column=1)
a = Label(tapp, text="Username",bg='white').grid(row=15,column=0,sticky=E)
b = Label(tapp, text="Password", bg='white').grid(row=16,column=0, sticky=E)
e = Entry(tapp).grid(row=15,column=1)
f = Entry(tapp,show="*").grid(row=16,column=1)
c = Button(tapp, text="Click to Create New Account").grid(row=17,column=1)












tapp.mainloop()
