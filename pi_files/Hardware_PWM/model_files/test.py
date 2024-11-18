from identity import Identity
from adafruit_servo import ServoKit
from time import sleep

kit = ServoKit(channels=16)

scan = Identity()

path = int(input())

if path = 0:
    scan.capture()
elif path = 1:
    result = scan.compare()
    
    if result == True:
        kit.servo[0].angle = 105
        sleep(5)
        kit.servo[0].angle = 0
        
else:
    print("Invalid path")
