# vou fazer um codigo de media tentando ser o mais reutilizavel possível
def calcular_media(list_numerica: list) -> float:
    numeros = 0   # acumulador pra saber a soma de tudo na lista (possivel usar sum tambem)
    qtd = len(list_numerica)    # saber a quantidade de itens na lista pra dividir m = itens / qtd itens
    for numero in list_numerica:    # pra cada numero na lista numerica ela vai somar tudo 
        numeros += numero
    media = numeros / qtd # por fim ela faz o calculo da média realmente
    return round(media, 2) 
