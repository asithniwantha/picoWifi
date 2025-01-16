from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

def blink_led():
    try:
        pin.toggle()
    except KeyboardInterrupt:
        pin.off()
        print("Blinking stopped")
        return
        
