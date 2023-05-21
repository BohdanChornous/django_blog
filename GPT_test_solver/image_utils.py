import os
import cv2
import numpy as np


def imread(path: str):
    with open(path, "rb") as file:
        chunk = bytearray(file.read())
        chunk_arr = np.asarray(chunk, dtype=np.uint8)

        return cv2.imdecode(chunk_arr, cv2.IMREAD_COLOR)
