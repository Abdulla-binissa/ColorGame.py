import tkinter
import random

# List of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
        'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Initial player score
score = 0

# The game time left, initially 30 seconds
timeleft = 30


# Starting game
def startGame(event):
    if timeleft == 30:
        countdown()
    # run next color
    nextColor()

# Choose and display next color
def nextColor():
    
    # use global variables from above
    global score
    global timeleft
    
    # If game is in progess
    if timeleft > 0:
        # make the text entry box active.
        e.focus_set()

        # typed color is correct
        if e.get().lower() == colors[1].lower():
            score += 1

        # clear the text box and shuffle colors
        e.delete(0, tkinter.END)
        random.shuffle(colors)

        # change color to type
        label.config(fg = str(colors[1]), text = str(colors[0]))

        # update score
        scoreLabel.config(text = "Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft
    
    # If game is in progress
    if timeleft > 0:

        # decrement the timer
        timeleft -= 1

        # update label
        timeLabel.config(text = "Time left: " + str(timeleft))

        # run every second
        timeLabel.after(1000, countdown)

###### Driver Code

# Create a GUI window
root = tkinter.Tk()

# Set title and size
root.title("ColorGame.py")
root.geometry("475x250")

# add instructions label
instructions = tkinter.Label(
        root, 
        text = "Type in the COLOR of the words, not the WORD!", 
        font = 'Helvetica 16')
instructions.pack()

# add score label
scoreLabel = tkinter.Label(
        root, 
        text = "Press enter to start!", 
        font = 'Helvetica 16')
scoreLabel.pack()

# add a time label
timeLabel = tkinter.Label(
        root, 
        text = "Time left: " + str(timeleft), 
        font = 'Helvetica 16')
timeLabel.pack()

# add a color display label
label = tkinter.Label(
    root, 
    font = 'Helvetica 60 bold')
label.pack()

# add text box to type
e = tkinter.Entry(root)

# run startGame when 'enter' is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on entry box
e.focus_set()

# start GUI
root.mainloop()






