n = int(input("entrer le nombre à analyser : "))
Y = [ int(i) for i in input().split()]
# total = 0
# for i in Y:
#     total += i
#     mean = total / n
# print(int(mean))

def arithmetic(n, i):
    total = sum(i)
    mean = total / n
    
    if total % n == 0:
        return int(mean)
    else:
        return float(mean)
    
result = arithmetic(n, Y)
print(result)
