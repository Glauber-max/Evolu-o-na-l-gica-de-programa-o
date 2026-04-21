from math import sqrt
# vou fazer uma função utilitaria que calcula por meio de baskara o x1 e x2 de uma equação do 2 grau (ax **2 +- bx +- c = 0 )
def doubleX(a: int, b: int, c:int): 
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "sem raizes reais", "sem raizes reais"
    
    deltaR = sqrt(delta)
    calculox1 = (-b + deltaR)  / (2 * a)
    calculox2 = (-b - deltaR) / (2 * a)
    return calculox1, calculox2

x1, x2 = doubleX(a=1, b=-5, c=6)
x3, x4 = doubleX(a=1, b=-5, c=6)
x5, x6 = doubleX(a=1, b=0, c=9)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
