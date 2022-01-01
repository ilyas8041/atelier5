class Rectangle:
    def __init__(self, l=0, h=0, n=""):
       self.a = l
       self.b = h
       self.n=n

    def afficher(self): #affichage du rectangle
        print("longeur du rectangle :%d \nlargeur du rectangle :%d \nnom du rectangle :%s" % (self.a, self.b, self.n))

    def surface(self,R): #calcul de surface
        self.S=R.a*R.b
        print("surface : %d" % (self.S), "\n")

class Carré(Rectangle):
    {}

R=Rectangle(4,3,"Rectangle")
R.afficher()
R.surface(R)

C=Carré(5,5,"Carré")
print(C.n)
C.surface(C)