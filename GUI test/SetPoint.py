from tkinter import *
import tkinter as ttk
    
    #setting
setPointWin = Tk()
setPointWin.title("Set point: Trajektorijas koordinātu izvēle")
setPointWin.geometry('280x143')
setPointWin.resizable(width=False, height=False)
setPointWin['bg'] = '#2a374a'

        #block grid
            #x axis block
xBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7',width=125,height=20)
xBlockStart.place(x=10,y=10)

xBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7',width=125,height=20)
xBlockEnd.place(x=10,y=60)

xTextStart = ttk.Label(setPointWin, text= 'X Sākumpunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
xTextStart.place(x=25,y=10)

XTextEnd =  ttk.Label(setPointWin, text= 'X Galapunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
XTextEnd.place(x=30,y=60)
    
            #y axis block
yBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7',width=125,height=20)
yBlockStart.place(x=145,y=10)

yBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7',width=125,height=20)
yBlockEnd.place(x=145,y=60)

yTextStart = ttk.Label(setPointWin, text= 'Y Sākumpunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
yTextStart.place(x=160,y=10)

yTextEnd =  ttk.Label(setPointWin, text= 'Y Galapunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
yTextEnd.place(x=170,y=60)

            #input blocks
                #X axis input block
xInputBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8',width=125,height=20)
xInputBlockStart.place(x=10,y=30)
enterX1 = ttk.Entry(setPointWin)
xInputBlockStart.create_window(62,10,window=enterX1)

xInputBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8',width=125,height=20)
xInputBlockEnd.place(x=10,y=80)
enterX2 = ttk.Entry(setPointWin)
xInputBlockEnd.create_window(62,10,window=enterX2)

            #Y axis input block
yInputBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8',width=125,height=20)
yInputBlockStart.place(x=145,y=30)
enterY1 = ttk.Entry(setPointWin)
yInputBlockStart.create_window(62,10,window=enterY1)


yInputBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8',width=125,height=20)
yInputBlockEnd.place(x=145,y=80)
enterY2 = ttk.Entry(setPointWin)
yInputBlockEnd.create_window(62,10,window=enterY2)

        #button
spApplyButton = Button(setPointWin, text="Apply", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat')
spApplyButton.place(x=11,y=110)
spCancelButton = Button(setPointWin, text="Cancel", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat', command=setPointWin.destroy)
spCancelButton.place(x=147, y=110)

setPointWin.mainloop()