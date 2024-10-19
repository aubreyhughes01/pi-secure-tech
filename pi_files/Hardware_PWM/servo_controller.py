from adafruit_servo import ServoKit

kit = ServoKit(channels=16)

# main program loop
try:
    while True:

        direction = int(input("Waiting for input: "))

        kit.servo[0].set_pulse_width_range(500, 2500)
        kit.servo[0].angle = direction     

except KeyboardInterrupt:
    print("Program stopped by user")
