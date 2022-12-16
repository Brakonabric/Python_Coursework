from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import time 

###BREZENHEMA ALGORITMA DAĻA
motion = []
def DrawLine(x1,y1,x2,y2,Draw):
    drawX = []
    drawY = []
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if x1<x2:
        xs=1 
    else:
        xs=-1
    if y1<y2:
        ys=1
    else:
        ys=-1
    x=x1
    y=y1
    p=2*dy-dx   
    
    if dx>dy:
        #sakumpunkts
        rootPlotArea.create_oval(x-5,y-5,x+5,y+5,tags="toDraw",fill="#b76b32",outline="#b76b32")
        while x<x2:
            x=x+xs
            if p > 0:
                y=y+ys
                p=p+2*dy-2*dx
            else:
                p=p+2*dy
            rootPlotArea.create_oval(x,y,x,y,tags="toDraw",fill="#f58220",outline="#f58220")
            motion.append(x)
            motion.append(y)
        #galapunkts
        rootPlotArea.create_oval(x-5,y-5,x+5,y+5,tags="toDraw",fill="#b76b32",outline="#b76b32")
            
    else:
        #sakumpunkts
        rootPlotArea.create_oval(x-5,y-5,x+5,y+5,tags="toDraw",fill="#b76b32",outline="#b76b32")
        while y!=y2:
            y=y+ys
            if p > 0:
                x=x+xs
                p=p+2*dx-2*dy
            else:
                p=p+2*dx
            rootPlotArea.create_oval(x,y,x,y,tags="toDraw",fill="#f58220",outline="#f58220")
            motion.append(x)
            motion.append(y)
        #galapunkts
        rootPlotArea.create_oval(x-5,y-5,x+5,y+5,tags="toDraw",fill="#b76b32",outline="#b76b32")
    createMotion()
    return

###GUI DAĻA

#Root win settings
root = Tk()
root['bg'] = '#2a374a'
root.title('Linass Jokšass 221RDB522')
root.geometry('1200x800')
root.resizable(width=False, height=False)

#Root Win construction
rootHeader = ttk.Canvas(root, highlightthickness=0,bg='#5159a7', width=1200, height=40)
rootHeader.place(x=0, y=0)

rootHeaderText = ttk.Label(root, text='BREZENHEMA ALGORITMA IZMANTOŠANA 2D OBJEKTA PĀRVIETOŠANAI.', font=('arial', 16, 'bold'), fg='#ffffff', bg='#5159a7')
rootHeaderText.place(x=230, y=5)

rootPlotArea = ttk.Canvas(root, highlightthickness=0, bg='#bacae8', width=1100, height=550)
rootPlotArea.place(x=80, y=120)

#Grid
xGrid = 0
while xGrid <= 22:
    yGrid = 0
    while yGrid <= 11:
        rootPlotArea.create_oval(-3+(50*xGrid),-3+(50*yGrid),3+(50*xGrid),3+(50*yGrid),fill="#97a5bf",outline="#97a5bf")
        yGrid+=1
    xGrid+=1

#xScale
xScale = 0
while xScale <= 22:
    ttk.Label(root, text = (xScale*50),font=('arial', 11, 'bold'), fg='#ffffff', bg='#2a374a').place(x=(62+(xScale*50)), y=690)
    xScale+=1

#yScale
yScale = 0
while yScale <= 11:
    ttk.Label(root,justify= "right", text = (yScale*50),font=('arial', 11, 'bold'), fg='#ffffff', bg='#2a374a').place(x=25, y=108+(yScale*50))
    yScale+=1

rootFooter = ttk.Canvas(root, highlightthickness=0, bg='#5159a7', width=1200, height=60)
rootFooter.place(x=0, y=740)

logBox = ttk.Canvas(root, highlightthickness=0, bg='#bacae8',width=1100,height=40)
logBox.place(x=80, y=750)

logText = Label(root, text='> ::', font=('arial', 16, 'bold'), bg='#bacae8', fg='#2a374a')
logText.place(x=90,y=755)

