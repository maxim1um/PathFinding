# point.py

import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value= 0
        self.cost = sys.maxsize