from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(12, GPIO.LOW);
GPIO.output(13, GPIO.LOW);
GPIO.output(11, GPIO.LOW);

# GUI DEFINITIONS

win = Tk()
win.title("LED TOGGLER")
myfont = tkinter.font.Font(family = "Helvetica", size = 12, weight= "bold")


def ledToggle1():
    if(GPIO.input(11)):
        GPIO.output(11, GPIO.LOW);
        ledButton1["text"] = "Turn LED1 on"
           
    else:
#         GPIO.cleanup()
        GPIO.output(12, GPIO.LOW);
        GPIO.output(13, GPIO.LOW);
        GPIO.output(11, GPIO.HIGH);
        ledButton1["text"] = "Turn LED1 off"
        ledButton2["text"] = "Turn LED2 on"
        ledButton3["text"] = "Turn LED3 on"
        
def ledToggle2():
    if(GPIO.input(12)):
        GPIO.output(12, GPIO.LOW);
        ledButton2["text"] = "Turn LED2 on"
           
    else:
#         GPIO.cleanup()
        GPIO.output(11, GPIO.LOW);
        GPIO.output(13, GPIO.LOW);
        GPIO.output(12, GPIO.HIGH);
        ledButton2["text"] = "Turn LED2 off"
        ledButton1["text"] = "Turn LED1 on"
        ledButton3["text"] = "Turn LED3 on"
        

def ledToggle3():
    if(GPIO.input(13)):
        GPIO.output(13, GPIO.LOW);
        ledButton3["text"] = "Turn LED3 on"
           
    else:
#         GPIO.cleanup()
        GPIO.output(11, GPIO.LOW);
        GPIO.output(12, GPIO.LOW);
        GPIO.output(13, GPIO.HIGH);
        ledButton3["text"] = "Turn LED3 off"
        ledButton1["text"] = "Turn LED1 on"
        ledButton2["text"] = "Turn LED2 on"
        
        
def Exitwin():
    GPIO.cleanup()
    win.destroy()
        
# WIDGETS
ledButton1 = Button(win, text = 'Turn led1 on', font = myfont, command = ledToggle1, bg = 'green', height = 1, width = 24)
ledButton1.grid(row=0, column = 1)

ledButton2 = Button(win, text = 'Turn led2 on', font = myfont, command = ledToggle2, bg = 'blue', height = 1, width = 24)
ledButton2.grid(row=1, column = 1)


ledButton3 = Button(win, text = 'Turn led3 on', font = myfont, command = ledToggle3, bg = 'red', height = 1, width = 24)
ledButton3.grid(row=2, column = 1)


exitbutton = Button(win, text = 'Exit', font = myfont, command = Exitwin, bg = 'blue', height = 1, width = 8)
exitbutton.grid(row = 3, column = 1)