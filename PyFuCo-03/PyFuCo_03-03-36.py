class Point:     # Pascal Naming Convention: Class names are in capital letter with every new word
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()     # Creates a new object based on the Class Point
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
