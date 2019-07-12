#################################################
# Hw6
# Your andrewID: vccheng
# Your section: H
#################################################

#################################################
# Hw6 problems: Clicker Game
#################################################

from PIL import Image
from tkinter import *
from image_utils import *


# This function initializes variables to set up game
def init(data):
    data.cX = data.width / 2  # set centerx, centery of rectangle
    data.cY = data.height / 2
    data.x = data.width / 2  # initial clicker x pos, y pos
    data.y = data.width / 2
    data.image = PhotoImage(file = 'pot.png')
    data.mode = 'launch'

# This function controls mousePressed for each mode
def mousePressed(event, data):
    if (data.mode == "launch"):
        launchMousePressed(event, data)
    elif (data.mode == "play"):
        playMousePressed(event, data)
    elif (data.mode == "gameOver"):
        gameOverMousePressed(event, data)


# This function controls keyPressed for each mode
def keyPressed(event, data):
    if (data.mode == "launch"):
        launchKeyPressed(event, data)
    elif (data.mode == "play"):
        playKeyPressed(event, data)
    elif (data.mode == "gameOver"):
        gameOverKeyPressed(event, data)


# This function controls timerFired for each mode
def timerFired(data):
    if (data.mode == "launch"):
        launchTimerFired(data)
    elif (data.mode == "play"):
        playTimerFired(data)
    elif (data.mode == "gameOver"):
        gameOverTimerFired(data)


# This function controls redrawAll for each mode
def redrawAll(canvas, data):
    if (data.mode == "launch"):
        launchRedrawAll(canvas, data)
    elif (data.mode == "play"):
        playRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):
        gameOverRedrawAll(canvas, data)


####################################
# launchScreen mode
####################################
# mousePressed not used
def launchMousePressed(event, data):
    pass

# If key "p" pressed, start game
def launchKeyPressed(event, data):
    if event.keysym == 'p':
        data.mode = 'play'



# Image starts to bounce around screen
def launchTimerFired(data):
    # bounce(data)
    pass



# This function draws everything on launch screen
def launchRedrawAll(canvas, data):
    offset = 30
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
    # background color
    canvas.create_image(data.width/2, data.height/2, image = data.image)


    canvas.create_text(data.width / 2, data.height / 2 + offset,
                       font="Arial 20 bold", text="Grow your plant",
                       fill="white")
    #create bouncing icon


    canvas.create_text(data.width / 2, data.height / 2 + offset,
                           font="Arial 20 bold", text="Press 'p' to play",
                           fill="white")
    canvas.create_image(data.imageLeft, data.imageTop, image=data.image)


####################################
# gameOver mode
####################################

# Not used
def gameOverMousePressed(event, data):
    pass


# go back to launch screen if "s" key pressed
def gameOverKeyPressed(event, data):
    pass


# Not used
def gameOverTimerFired(data):
    pass


# Draws game over screen, including score, text, and restart instructions
def gameOverRedrawAll(canvas, data):









####################################
# play mode
####################################

# When a user clicks within boundaries of an image, it disappears
def playMousePressed(event, data):
    pass



# This function controls scroll and clicker position
def playKeyPressed(event, data):
    pass




















# This function controls timing in game
def playTimerFired(data):
    pass

import random


# redraws everything in play mode
def playRedrawAll(canvas, data):
     canvas.create_image(data.width/2, data.height/2, image = data.image)











####################################
# use the run function as-is
####################################
# This function runs the Clicker Game.
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

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass

    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
    root = Tk()
    root.resizable(width=False, height=False)  # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
    mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
    keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(300, 600)
