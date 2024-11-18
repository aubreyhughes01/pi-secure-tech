import cv2
import pandas as pd
from deepface import DeepFace

class Identity:

    def __init__(self):
        self.database_path = "database"

    def capture(self):
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            print("Error: cannot open camera")
            exit()

        # Capture frame
        ret, frame = cam.read()

        if ret:
            cv2.imwrite("captured_image.jpg", frame)

        cam.release()
        cv2.destroyAllWindows()

    def compare(self):
        # dataframe object
        df = DeepFace.find(img_path = "captured_image.jpg", db_path = database_path)

        if df.empty:
            print("No match")

            return False
        else:
            print("Match found")
            print(result)

            return True


        
