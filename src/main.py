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
                print("ENTER PIN: \n")
                if(kp.enter_pin() == True):
                    #prev_state = state
                    #[PIN ENTRY/CHECK LOGIC]
                    state = 'ARMED'
                    print(f"State Transition: DISARMED --> { state }")
                else:
                    buzzer.buzzXTimes(1)
                    print("INCORRECT PIN \n")
                    continue
            #set the state to PIN_RESET on entry of '#' key and correct PIN 
            elif(kp.get_key() == 'A'):
                print("ENTER PIN: \n")
                if(kp.enter_pin() == True):
                    #[PIN ENTRY/CHECK LOGIC]
                    state = 'PIN_RESET'
                    print(f"State Transition: DISARMED --> { state }")
                else:
                    buzzer.buzzXTimes(1)
                    print("INCORRECT PIN \n")
                    continue

        #cannot enter PIN_RESET state from ARMED state
        elif(state == 'ARMED'):
            #state entry actions run once 
            if(prev_state != state):
                buzzer.buzzXTimes(1)
                rgb.redLEDBlink()
                rgb.rgbOFF()
            prev_state = state

            #manually transition out of ARMED state prior to intruder detection
            if(kp.get_key() == '*'):
                print("ENTER PIN: \n")
                if(kp.enter_pin() == True):
                    #[PIN ENTRY/CHECK LOGIC]
                    state = 'DISARMED'
                    print(f"State Transition: ARMED --> { state }")
                    continue
                else:
                    buzzer.buzzXTimes(1)
                    print("INCORRECT PIN \n")   
                    continue
            #Use interrupts via pir.py for motion detected event 
            #Assigned to global var --> alarm gets flipped on 
            elif(pir.Intruder == 1):
                buzzer.buzzON()
                rgb.redLED()
                #typically we would disarm the sys with PIN entry but '6'
                #can be a placeholder til then 
                if(kp.get_key() == '*'):
                    print("ENTER PIN TO DISARM: \n")
                    if(kp.enter_pin() == True):
                        buzzer.buzzOFF()
                        rgb.rgbOFF()
                        state = 'DISARMED'
                        print(f"State Transition: ARMED --> { state }")
                        #prev_state = state
                    else:
                        print("INCORRECT PIN \n")
                        buzzer.buzzXTimes(1)
                        continue

        #cannot enter ARMED state from PIN_RESET state 
        elif(state == 'PIN_RESET'):
            if(prev_state != state):
                buzzer.buzzXTimes(1)
                buzzer.buzzOFF()
                rgb.blueLED(1)
                rgb.rgbOFF()
            prev_state = state

            #transition manually between PIN_RESET & DISARMED 
            #NO pin entry required for this specific state transition
            if(kp.get_key() == '*'):
                print("SET NEW PIN: \n")
                if(kp.enter_pin() == True):
                    prev_state = state
                    state = 'DISARMED'
                    print(f"State Transition: PIN_RESET --> { state }")
                    #continue

            #PIN RESET LOGIC 
            #successful pin reset --> automatic state transition to DISARMED
            if(kp.get_key() == 'A'):
                kp.set_pin() #allows the user to set a new PIN code 
                state = 'DISARMED' #automatic transition to DISARMED after new PIN 
                print("Automatic STATE transition on SET PIN: \n")
                print(f"State Transition: PIN_RESET --> { state }")
            
            #elif(pir.Intruder == 0):
                #buzzer.buzzOFF()
                #rgb.rgbOFF()

        #output to logs for testing 
        sys.stdout.flush()

if __name__ == "__main__":
    main()
