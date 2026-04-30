from gpiozero import MotionSensor
import buzzer
import rgb
import time as t

pir = MotionSensor(4)

Intruder = 0

def motion_detected():
    print("Motion detected!")
    global Intruder
    Intruder = 1
	
def motion_stopped():
    print("Motion stopped!")
    global Intruder
    Intruder = 0
	
pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped



	

