import random

mot_mal = [
    "Bozy","ketaka","Rindra","Tiana","Herizo","Soa","Finaritra","sahaza","linda","sedy","bema","daika","narovana",
    "malala","harimanitra","dianah","koto","benja","sedera","nancy","fanja","john","mika","micka","dadabe","neny",
    "safidy","mioty","sarindra","nicole","nomena","toky","toliniaina","naunau","haritiana","sarah","vatosoa","faniry",
    "faly","tezitra","bemaso","faratiana","farakely","sanyh","rakoto","naina","niaina","fanomezantsoa","njara","laza","zafy",
    "nyavo","navosoa","chat","alika","kisoa","kambana","heritiana","hery","valisoa","mandrindra","olivier","santatra","sarobidy","daniel","mariah"
]

symbole = "@#$*/?:!*%+-.&\ 0123456789"

def generate_password():
    mot = random.choice(mot_mal)
    l_rest = random.randint(0, 14 - len(mot))
    for i in range(l_rest):
        mot += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" + symbole)
    return mot

passwords = [generate_password() for i in range(5000)]

with open("password_5000.txt", "w") as file:
    file.write("\n".join(passwords))

print("5000 password génerés et sauvegardés dans password_5000.txt")
