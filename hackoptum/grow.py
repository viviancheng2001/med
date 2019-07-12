# Basic Animation Framework

from PIL import Image
from Tkinter import *

from image_utils import *
import math, mindwave, time, string


####################################
# customize these functions
####################################

def init(data):

    data.image = PhotoImage(file='pott.gif'
                        )
    data.headset = mindwave.Headset('/dev/ttyUSB0', 'DB00')
    data.im = PhotoImage(file = 'cann.gif')
    data.sky = PhotoImage(file='sky.gif')

    data.bac = PhotoImage(file = 'bb.gif')
    data.im = data.im.subsample(6,6)
    data.f = PhotoImage(file = 'fl.gif')
    data.imageWidth = data.f.width()
    data.imageHeight = data.f.height()
    data.fLeft = (data.width/2) - (data.imageWidth/2)
    data.fTop = (data.height/0.92) + (data.imageHeight/2)
    data.med = '50'
    data.canWidth = data.im.width()
    data.canHeight = data.im.height()
    data.cLeft = (100) - data.canWidth/2
    data.cTop = data.height/10 + data.canHeight/2
    data.mode = 'med'
    data.s = PhotoImage(file = 'soi.gif')
    data.watering = ''


def redrawAll(canvas,data):
    if (data.mode == 'phys'):
        physRedrawAll(canvas,data)
    elif (data.mode == 'med'):
        medRedrawAll(canvas,data)

def keyPressed(event, data):
    if (data.mode == 'phys'):
        physKeyPressed(event,data)
    elif (data.mode == 'med'):
        medKeyPressed(event,data)


 # This function controls mousePressed for each mode
def mousePressed(event, data):
     if (data.mode == "phys"):
         physMousePressed(event, data)
     elif (data.mode == "med"):
         medMousePressed(event, data)



def medKeyPressed(event, data):
    data.fTop = 532 + ((3.1)*(data.headset.meditation))

def medMousePressed(event,data):
    pass

def physKeyPressed(event,data):
    pass

def physMousePressed(event,data):
    pass



def physRedrawAll(canvas,data):
    canvas.create_image(data.width/2,data.height/2, image = data.bac)
    canvas.create_text(data.width/2, data.height/7, text = 'Welcome to Blossom!', font = 'Times 35 ')

def medRedrawAll(canvas, data):

    # canvas.create_rectangle(0,0, data.width, data.height, fill='LightSkyBlue1')
    canvas.create_image(data.width/2, data.height/2, image=data.sky)


    canvas.create_image(data.fLeft + (data.imageWidth / 2), data.fTop - (data.imageHeight / 2), image=data.f)

    canvas.create_rectangle(0, 430, data.width, data.height, fill='orange3')
    # canvas.create_image(data.width/2, data.height/1,image = data.s)
    canvas.create_image(data.width / 2, data.height / 1.5, image=data.image)

    canvas.create_image(data.cLeft + (data.canWidth/2), data.cTop - (data.canHeight/2), image=data.im)

    canvas.create_text(data.width/1.3, 60, text = 'Meditation Level: ' + str(data.headset.meditation), font = 'Times 20')
    canvas.create_text(100,data.height/4.8, text = data.watering)

def getMeditationLevel(data):
    pass


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)

        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    
        # setup headset
##    data.headset = mindwave.Headset('/dev/ttyUSB0', 'DB00')
    time.sleep(2)

    data.headset.connect()
    print "Connecting..."


    totaltime = 0
    totalmed = 0

    while data.headset.status != 'connected':
        time.sleep(0.5)
        if data.headset.status == 'standby':
            data.headset.connect()
            print "Retrying connect..."

    print "Connected."
    time.sleep(.5)
        
    
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600,600)