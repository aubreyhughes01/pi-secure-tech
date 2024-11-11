from adafruit_servokit import ServoKit

class Rotator:
    def __init__(self, degree):
        self.degree = degree

    def rotate(self):
        kit = ServoKit(channels=16)

        kit.servo[0].set_pulse_width_range(500, 2500)
        kit.servo[0].angle = self.degree
