import random

mot_mal = [
    "Bozy","ketaka","Rindra","Tiana","Herizo","Soa","Finaritra","sahaza","linda","sedy","bema","daika","narovana",
    "malala","harimanitra","dianah","koto","benja","sedera","nancy","fanja","john","mika","micka","dadabe","neny",
    "safidy","mioty","sarindra","nicole","nomena","toky","toliniaina","naunau","haritiana","sarah","vatosoa","faniry",
    "faly","tezitra","bemaso","faratiana","farakely","sanyh","rakoto","naina","niaina","fanomezantsoa","njara","laza","zafy"
]

symbole = "@#$*/?:!*%+-.&\ 0123456789"

def generate_password():
    mot = random.choice(mot_mal)
    l_rest = random.randint(0, 14 - len(mot))
    for i in range(l_rest):
        mot += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" + symbole)
    return mot

passwords = [generate_password() for i in range(1500)]

with open("password.txt", "w") as file:
    file.write("\n".join(passwords))

print("1500 password génerés et sauvegardés dans password.txt")
