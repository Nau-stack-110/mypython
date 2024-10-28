class Voiture:
    def __init__(self, type, distance, vitesse, temps, consommation, annesortie, chevaux):
        self.type = type
        self.prix_carburant = 6000
        self.distance = distance
        self.vitesse = vitesse
        self.temps = temps
        self.consommation = consommation
        self.annesortie = annesortie
        self.chevaux = chevaux
        
    def dist_parcouru(self):
        self.distance = self.vitesse * self.temps
        print("distance parcourue = " , self.distance , "km/h")
    
    def depense(self):
             consommationtotal = (self.consommation / 100) * self.distance
             print("depense attendue  = ", consommationtotal * self.prix_carburant)
             
    def enregistre(self):
        f = open("facture.txt", "a")
        txt  = "type = {} ,\n vitesse = {} ,\n prix_carburant = {:.2f} ,\n distance = {} ,\n temps = {} ,\n consommation = {} ,\n annesortie = {} ,\n chevaux = {} \n \n "
        f.write(txt.format(self.type, self.vitesse, self.prix_carburant, self.distance, self.temps, self.consommation, self.annesortie, self.chevaux))
        f.write("\n")
        f.close()
        f=open("facture.txt", "r")
        print(f.read())

        
car = Voiture(str,int,int,int,int,int,str)   
car.type = input("entrer le type de votre voiture : ")
car.vitesse = int(input("entrer la vitesse en km/h : "))
car.temps = int(input("entrer le temps : "))
car.consommation = int(input("entrer la consommation : "))
car.annesortie = int(input("entrer l\'année de sortie : "))
car.chevaux = input("entrer chevaux : ")


print(car.dist_parcouru())
print(car.depense())
print(car.enregistre())






    
    




    

