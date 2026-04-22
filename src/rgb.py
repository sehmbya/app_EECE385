import gpiozero
import time as t 

# GPIO pinout 
# blue = 27 
# red = 10
# green = 22 

def redLED():
    red = gpiozero.LED("GPIO10")
    red.on()
    print("red LED is flipped on")
    #red.off()

def blueLED():
    blue = gpiozero.LED("GPIO27")
    blue.off()

def greenLED():
    green = gpiozero.LED("GPIO22")
    green.off()
    
