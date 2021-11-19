from time import *
from threading import Thread

def myBox():
    while True:
        print("My box is Open ")
        sleep(5)
        print("My box is Closed")
        sleep(5)

def myLED():
    while True:
        print("My LED is On")
        sleep(1)
        print("My LED is Off")
        sleep(1)
boxThread = Thread(target=myBox)
LEDThread = Thread(target=myLED)
boxThread.daemon = True
LEDThread.daemon = True
boxThread.start()
LEDThread.start()
j =0
while True :
    print(j)
    j = j+1
    sleep(.1)