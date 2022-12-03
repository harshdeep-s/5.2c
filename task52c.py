from tkinter import *  # library named tkinter is imported
import tkinter.font      # importing tkinter.font library
import RPi.GPIO as GPIO    # imorting RPi.GPIO library

GPIO.setmode(GPIO.BOARD)    # setting BOARD type pins to use in raspberrypi

"""setting  11, 12 and 13 pins as output """

GPIO.setup(11, GPIO.OUT)     
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

""" intially setting 11, 12 and pins as low"""

GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(11, GPIO.LOW)


win = Tk()  #helps to display the root window and manages all the other components of the tkinter application
win.geometry("250x200") # here dimensions are given to window of 250x200
win.title("LED TOGGLER")
myfont = tkinter.font.Font(family = "Helvetica", size = 12, weight= "bold")     # intialized a type of font that will be used further

num = IntVar()   
        
def Exitwin():
    GPIO.cleanup()   # make all the pins low
    win.destroy()    # closing the window 

def led():
    value = num.get()      # fetching value of num used further for buttons

""" if button 1 is pressed then value = 1, and green led will get turned on by turning all other led's off """
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
#turning blue led on
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

    elif(value == 3):                   #turning red led on
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

""" making radio buttons where they will change value for value variable and led will glow, buttons are placed in GUI using ledbutton.place function """
ledButton1 = Radiobutton(win, text = 'Turn green LED on',indicatoron = 0, font = myfont, variable=num, value = 1, command = led, height = 2, width = 20)
ledButton1.place(relx = 0.5, rely = 0.1, anchor = CENTER)

ledButton2 = Radiobutton(win, text = 'Turn blue LED on',indicatoron = 0, font = myfont, variable=num, value = 2, command = led, height = 2, width = 20)
ledButton2.place(relx = 0.5, rely = 0.3, anchor = CENTER)

ledButton3 = Radiobutton(win, text = 'Turn red LED on',indicatoron = 0, font = myfont,variable = num, value = 3, command = led, height = 2, width = 20)
ledButton3.place(relx = 0.5, rely = 0.5, anchor = CENTER)


exitbutton = Radiobutton(win, text = 'Exit',indicatoron = 0, font = myfont, command = Exitwin, height = 2, width = 8)
exitbutton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

win.mainloop()                  # runs tkinter event in loop
