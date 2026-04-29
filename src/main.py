import sys
import keypad as kp
import buzzer
import time as t
import rgb
import pir
from datetime import datetime 
from gpiozero import LED

def main():
    #print to console that app has been initialized
    current_time = datetime.now()
    print("385App Initialized!!!")

    #state definitions
    #typically would use a typedef enum but python is different
    DISARMED = 'DISARMED'
    ARMED = 'ARMED' 
    RESET = 'PIN_RESET'

    #set the initial state 
    state = DISARMED
    kp.keypadInit()
    rgb.rgbOFF()
    buzzer.buzzOFF()

    buzzer.buzzXTimes(2)

    buzzer.buzzOFF()

    rgb.blueLED(3)

    while True:
        #rgb.redLED_blink()
        rgb.greenLED()



        #state machine implementation
        #if(state == DISARMED):
            #print("state == DISARMED")
        #elif(state == ARMED):
            #print("state == ARMED")
        #elif(state == RESET):
        #    print("state == RESET (PIN_RESET)")

        #output to logs for testing 
        sys.stdout.flush()

if __name__ == "__main__":
    main()
