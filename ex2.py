class Etudiant:
    def __init__(self,nom,prenom,age,cne,moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age  =age
        self.cne = cne
        self.moyenne = moyenne
mylist = [Etudiant("nom1","prenom1",25,"cne1",16),Etudiant("nom2","prenom2",22,"cne2",12),Etudiant("nom3","prenom3",23,"cne3",18),]

mylist.sort(key=lambda Etudiant : Etudiant.age )
print("la liste trieé par age :")
for i in mylist:
    print(i.nom, i.prenom, i.age, i.cne, i.moyenne,"\n")

mylist.sort(key=lambda Etudiant:Etudiant.moyenne)
print("la liste trieé par moyenne :")
for i in mylist:
    print(i.nom, i.prenom, i.age, i.cne, i.moyenne,"\n")