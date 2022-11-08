from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(11, GPIO.LOW)

# GUI DEFINITIONS8

win = Tk()
win.geometry("250x200")
win.title("LED TOGGLER")
myfont = tkinter.font.Font(family = "Helvetica", size = 12, weight= "bold")     

num = IntVar()   
        
def Exitwin():
    GPIO.cleanup()
    win.destroy()

def led():
    value = num.get()
    if(value == 1):
        if(GPIO.input(11)):
            GPIO.output(11, GPIO.LOW)
            ledButton1["text"] = "Turn green LED on"
           
        else:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.HIGH)
            ledButton1["text"] = "Turn green LED off"
            ledButton2["text"] = "Turn blue LED on"
            ledButton3["text"] = "Turn red LED on"

    elif(value == 2):
        if(GPIO.input(12)):
            GPIO.output(12, GPIO.LOW)
            ledButton2["text"] = "Turn blue LED on"
           
        else:
            GPIO.output(11, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            ledButton2["text"] = "Turn blue LED off"
            ledButton1["text"] = "Turn green LED on"
            ledButton3["text"] = "Turn red LED on"

    elif(value == 3):
        if(GPIO.input(13)):
            GPIO.output(13, GPIO.LOW)
            ledButton3["text"] = "Turn red LED on"
        else:
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            ledButton3["text"] = "Turn red LED off"
            ledButton1["text"] = "Turn green LED on"
            ledButton2["text"] = "Turn blue LED on"


        
# WIDGETS
ledButton1 = Radiobutton(win, text = 'Turn green LED on',indicatoron = 0, font = myfont, variable=num, value = 1, command = led, height = 2, width = 20)
ledButton1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

ledButton2 = Radiobutton(win, text = 'Turn blue LED on',indicatoron = 0, font = myfont, variable=num, value = 2, command = led, height = 2, width = 20)
ledButton2.place(relx = 0.5, rely = 0.3, anchor = CENTER)

ledButton3 = Radiobutton(win, text = 'Turn red LED on',indicatoron = 0, font = myfont,variable = num, value = 3, command = led, height = 2, width = 20)
ledButton3.place(relx = 0.5, rely = 0.5, anchor = CENTER)


exitbutton = Radiobutton(win, text = 'Exit',indicatoron = 0, font = myfont, command = Exitwin, height = 2, width = 8)
exitbutton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

win.mainloop()
