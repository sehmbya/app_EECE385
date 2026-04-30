import gpiozero
import time as t 

# GPIO pinout 
# blue = 15 
# red = 18
# green = 14 

red = gpiozero.LED("GPIO18",active_high=False)
blue = gpiozero.LED("GPIO15",active_high=False)
green = gpiozero.LED("GPIO14",active_high=False)


def redLED():
    if(red.is_lit == False):
        red.on()

# blinks n number of times
def blueLED(n: int) -> None:
    for _ in range(n):
        blue.on()
        t.sleep(0.25)
        blue.off()
        t.sleep(0.25)

def greenLEDBlink():
    green.on()
    t.sleep(0.25)
    green.off()

def rgbOFF():	
    if (red.is_lit == True):
        red.off()
    if (green.is_lit == True):
        green.off()
    if (blue.is_lit == True):
        blue.off()
