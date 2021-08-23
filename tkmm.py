#!/usr/bin/python3
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
#import RPi.GPIO as GPIO
import time
import random
from playsound import playsound

global t
master = Tk()
master.title("/// Magick Meditator ///")

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
slider_font = 18
slider_width = 80
slider_color = "SteelBlue1"
slider_trough_color = "steelblue"
slider_text_color = "black"
slider_border = 5
slider_length = int(screen_width)
slider_relief = RIDGE
button_width = 39
button_height =8
button_border = 3
button_font = '-weight bold'
welcome_height = 6
welcome_width = 136
welcome_font = 16
welcome_background = "Steelblue3"
welcome_border = 6
welcome_relief = RAISED

#master.attributes("-fullscreen", True)
#master.geometry("1366x768")
time_to_exit = False
loop_is_working = False
print(screen_width)
print(screen_height)

nohold = False


def countdown():
    global loop_is_working
    loop_is_working = True
    greetinglist = ["/// Namaste ///", "/// Aepalizage ///", "/// Om Namah Shivaya ///", "/// 93 ///", "/// Love is the Proximate Cause ///"]
    greeting = greetinglist[int(round(random.random()*(len(greetinglist)-1),0))]
    b=10
    for i in range(1,11):
        print(greeting)
        t.set(str(greeting)+"\nMeditation starting in "+str(b)+" seconds")
        master.update_idletasks()
        print("Meditation starting in "+str(b))
        time.sleep(1)
        b -= 1
    master.after(0, loop)

def loop():
    global loop_is_working
    
    x = float(inhale.get())
    y = float(hold.get())
    z = float(exhale.get())
    nohold = False

    if x>=2:
        inhalesleep=(x-2)
    else:
        inhalesleep=0    
    
    if y>=2:
        holdsleep=(y-2)
    else:
        holdsleep=0
    if y==0:
        nohold = True
    
    if z>=2:
        exhalesleep=(z-2)
    else:
        exhalesleep=0
    
    print(("Now Counting:\nInhale for: ")+str(inhale.get())+(" seconds.\nHold for: ")+str(hold.get())+
    (" seconds.\nExhale for: ")+str(exhale.get())+" seconds.")
    t.set("Now Counting:\nInhale for: "+str(inhale.get())+" seconds.\nHold for: "+str(hold.get())+
    " seconds.\nExhale for: "+str(exhale.get())+" seconds.")
    master.update_idletasks()
    
    
    if loop_is_working:
        
        playsound('inhalebeep.mp3')
        time.sleep(inhalesleep)
        
        if not nohold:
            playsound('holdbeep.mp3')
            time.sleep(holdsleep)
        
        playsound('exhalebeep.mp3')
        time.sleep(exhalesleep)
        
        if not nohold:
            playsound('holdbeep.mp3')
            time.sleep(holdsleep)

        master.after(0, loop)
    else:
        reset()


def reset():
    global loop_is_working
    inhale.set(0)
    hold.set(0)
    exhale.set(0)
    t.set("Welcome! Drag the sliders to set values. Tap to the left or right "
    "of the sliders to fine tune the values.")
    loop_is_working = False

t = StringVar()
t.set("Welcome! Drag the sliders to set values. Tap to the left or right of "
"the sliders to fine tune the values.")

welcome = Label(master, bg=welcome_background, bd=welcome_border,
relief=welcome_relief,
width=welcome_width, height=welcome_height, font=welcome_font, textvariable=t)
welcome.grid(column=1, row=1, columnspan=3)

inhale = Scale(master, label="Set # Seconds Inhale:", font=slider_font,
from_=0, to=20, orient=HORIZONTAL, length=slider_length, width=slider_width,
troughcolor=slider_trough_color, bg=slider_color, fg=slider_text_color,
bd=slider_border, sliderlength=slider_width, sliderrelief=slider_relief)
inhale.grid(column=1, row=2, columnspan=3)

hold = Scale(master, label="Set # Seconds Hold:", font=slider_font,
from_=0, to=20, orient=HORIZONTAL, length=slider_length, width=slider_width,
troughcolor=slider_trough_color, bg=slider_color, fg=slider_text_color,
bd=slider_border, sliderlength=slider_width, sliderrelief=slider_relief)
hold.grid(column=1, row=3, columnspan=3)

exhale = Scale(master, label="Set # Seconds Exhale:", font=slider_font,
from_=0, to=20, orient=HORIZONTAL, length=slider_length, width=slider_width,
troughcolor=slider_trough_color, bg=slider_color, fg=slider_text_color,
bd=slider_border, sliderlength=slider_width, sliderrelief=slider_relief)
exhale.grid(column=1, row=4, columnspan=3)

go = Button(master, text="START", command=countdown, bg="green3",
width=button_width, height=button_height, bd=button_border, font=button_font)
go.grid(column=1, row=5)

adios = Button(master, text="EXIT", command=exit, bg="red3",
width=button_width, height=button_height, bd=button_border, font=button_font)
adios.grid(column=3, row=5)

resetb = Button(master, text="RESET", command=reset, bg="yellow3",
width=button_width, height=button_height, bd=button_border, font=button_font)
resetb.grid(column=2, row=5)

mainloop()
