import time as t
import gpiozero

buzz = gpiozero.Buzzer(23)

#initalizion of buzzer on startup of application 
def buzzOFF() -> None:
    if(buzz.is_active == True):
        buzz.off()

#for intrusion leave buzzer on continuously
def buzzON():
    if(buzz.is_active == False):
        buzz.on()

def buzzXTimes(n: int) -> None:
    for _ in range(n):
        buzz.on()
        t.sleep(0.25)
        buzz.off()
        t.sleep(0.25)

