class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x1 = float(x)
        self.y1 = float(y)

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    def display(self):
        print("[(",self.orig.x1,",", self.orig.y1,")", "(",self.extrem.x1,"," ,self.extrem.y1,")]")

S = Segment(1, 2, 3, 4)
S.display()