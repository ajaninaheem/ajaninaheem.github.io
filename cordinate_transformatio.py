import tkinter as tk
from tkinter import font
import math
form = tk.Tk()
form.geometry('500x400')
form.title('Coordinate Transformation')
layer= tk.Label(form,text="NATIONAL CENTER FOR REMOTE SENSING JOS,PLATEAU STATE, NIGERIA. ",font=('Arial',10),bd=20,bg='green')
layer.place(relx=0.01,rely =0.02,relheight=0.08,relwidth=1)
layer2=tk.Label(form,text="DEPARTMENT OF GROUND RECEIVING STATION ",font=('Arial',10),bd=20,bg='yellow')
layer2.place(relx=0.17,rely =0.1,relheight=0.04,relwidth=0.7)
var=tk.IntVar()
R1=tk.Radiobutton(form,text='DD',variable=var,value=1)
R1.place(relx=0.185,rely =0.14,relheight=0.1,relwidth=0.22,anchor="n")
lbl_geodetic_lat = tk.Label(form, text ='Geodetic Latitude')
geodetic_lat_ent = tk.Entry(form)
lbl_geodetic_lat.place(relx=0.2,rely =0.21,relheight=0.1,relwidth=0.2,anchor="n")
geodetic_lat_ent.place(relx=0.3,rely =0.23,relheight=0.04,relwidth=0.2)
lbl_geodetic_long = tk.Label(form, text='Geodetic Longitude')
geodetic_long_ent = tk.Entry(form)
lbl_geodetic_long.place(relx=0.2,rely =0.3,relheight=0.1,relwidth=0.25,anchor="n")
geodetic_long_ent.place(relx=0.32,rely =0.32,relheight=0.04,relwidth=0.2)

def convert():
    lat = float(geodetic_lat_ent.get())
    long = float(geodetic_long_ent.get())
    a = 6378137.0
    f = 1 / 298.257223563
    e = 2*f - f**2
    hgt=0
    n = a / math.sqrt(1 - e * math.sin(math.radians(lat)) ** 2)
    x = (n + hgt) * math.cos(math.radians(lat)) * math.cos(math.radians(long))
    y = (n + hgt) * math.cos(math.radians(lat)) * math.sin(math.radians(long))
    z = (n * (1 - e) + hgt) * math.sin(math.radians(lat))
    x_format = format(x, '0.3f')
    y_format = format(y, '0.3f')
    ent_X.insert(0, x_format)
    ent_Y.insert(0, y_format)
convertBtn = tk.Button(form, text='Convert', command=convert)
convertBtn.place(relx=0.4,rely =0.4,relheight=0.05,relwidth=0.1)
lbl_X = tk.Label(form, text='X')
ent_X = tk.Entry(form)
lbl_X.place(relx=0.25,rely =0.5,relheight=0.1,relwidth=0.2,anchor="n")
ent_X.place(relx=0.3,rely =0.52,relheight=0.04,relwidth=0.2)
lbl_Y = tk.Label(form, text='Y')
ent_Y = tk.Entry(form)
lbl_Y.place(relx=0.25,rely =0.58,relheight=0.1,relwidth=0.2,anchor="n")
ent_Y.place(relx=0.3,rely =0.62,relheight=0.04,relwidth=0.2)

def clear():
    geodetic_lat_ent.delete(0, 'end')
    geodetic_long_ent.delete(0, 'end')
    ent_X.delete(0, 'end')
    ent_Y.delete(0, 'end')
clearBtn = tk.Button(form, text='Clear', command=clear)
clearBtn.place(relx=0.35,rely =0.68,relheight=0.07,relwidth=0.2)
closeBtn = tk.Button(form, text='Close', command=form.destroy)
closeBtn.place(relx=0.7,rely =0.68,relheight=0.07,relwidth=0.2)
form.mainloop()

