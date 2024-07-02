#GUI Application with Radiobutton

# Import Module
from tkinter import *

# create root window

root =Tk()

# root window title and dimension
root.title("Welcome to Sri Lanka")

# set geomtry
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 

menu =Menu(root)
item= Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File',menu=item)
root.config(menu=menu)

lbl1=Label(root,text="Are you a Sri Lankan ?")
lbl1.grid()

txt =Entry(root,width=50)
txt.grid(column =0 , row=1)

# Tkinter string variable
# able to store any string value


lbl2=Label(root,text="")
lbl2.grid(column=0, row=3)
# function to display user text when
# button is clicked#
def clicked():
    answer=txt.get()
    if answer == 'yes' :
     res = " Hey !!! You are Sri Lankan " 
    else:
     res = "OOPS .... You are Not a Sri Lankan "
     
    lbl2.configure(text = res)
   #txt.delete("1.0","end")
    
# button widget with red color text inside
btn = Button(root, text = "Submit" ,
             fg = "red", command=clicked)

# Set Button Grid
btn.grid(column=0, row=2)

# Execute Tkinter
root.mainloop()