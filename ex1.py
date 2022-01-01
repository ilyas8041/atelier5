
class Vecteur2D:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def afficher(self): #methode d'affichage
        print(self.x,self.y)

v1 = Vecteur2D() #instanciation des vecteurs
v2 = Vecteur2D(5,10)
print("vecteur1 :")
v1.afficher()
print("vecteur2 :")
v2.afficher()