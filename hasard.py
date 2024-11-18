import random 
secret = random.randrange(0, 10)
for i in range(3):
    x = int(input("Entrer un nombre entre 0 et 10 :"))
    if x == secret:
        print("bravos, vous avez gagné")
        exit()
    elif x > secret:
        print("plus grand")
    else:
        print("plus petit")
    