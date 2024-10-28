def calc(x, y):
    c = x + y
    print(c)
def sub(x, y):
    c = x - y
    print(c)
def mult(x, y):
    c = x * y
    print(c)
def divide(x, y):
    c = x / y
    print(c)

def enter():
    a = int(input("entrer a: "))
    b = int(input("entrer B: "))
    op = input()
    if(op == "/"):
        divide(a,b)
    elif op == "-":
        sub(a,b)
    elif op == "*":
        mult(a, b)
    else: 
        calc(a, b)
enter()


    
    