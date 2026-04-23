import gpiozero
import time as t 

# GPIO pinout 
# blue = 27 
# red = 10
# green = 22 

def redLED_blink():
    red = gpiozero.LED("GPIO10",active_high=False)
    red.on()
    print("red LED is flipped on")
    t.sleep(0.25)
    red.off()
    print("red LED is flipped off")
    t.sleep(0.25)
    #red.off()
def blueLED():
    blue = gpiozero.LED("GPIO27",active_high=False)
    blue.on()

def greenLED():
    green = gpiozero.LED("GPIO22",active_high=False)
    green.on()

def rgbOFF():	
	r = gpiozero.LED("GPIO10",active_high=False)
	g = gpiozero.LED("GPIO27",active_high=False)
	b = gpiozero.LED("GPIO22",active_high=False)
	r.off()
	g.off()
	b.off()
