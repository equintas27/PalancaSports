import cv2
import numpy as np

class PalancaStabilizer:
    def _init_ (self):
        self.prev_frame_gray = None
    def stabilizer(self, frame):
        

