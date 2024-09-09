from gpiozero import AngularServo
from time import sleep

# initialized to GPIO pin 14
# min_pulse and max_pulse may need adjusting, but these are common values and supported by user reviews for the MG996R
servo = AngularServo(14, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# values need to be figured through testing
'''
UNLOCK = 15
LOCK = 30
'''

# functions to set the servo angle
def set_angle(angle):
    servo.angle = angle
    sleep(1)
'''
def unlock():
    servo.angle = UNLOCK
    sleep(1)

def lock():
    servo.angle = LOCK
    sleep(1)
'''

# main program loop
try:
    while True:
        angle = int(input("Enter angle (0 to 180): "))  # user input for angle
        set_angle(angle)    # set servo to entered angle

except KeyboardInterrupt:
    print("Program stopped by user")


