from math import sqrt
# vou fazer uma função utilitaria que calcula por meio de baskara o x1 e x2 de uma equação do 2 grau (ax **2 +- bx +- c = 0 )
def doubleX(a: float, b: float, c:float): 
    if a == 0:
        return "a não pode ser zero", "a não pode ser zero"
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "sem raizes reais", "sem raizes reais"
    elif delta >= 0:
        deltaR = sqrt(delta)
        calculox1 = (-b + deltaR)  / (2 * a)
        calculox2 = (-b - deltaR) / (2 * a)
        return calculox1, calculox2
