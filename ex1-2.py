
class Vecteur2D:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def afficher(self): #methode d'affichage
        print(self.x,self.y)
    def addition(self, v1, v2):
        self.x = v2.x + v1.x
        self.y = v2.y + v1.y
        print(self.x, self.y)

v1 = Vecteur2D(1,2) #instanciation des vecteurs
v2 = Vecteur2D(5,10)
print("vecteur1 :")
v1.afficher()
print("vecteur2 :")
v2.afficher()
somme=Vecteur2D()
print("l'addition des deux vecteurs est: ")
somme.addition(v1,v2)

