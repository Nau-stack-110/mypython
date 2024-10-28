nom = input("entrer votre propre Nom :")
taille = float(input("entrer votre taille en cm :"))
poids = float(input("entrer votre poids en kg :"))

taille_c = taille / 100
imc = poids / pow(taille_c, 2)
print(float(imc))

if imc <= 18.5 :
    print("Vous etes normal!")
else :
    print("bota be ianao")
