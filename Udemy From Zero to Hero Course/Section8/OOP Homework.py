class Line:
    
    def __init__(self,coor1,coor2):
        
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**(1/2)
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())

print(li.slope())

print("\n")

class Cylinder:
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.height * self.radius ** 2
    
    def surface_area(self):
        return 2 * Cylinder.pi * self.radius ** 2 + 2 * Cylinder.pi * self.radius * self.height

# EXAMPLE OUTPUT
c = Cylinder(2,3)

print(c.volume())

print(c.surface_area())