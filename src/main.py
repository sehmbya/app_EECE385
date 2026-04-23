import sys
import time as t
import rgb
import pir
from datetime import datetime 
from gpiozero import LED

def main():
    current_time = datetime.now()
    print("385App Initialized!!!")

    #testLED = LED("BOARD11")

    rgb.rgbOFF()
    #testing output continuously... print time every 5 seconds
    while True:
        #print(f"current time in EST is: { current_time }")

        #testLED.on()
        #t.sleep(1)
        #testLED.off()
        #t.sleep(1)


        #t.sleep(1)
        #rgb.redLED_blink()
        rgb.greenLED()
        rgb.blueLED()

        #output to logs for testing 
        sys.stdout.flush()


if __name__ == "__main__":
    main()
