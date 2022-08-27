from tkinter import *
from tkcalendar import DateEntry
from tkinter import filedialog
from PIL import Image,ImageTk
import datetime
import os

window= Tk()
window.title("Catalogue Search")
height=600
width = 700
cavas= Canvas(window,height= height,width= width)
cavas.pack()
def select():
    window.filename = filedialog.askopenfilename(initialdir='.',filetypes=[("jpeg files", "*.jpeg"), ("all files", "*.*")])
    img=Image.open(window.filename)
    img=img.resize((300,300))
    img= ImageTk.PhotoImage(img)
    im1.image=img
    im1['image']=img
def searchfiles(extension,path):
    start = b2.get_date()
    end = b4.get_date()
    for file in DateEntry.select_range( start,end,end):
        if start < end:
         for r,d,f in os.walk(path):
            for file in f:
                 if file.endswith(extension):
                     lw1.config((lw1.insert(0,r+'\\'+file)))
            print(file)
            
def open_file():
    opn=lw1.get(lw1.curselection()[0])
    img=Image.open(opn)
    img=img.resize((300,300))
    img= ImageTk.PhotoImage(img)
    im1.config(image=img)
    im1.image=img

def exit():
    window.destroy()
b1 = Label(window, text= "Start Date (dd-mm-yy)")
b1.place(relx=0.12,rely =0.05,relheight=0.1,relwidth=0.2,anchor="n")
date_text = StringVar()
b2 = DateEntry(window,textvariable=date_text,date_pattern="dd-mm-yy")
b2.place(relx=0.12,rely = 0.12,relheight=0.05,relwidth=0.2,anchor="n")
b3 = Label(window, text= "End Date (dd-mm-yy)")
b3.place(relx=0.12,rely = 0.2,relheight=0.04,relwidth=0.2,anchor="n")
date_to =StringVar()
b4 = DateEntry(window, textvariable=date_to,selectmode='day',date_pattern="dd-mm-yy")
b4.place(relx=0.12,rely = 0.25,relheight=0.04,relwidth=0.2,anchor="n")
b5 = Button(window, text= "Search",command=lambda :searchfiles('.tif',('C:\\Share')))
b5.place(relx=0.12,rely = 0.3,relheight=0.04,relwidth=0.07,anchor="n")
lw1 = Listbox(window)
lw1.place(relx=0.27,rely = 0.35,relheight=0.5,relwidth=0.5,anchor ='n')
lw1.bind("<<Double-Button>>",open_file)
scr=Scrollbar(lw1)
scr.place(relx=0.47,relheight=1,relwidth=0.08)
lw1.config(lw1,yscrollcommand=scr.set)
scr.configure(command=lw1.yview)
b6 = Button(window, text= "Previous")
b6.place(relx=0.27,rely=0.88,relheight=0.1)
b7 = Button(window, text= "Select Folder",command=select)
b7.place(relx=0.38,rely = 0.88,relheight=0.1,relwidth=0.2)
b8= Button(window, text="Next")
b8.place(relx=0.65,rely = 0.88,relheight=0.1,relwidth=0.1)
b9= Button(window, text="Exit",command=exit)
b9.place(relx=0.85,rely = 0.88,relheight=0.1,relwidth=0.1)
lf1= Frame(window,bd=10)
lf1.place(relx=0.28,rely = 0.1,relheight=0.78,relwidth=0.7)
im1= Label(lf1,bd=10,bg="black")
im1.place(relheight=1,relwidth=1)
b10 = Button(lf1, text= "zoom(+)")
b10.place(relx=0.7,rely=0.01,relheight=0.07,relwidth=0.13)
b11 = Button(lf1, text= "zoom(-)")
b11.place(relx=0.85,rely=0.01,relheight=0.07,relwidth=0.13,anchor="nw")
window.mainloop()

print(dir(DateEntry))