#desafio é criar uma função que receba uma lísta de números e diga a mediana deles
# fiz uma tupla (foi o jeito mais fácil que achei)
#transformo em lista, ordeno em crescente, pego a quantidade, verifico os pares
# como os índices começam no zero, tive que subtrair um número (ou omitir uma soma na fórmula)
#para o índice começar em 1 e não bugar a função
#simplesmente faço as operações e retorno o resultado
def mediana(*numeros: list) -> float: 
    numerosL = list(numeros)  
    numerosL.sort()  
    quantidade = len(numerosL) 
    if quantidade % 2 == 0: 
        posisao = (quantidade // 2) - 1 
        posisao2 = quantidade // 2 
        resultado = (numerosL[posisao] + numerosL[posisao2]) / 2 
        return resultado

    posisao = quantidade // 2
    return numerosL[posisao]

# esperado nums1 = 45.5, nums = 3.5
nums1 = mediana(20, 37, 92, 14, 54, 78)    
nums = mediana(2, 4, 5, 1, 3, 6)
print(nums1)
print(nums)