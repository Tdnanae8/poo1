class Point():
    def move(self, x,y): #mov = mover
        self.x = x
        self.y = y
    def origin(self):
        self.x = 0
        self.y = 0
p1 = Point()
p2 = Point()
print(p1, p2)
p1.move(4,5)
p2.move(6,6)
print(p1.x,p1.y)
print(p2.x,p2.y)
#EJERCICIO:
#CREAR UN METODO QUE VUELVA EL PUNTO AL ORIGEN
p1.origin()
p2.origin()
print(p1.x,p1.y)
print(p2.x,p2.y)