#Functions
#motion
def createMotion():
    if len(motion) > 0:
        i = 0
        while i < len(motion):
            winUpdate()
            x = motion[i]
            y = motion[i+1]
            rootPlotArea.delete("frame")
            if i % 10 == 0:
                time.sleep(0.002)
            rootPlotArea.create_oval(x-10,y-10,x+10,y+10,tags="frame",fill="#b76b32",outline="#b76b32")
            i+=2
        createMotion()
    else:
        return



    #XY axis traking function
def showPosition(pos):
    x = pos.x
    y = pos.y

    xPos = ttk.Label(root, text = 'X: %a   ' % (x), font=('arial', 10, 'bold'), fg='#ffffff', bg='#5159a7')
    xPos.place(x=17,y=750)

    yPos = ttk.Label(root, text = 'Y: %a   ' % (y), font=('arial', 10, 'bold'), fg='#ffffff', bg='#5159a7')
    yPos.place(x=17,y=770)

rootPlotArea.bind('<Motion>', showPosition)
#rootPlotArea.bind('<Double-1>', showPosition)

    #LogBox text update
showX1 = 0
showY1 = 0
showX2 = 0
showY2 = 0

logMsgStart = "> :: Lūdzu, atlasiet sākumpunktu, veicot dubultklikšķi uz loga" 
logMsgEnd = "> :: Lūdzu, atlasiet galapunktu, veicot dubultklikšķi uz loga" 
logMsgFull = "> :: Lūdzu, notīriet trajektorijas ekrāna lauku, noklikšķinot uz pogas \"CLEAR\""
logMsgClear = "> :: "

def logResult(x1,y1,x2,y2):
    logMsgResult = "> :: Sākumpunkts X1 = %a, Y1 = %a; Galapunkts X2 = %a, Y2 = %a." % (x1,y1,x2,y2)
    logText.config(text = logMsgResult)

def getLog(msg):
    global logMsgStart
    global logMsgEnd
    global logMsgFull
    global logMsgResult
    global logMsgClear
    if msg == "start":
        logText.config(text = logMsgStart)
    elif msg == "end":
        logText.config(text = logMsgEnd)
    elif msg == "clear":
        logText.config(text = logMsgClear)
    else:
        logText.config(text = logMsgFull)
    
    #Child windows HELP
setPoint = []
def getPoint(pos):
    getX = int(pos.x)
    getY = int(pos.y)
    if len(setPoint) < 4:
        getLog("end")
        setPoint.append(getX)
        setPoint.append(getY)
    if len(setPoint) == 4:
        X1 = setPoint[0]
        Y1 = setPoint[1]
        X2 = setPoint[2]
        Y2 = setPoint[3]

        logResult(X1,Y1,X2,Y2)
        rootPlotArea.config(cursor="arrow")
        DrawLine(X1,Y1,X2,Y2,True)
        rootPlotArea.unbind('<Double-1>')

    #clear plot
def Clear():
    rootPlotArea.unbind('<Double-1>')
    rootPlotArea.delete("frame")
    global motion
    motion = []
    global setPoint
    setPoint = []
    getLog("clear")
    rootPlotArea.delete("toDraw")
    print("CLEARED")

def pickPointFromArea():
    rootPlotArea.config(cursor="tcross")
    if len(setPoint) == 4:
        getLog("full")
        return
    getLog("start")
    rootPlotArea.bind('<Double-1>', getPoint)
    
    
