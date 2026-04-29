import time as t
import gpiozero

#initalizion of buzzer on startup of application 
def buzzOFF() -> None:
    buzz = gpiozero.Buzzer(23)
    buzz.off()

#for intrusion leave buzzer on continuously
def buzzON():
    buzz = gpiozero.Buzzer(23)
    buzz.on()

def buzzXTimes(n: int) -> None:
    buzz = gpiozero.Buzzer(23)

    for _ in range(n):
        buzz.on()
        t.sleep(0.25)
        buzz.off()
        t.sleep(0.25)

