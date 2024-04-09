class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    
    def distanceStartCenter(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5    
    

    def distPoint1Point2(self, pointTwo):
        return ((self.x - pointTwo.x) ** 2 + (self.y - pointTwo.y) ** 2) ** 0.5
    

p1_x = int(input("p1.x: "))
p1_y = int(input("p1.y: "))

p2_x = int(input("p2.x: "))
p2_y = int(input("p2.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

print(p1.distanceStartCenter())
print(p1.distPoint1Point2(p2))   