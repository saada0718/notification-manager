"""
Importing all the modules
"""
from tkinter import *
from tkinter import messagebox
from plyer import  notification
import threading
import time


root = Tk()

"""
    Name: setAtt
    Parameters: None
    Output: None
    Purpose: The purpose of this function is to create the graphical user interface portion of the software
    Author: Saad Ahmed
"""
def setAtt():
    root.configure(bg="black")
    root.geometry("800x400")
    root.resizable(False,False)
    lblName = Label(root,text="Please enter the name of the notification",font=("Helvetica",15),bg="black",fg="white")
    lblName.pack()
    entrName = Entry(root, width=25,font=('Helvetica',12))
    entrName.pack(pady=25)
    lblNotification = Label(root,text="Please enter the notification",font=("Helvetica",15),bg="black",fg="white")
    lblNotification.pack(pady=50)
    entrNotification = Entry(root, width=50,font=('Helvetica',12))
    entrNotification.pack()
    lblTime = Label(root, text="Time between notification (min.)",bg="black",fg="white")
    lblTime.pack(pady=5)
    entrTime = Entry(root,width=5)
    entrTime.pack()
    submit = Button(root,text="submit",width=8,font=('Helvetica',12),command=lambda:myClick(entrName.get(),entrNotification.get(),entrTime.get()))
    submit.pack(pady=15)

"""
    Name: myClick
    Parameters: name, notif, min
    Output: None
    Purpose: This function is called when the my click button is clicked and it checks if the information that the user entered is valid or not and then creates a notfication
             The notification runs in a thread.
    Author: Saad Ahmed
"""
def myClick(name,notif,min):

    if ErrorCheck(name,notif,min):
        thread = threading.Thread(target=createNotification , args=(name,notif,min))
        thread.start()

"""
    Name: ErrorCheck
    Parameters: name, notif, min
    Output: bool
    Purpose: The purpose of this function is to check if the user entered the information when they clicked the submit button and if the information is in the valid format
    Author: Saad Ahmed
"""
def ErrorCheck(name,notif,min):
    if name == "":
        messagebox.showinfo("No name", "Enter the name for the notification")
        return False
    if notif == "":
        messagebox.showinfo("No message", "Enter a notification message")
        return False
    if min == "":
        messagebox.showinfo("No time", "Please enter the time you would like between notfications")
        return False
    elif not (min.isdigit()):
        messagebox.showinfo("Not a number", "Please enter a number")
        return False
    return True

"""
    Name: createNotification    
    Parameters: name, notif, min
    Output: None
    Purpose: The purpose of this function is to create a notification 
    Author: Saad Ahmed
"""
def createNotification(name,notif,min):
    while True:
        notification.notify( title=name, message = notif, timeout=0)
        time.sleep(int(min)*60)
"""
    Name: main
    Parameters: None
    Output: None
    Purpose: This function is the conductor furnction. It call all the helper functions
    Author: Saad Ahmed
"""
def main():
    setAtt()
    root.mainloop()

if __name__ == '__main__':
    main()
