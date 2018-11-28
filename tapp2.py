from tkinter import *
import os   


def dellogwin():
  successwin.destroy()
 
def delpasswin():
  passwindow.destroy()
 
def emptyspacewin():
  emptyspace.destroy()


########################login successful window#########(5)
def login_sucess():
  global successwin
  successwin = Toplevel(window)
  successwin.title("Login Window")
  successwin.geometry("150x100")
  Label(successwin, text = "Thank You Successfully Logged").pack()
  Button(successwin, text = "OK", command =dellogwin).pack()


############################wrong password window###############(6) 
def password_not_recognised():
  global passwindow
  passwindow = Toplevel(window)
  passwindow.title("Login Window")
  passwindow.geometry("150x100")
  Label(passwindow, text = "Password Error Please Try Agian").pack()
  Button(passwindow, text = "OK", command =delpasswin).pack()
 
#######################Not entered anything in username n password#(7)
def user_not_found():
  global emptyspace
  emptyspace = Toplevel(window)
  emptyspace.title("Login Window")
  emptyspace.geometry("150x100")
  Label(emptyspace, text = "Enter Username and Password").pack()
  Button(emptyspace, text = "OK", command =emptyspacewin).pack()


####################registered user##############(4)
def register_user():
  print("working")
   
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(regwindow, text = "Registration Successful", fg = "green" ,font = ("calibri", 11)).pack()


######################login verification###################(5)
def login_verify():
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
   


#########REGISTERATION SCREEN##################(2)
def register():
  global regwindow
  regwindow = Toplevel(window)
  regwindow.title("App Registeration")
  regwindow.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(regwindow, text = "Please enter details below").pack()
  Label(regwindow, text = "").pack()

  Label(regwindow, text = "Username * ").pack()
  username_entry = Entry(regwindow, textvariable = username)
  username_entry.pack()
  
  Label(regwindow, text = "Password * ").pack()
  password_entry =  Entry(regwindow, textvariable = password)
  password_entry.pack()
  
  Label(regwindow, text = "").pack()
  Button(regwindow, text = "Register", width = 10, height = 1, command = register_user).pack()
 

#############################Login screen###################(3)
def login():
  global logwindow
  logwindow = Toplevel(window)
  logwindow.title("Login")
  logwindow.geometry("300x250")
  Label(logwindow, text = "Please enter details below to login").pack()
  Label(logwindow, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(logwindow, text = "Username * ").pack()
  username_entry1 = Entry(logwindow, textvariable = username_verify)
  username_entry1.pack()
  Label(logwindow, text = "").pack()
  Label(logwindow, text = "Password * ").pack()
  password_entry1 = Entry(logwindow, textvariable = password_verify)
  password_entry1.pack()
  Label(logwindow, text = "").pack()
  Button(logwindow, text = "Login", width = 10, height = 1, command = login_verify).pack()


###########ENTRY WINDOW#############(1)
def main_window():
  global window
  window = Tk()
  window.geometry("300x400")
  window.title("MTRADE APP")
  logo=PhotoImage(file='C:\\Users\\ADMIN\\Desktop\\download.png')
  Label(window, image=logo, bg='red').pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  window.checkbox = Checkbutton(window, text="Keep me logged in", bg='white').pack()
  fbutton = Button(window, text="Forget your password?").pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
 
  window.mainloop()
 
main_window()
