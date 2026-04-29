from gpiozero import MotionSensor
import time as t

pir = MotionSensor(4)

def motion_detected():
	print("Motion detected!")
	
def motion_stopped():
	print("Motion stopped!")
	
	
pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped



	

