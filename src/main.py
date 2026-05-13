import sys
import keypad as kp
import buzzer
import time as t
import rgb
import pir
from datetime import datetime 
from gpiozero import LED

def main():
    #state definitions
    #typically would use a typedef enum but python is different
    DISARMED = 'DISARMED'
    ARMED = 'ARMED' 
    RESET = 'PIN_RESET'

    state = DISARMED
    prev_state = None

    #Initialization functions
    kp.keypadInit()
    rgb.rgbOFF()
    buzzer.buzzOFF()

    #Primary Finite State Machine (FSM) Implementation
    #STATES = {'DISARMED', 'ARMED', 'PIN_RESET'}
    #Initial state := 'DISARMED' 
    while True:
        
        if(state == 'DISARMED'):
            #entry actions only taken once upon entry of state 
            if(prev_state != state):
                buzzer.buzzXTimes(2)
                rgb.greenLEDBlink()
                rgb.rgbOFF()
            prev_state = state

            #set the state to ARMED on entry of '*' key and correct PIN
            if(kp.get_key() == '*'):
                #prev_state = state
                #[PIN ENTRY/CHECK LOGIC]
                state = 'ARMED'
                print(f"State Transition: DISARMED --> { state }")
            #set the state to PIN_RESET on entry of '#' key and correct PIN 
            elif(kp.get_key() == '#'):
                #[PIN ENTRY/CHECK LOGIC]
                state = 'PIN_RESET'
                print(f"State Transition: DISARMED --> { state }")

        #cannot enter PIN_RESET state from ARMED state
        elif(state == 'ARMED'):
            #state entry actions run once 
            if(prev_state != state):
                buzzer.buzzXTimes(1)
                rgb.redLEDBlink()
                rgb.rgbOFF()
            prev_state = state

            #manually transition out of ARMED state prrior to intruder detection
            if(kp.get_key() == '*'):
                #[PIN ENTRY/CHECK LOGIC]
                state = 'DISARMED'
                print(f"State Transition: ARMED --> { state }")
                continue
            #Use interrupts via pir.py for motion detected event 
            #Assigned to global var --> alarm gets flipped on 
            elif(pir.Intruder == 1):
                buzzer.buzzON()
                rgb.redLED()
                #typically we would disarm the sys with PIN entry but '6'
                #can be a placeholder til then 
                if(kp.get_key() == '6'):
                    #[PIN ENTRY/CHECK LOGIC]
                    buzzer.buzzOFF()
                    rgb.rgbOFF()
                    print(f"State Transition: ARMED --> { state }")
                    #prev_state = state
                    state = 'DISARMED'

        #cannot enter ARMED state from PIN_RESET state 
        elif(state == 'PIN_RESET'):
            if(prev_state != state):
                buzzer.buzzXTimes(1)
                buzzer.buzzOFF()
                rgb.blueLED(1)
            prev_state = state

            #transition manually between PIN_RESET & DISARMED 
            #NO pin entry required for this specific state transition
            if(kp.get_key() == '*'):
                prev_state = state
                state = 'DISARMED'
                print(f"State Transition: PIN_RESET --> { state }")
                continue
            
            #[PIN RESET keypad functions/logic written here]
            #successful pin reset --> automatic state transition to DISARMED


            #elif(pir.Intruder == 0):
                #buzzer.buzzOFF()
                #rgb.rgbOFF()

        #output to logs for testing 
        sys.stdout.flush()

if __name__ == "__main__":
    main()
