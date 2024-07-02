from tkinter import *


def selection():
    selected_option ="You selected the option" + str(vradio.get())
    label.config(text=selected_option)
# create root window

def clicked():
    answer=str(vradio.get())
    if answer == '1' :
     res = " Hey !!! You are Sri Lankan " 
    else:
     res = "OOPS .... You are Not a Sri Lankan "
    selected_option =res 
    label.configure(text = res)

root =Tk()

# root window title and dimension
root.title("Welcome to Sri Lanka")





# set geomtry
root.geometry('350x200')

lbl1=Label(root,text="Are you a Sri Lankan ?")
lbl1.pack()

vradio =IntVar()
#when command is selection 
#R1=Radiobutton(root,text="Yes" ,variable=vradio ,value=1,command=selection)
#R1.pack(anchor=W)

#when command is clicked
R1=Radiobutton(root,text="Yes" ,variable=vradio ,value=1,command=clicked)
R1.pack(anchor=CENTER)

#when command is selection
#R2=Radiobutton(root,text="No" ,variable=vradio ,value=2,command=selection)
#R2.pack(anchor=W)

#when command is clicked
R2=Radiobutton(root,text="Yes" ,variable=vradio ,value=1,command=clicked)
R2.pack(anchor=CENTER)

 #"""Anchor W will center the text vertically around the reference point, with the left edge of the text box passing through that point, and so on."""
#lbl1.grid()

label = Label(root)
label.pack()



# Execute Tkinter
root.mainloop()