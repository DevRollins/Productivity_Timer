## This is a program that will help you manage your time and hopefully aid you in increasing productivity. 
## Start the program by welcoming the user to the program and prompting them to input how long they would like to study
## and for how long they would like to take breaks 

## Write code that doodles while you work.
import time 
import winsound   ## Import necessary libraries for all functionality 
import turtle 
from turtle import *
import random 

window = turtle.Screen()      
window.title('Productivity Timer')      ## Create window for user input
pen = turtle.Turtle()           ## Declare a pen to draw timer and an artist to draw while the timer runs
artist = turtle.Turtle()
pen.hideturtle()        ## Hide the turtle arrows from user
artist.hideturtle()
pen.color('White')
pen.up()
pen.setx(0)
window.bgcolor('black')

        ## Red Colors
COLORS = [(1.0, 0.0, 0.0), (1.0, 0.05, 0.00,), (1.0, 0.10, 0.0), (1.0, 0.15, 0.0), (1.0, 0.20, 0.0), (1.0, 0.25, 0.0), (1.0, 0.30, 0.0),
        (1.0, 0.35, 0.0), (1.0, 0.40, 0.0), (1.0, 0.45, 0.0), (1, 0.50, 0.0), (1.0, 0.55, 0.00),
        ## Green Colors
        (0.0, 1.0, 0.0), (0.0, 0.95, 0.05), (0.0, 0.90, 0.10,), (0.0, 0.85, 0.15), (0.0, 0.80, 0.20), (0.0, 0.75, 0.25), (0.0, 0.70, 0.30),
        (0.0, 0.65, 0.35), (0.0, 0.60, 0.40), (0.0, 0.65, 0.35), (0.0, 0.70, 0.30), (0.0, 0.75, 0.35),
        ## Blue Colors
        (0.0, 0.0, 1.0), (0.05, 0.0, 0.95), (0.10, 0.0, 0.90), (0.15, 0.0, 0.85), (0.20, 0.0, 0.80), (0.25, 0.0, 0.75), (0.30, 0.0, 0.70),
        (0.35, 0.0, 0.65,), (0.40, 0.0, 0.60,), (0.45, 0.0, 0.55), (0.50, 0.0, 0.50), (0.55, 0.0, 0.45)]

def main(): ## Welcome user to the program while initializing variables for later inputs
    worktime = int(window.numinput('Work', 'In minutes, how long would you like to be productive?', minval=1, maxval=9000) * 60)
    breaktime = int(window.numinput('Break', 'In minutes, how long would you like to rest between productivity?', minval=1, maxval=9000) * 60)
    loop = int(window.numinput('Loop', 'How many times would you like to loop through this?', minval=1, maxval=9000))
    print('\nHere we go! Your productivity begins... NOW!')

    while loop:
        for i in range(loop): ## Loop that creates a countdown timer 
            t = worktime
            while t:
                mins = t // 60
                secs = t % 60 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                pen.sety(150)
                pen.write('Work! Work! Work!',align='center', font=('Times New Roman', 25))
                pen.sety(75)
                pen.write('Time Left:', align='center', font=('Times New Roman', 25))
                pen.sety(0)
                pen.write(timer, align='center', font=('Times New Roman', 25))
                time.sleep(0.5)
                t-= 1  
                pen.clear()
                if t == 0:
                    winsound.PlaySound("Notification.wav", winsound.SND_FILENAME) ## When the timer reaches zero, the 'Notification' sound will play
            pen.write('YOU DID IT! NOW FOR A BREAK', align='center', font=('Times New Roman', 25))    ## Message notifying user when each work period is up    
            time.sleep(2)
            pen.clear()
            t = breaktime  ## New timer for the break
            while t:
                mins = t // 60
                secs = t % 60 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                pen.sety(150)
                pen.write('Take break! You are killing it!', align='center', font=('Times New Roman', 25))
                pen.sety(75)
                pen.write('Time Left:', align='center', font=('Times New Roman', 25))
                pen.sety(0)
                pen.write(timer, align='center', font=('Times New Roman', 25))
                time.sleep(0.5)
                t-= 1 
                pen.clear()
                if t == 0:
                    winsound.PlaySound("GetBusy.wav", winsound.SND_FILENAME)    ## New sound
            pen.write("And your break is up! Let's go again!", align='center', font=('Times New Roman', 25))    ## Message notifying user when each break period is up.
            break
    turtle.Terminator() 
    pen.write('Good job! You have completed your productivity for now!', align='center', font=('Times New Roman', 50, 'bold'))    ## Message to notify user when the entire work session is over. 
    pen.clear()     ## Clear entire screen
    artist.clear()
    bye()   ## Close turtle
           ## Declare that the window closes whenever the red x is hit
    
def colorloop(): 
    try:
            for i in range(1000):
                    idx = int(i/10)
                    color = COLORS[idx]
                    artist.color(color)
                    artist.forward(i)
                    artist.right(98)
                    artist.speed(0)
            artist.setx(0)
            artist.sety(0)
    except IndexError:
            turtle.reset()
            turtle.sety(0)
            colorloop()
    artist.clear()

def house():  ## Use turtle to draw while the user is working. For now, it is a house on a sunny day.
    speed(0) 

    #Grass
    bgcolor('Green')
    
    #Sky
    penup()
    goto(-400, -100)
    pendown()
    color('deepskyblue') 
    begin_fill()
    for i in range(2):
        forward(800)
        left(90)
        forward(500)
        left(90)
    end_fill()
# Sun
    penup()
    goto(-320, 225)
    pendown()
    color('Gold')
    begin_fill()
    circle(50)
    end_fill()

#Clouds 
    penup()
    pensize(3)
    goto(200, 200)
    pendown()
    color('lightgray')
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(220, 240)
    pendown()
    color('lightgray')
    begin_fill()
    circle(35)
    end_fill()
    penup()
    goto(230, 215)
    pendown()
    color('lightgray')
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(180, 215)
    pendown()
    color('lightgray')
    begin_fill()
    circle(35)
    end_fill()
    penup()
    goto(280, 200)
    pendown()
    color('lightgray')
    begin_fill()
    circle(35)
    end_fill()
    penup()
    goto(227,217)
    pendown()
    color('lightgray')
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(205,220)
    begin_fill()
    circle(30)
    end_fill()
    penup()
    ## The house
    pensize(2)
    goto(-100,-100)
    pendown()
    color('black', 'brown') ## Stroke, fill colors
    begin_fill() 

    for i in range(4):
        forward(200)
        left(90)
    end_fill()
    penup()
    goto(20, 130)
    pendown()
    color('black', 'red') 
    begin_fill()
    ## Chimney
    for i in range(2):
        forward(40)
        left(90)
        forward(100)
        left(90)
    end_fill()
    ## Roof
    penup()
    goto(-127, 70)
    pendown()
    begin_fill()
    for i in range(3):
        forward(250)
        left(120) 
    end_fill()

if __name__=="__main__":
    main()