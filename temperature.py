n = int(input("enter le nombre de temperature à analyser : "))
T = [int(i) for i in input().split()]
pos = []
neg = []
for t in T:
    if t > 0:
        pos.append(t)
    elif t < 0:
        neg.append(t)
if pos == [] and neg == []:
    print("0")
elif pos == []:
    print(max(neg))
else:
    print(min(pos))

    
    
