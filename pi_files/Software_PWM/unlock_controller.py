from gpiozero import AngularServo
from time import sleep

# initialized to GPIO pin 14
# min_pulse and max_pulse may need adjusting, but these are common values and supported by user reviews for the MG996R
servo = AngularServo(14, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

UNLOCK = 90

def unlock():
    servo.angle = UNLOCK
    sleep(1)

# main program, unlock function call
unlock()
