import gpiozero
import time as t 

# GPIO pinout 
# blue = 15 
# red = 18
# green = 14 

def redLED():
    red = gpiozero.LED("GPIO18",active_high=False)
    red.on()

# blinks n number of times
def blueLED(n: int) -> None:
    blue = gpiozero.LED("GPIO14",active_high=False)
    for _ in range(n):
        blue.on()
        t.sleep(0.25)
        blue.off()
        t.sleep(0.25)

def greenLEDBlink():
    green = gpiozero.LED("GPIO15",active_high=False)
    green.on()
    t.sleep(0.25)
    green.off()

def rgbOFF():	
	r = gpiozero.LED("GPIO18",active_high=False)
	g = gpiozero.LED("GPIO14",active_high=False)
	b = gpiozero.LED("GPIO15",active_high=False)
	r.off()
	g.off()
	b.off()