def openHelp():
    #setting
    helpWin = Toplevel()
    helpWin.title('Help: Pogu apraksts')
    helpWin.geometry('580x243')
    helpWin.resizable(width=False, height=False)
    helpWin['bg'] = '#2a374a'

        #Block grid
            #Pick Point block
    ppHeaderBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#5159a7',width=560,height=20)
    ppHeaderBlock.place(x=10,y=10)

    ppHeaderText = ttk.Label(helpWin, text= 'PICK POINT', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    ppHeaderText.place(x=255,y=10)

    ppInfoBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#647abc',width=560,height=20)
    ppInfoBlock.place(x=10,y=30)

    ppInfoText = ttk.Label(helpWin, text= 'Norādiet trajektorijas sākuma un beigu punktu, noklikšķinot uz ekrāna.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    ppInfoText.place(x=80,y=30)
        
            #Set Point block
    spHeaderBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#5159a7',width=560,height=20)
    spHeaderBlock.place(x=10,y=60)

    spHeaderText = ttk.Label(helpWin, text= 'SET POINT', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    spHeaderText.place(x=255,y=60)

    spInfoBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#647abc',width=560,height=20)
    spInfoBlock.place(x=10,y=80)

    spInfoText = ttk.Label(helpWin, text= 'Norādiet trajektorijas sākuma un beigu punktu x y koordinātas, noklikšķinot uz ekrāna.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    spInfoText.place(x=45,y=80)
        
            #Clear block
    clHeaderBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#5159a7',width=560,height=20)
    clHeaderBlock.place(x=10,y=110)

    clHeaderText = ttk.Label(helpWin, text= 'CLEAR', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    clHeaderText.place(x=262,y=110)

    clInfoBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#647abc',width=560,height=20)
    clInfoBlock.place(x=10,y=130)

    clInfoText = ttk.Label(helpWin, text= 'Notīrīt trajektorijas ekrāna lauku.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    clInfoText.place(x=190,y=130)
        
            #Cancel block
    ccHeaderBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#5159a7',width=560,height=20)
    ccHeaderBlock.place(x=10,y=160)

    ccHeaderText = ttk.Label(helpWin, text= 'CANCEL', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    ccHeaderText.place(x=258,y=160)
    
    ccInfoBlock = ttk.Canvas(helpWin, highlightthickness=0, bg='#647abc',width=560,height=20)
    ccInfoBlock.place(x=10,y=180)

    ccInfoText = ttk.Label(helpWin, text= 'Pārtraukt programmu.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    ccInfoText.place(x=215,y=180)
    
        #Buttons
    helpOkButton = Button(helpWin, text="OK", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=78,relief='flat', command=helpWin.destroy)
    helpOkButton.place(x=12, y=210)

    helpWin.mainloop()

    #child windows SET POINT
def openSetPoint():
    Clear()
    setPointWin = Toplevel()
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

    def Apply():
        Clear()
        try:
            x1 = int(enterX1.get())
            y1 = int(enterY1.get())
            x2 = int(enterX2.get())
            y2 = int(enterY2.get())
            if x1 < 0 or x1 > 1100 or y1 < 0 or y1 > 550 or x2 < 0 or x2 > 1100 or y2 < 0 or y2 > 550:
                setPointWin.destroy()
                messagebox.showwarning(title='Error', message='Koordinātas nav ievadītas vai ir ievadītas nepareizi. Grafika izmērs ir 1100px uz 550px')
                return
            setPointWin.destroy()
            logResult(x1,y1,x2,y2)
            DrawLine(x1,y1,x2,y2,True)
        except:
            setPointWin.destroy()
            messagebox.showwarning(title='Error', message='Koordinātas nav ievadītas vai ir ievadītas nepareizi. Grafika izmērs ir 1100px uz 550px')
            
        #button
    spApplyButton = Button(setPointWin, text="Apply", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat', command=Apply)
    spApplyButton.place(x=11,y=110)
    spCancelButton = Button(setPointWin, text="Cancel", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat', command=setPointWin.destroy)
    spCancelButton.place(x=147, y=110)

    setPointWin.mainloop()

#Root Win buttons
pPointButton = Button(root, text="PICK POINT", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=19,relief='flat',command=pickPointFromArea)
pPointButton.place(x=80, y=60)

sPointButton = Button(root, text="SET POINT", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=19,relief='flat',command=openSetPoint)
sPointButton.place(x=351, y=60)

helpButton = Button(root, text="HELP", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13, relief='flat',command=openHelp)
helpButton.place(x=622, y=60)

clearButton = Button(root, text='CLEAR', font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13, relief='flat',command=Clear)
clearButton.place(x=813, y=60)

closeButton = Button(root, text="CLOSE", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13,relief='flat', command=root.destroy)
closeButton.place(x=1004, y=60)
def winUpdate():
    root.update()
    rootPlotArea.update()
    logBox.update()

root.mainloop()
