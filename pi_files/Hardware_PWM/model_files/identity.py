import os
import cv2
import sys
import time
from deepface import DeepFace

class Identity:

    def __init__(self):
        self.database_path = "Hardware_PWM/persistence_files/database"
        self.blank_database = "Hardware_PWM/persistence_files/blank_database"

    def capture(self, location):
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            print("Error: cannot open camera")
            exit()

        # Capture frame
        ret, frame = cam.read()

        if ret:
            if location == "Hardware_PWM/persistence_files/temp/":
                cv2.imwrite(location + "captured_image.jpg", frame)
            else:
                timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
                filename = f"captured_image{timestamp}.jpg"
                cv2.imwrite(location + filename, frame)

        cam.release()
        cv2.destroyAllWindows()

    def compare(self):
        # dataframe object
        df = DeepFace.find(img_path = "Hardware_PWM/persistence_files/temp/captured_image.jpg", db_path = database_path)
        blankdf = DeepFace.find(img_path = "Hardware_PWM/persistence_files/temp/captured_image.jpg", db_path = blank_database, enforce_detection=False)

        if sys.getsizeof(df[0]) > sys.getsizeof(blankdf[0]):     # comparison of dataframe size when image is identified vs when it's unsuccessful
            print("Match found")
            return True
        else:
            print("No match found")
            return False

