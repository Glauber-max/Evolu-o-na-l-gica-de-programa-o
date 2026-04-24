# fazer uma função que filtre dados -> resolvi fazer uma de investimentos buscando apenas dividend yild 
from typing import TypedDict, List #tive que garantir a incidencia de dados obrigatorios( e chaves que teriam de fato), usei o typeddict

class Ativo(TypedDict): #estabeleci o formato dos dicionarios
    nome: str
    preco: float
    dividendo_mensal: float
    setor: str

def analise_dados(investimentoMensal: float, ativos: List[Ativo], dividend_yield_esperado: float) -> list:
    lista_ativos = [] 
    lista_passaram = []      
    for item in ativos: 
        yields = (item["dividendo_mensal"] / item["preco"]) * 100
        if  yields > dividend_yield_esperado:  #fiz a função que se o dividend yield for maior que um dividend escolhido, ele filtra os dados e retorna uma lista de dict com os ativos que passaram.
            lista_passaram.append({
                "nome": item["nome"],
                "preco": item["preco"],
                "yield": yields
            })
    if len(lista_passaram) > 0: #tratando uma exceção simples(divisao por zero)
        verba_ativo = investimentoMensal / len(lista_passaram)
        for ativo in lista_passaram: # esses ativos que passaram passam novamente por um for, para fazer uma divisao do investimento total  e retorna uma lista de strings formatada
            qtd = verba_ativo  / ativo["preco"]
            lista_ativos.append(f"ativos que passaram -> ||||  ativo: {ativo['nome']}  |  quantidade: {qtd: .0f} | Yield:  {ativo['yield']: .2f}% |||| ")
    else:  
       print("nenhuma lista filtrada")
    return lista_ativos
             

ativos_brutos = [ #volume de dados para teste
    {"nome": "PETR4", "preco": 38.50, "dividendo_mensal": 0.45, "setor": "Energia"},
    {"nome": "VALE3", "preco": 65.20, "dividendo_mensal": 0.30, "setor": "Mineração"},
    {"nome": "ITUB4", "preco": 32.10, "dividendo_mensal": 0.25, "setor": "Bancário"},
    {"nome": "BBDC4", "preco": 14.80, "dividendo_mensal": 0.12, "setor": "Bancário"},
    {"nome": "TAEE11", "preco": 35.40, "dividendo_mensal": 0.28, "setor": "Energia"},
    {"nome": "MXRF11", "preco": 10.50, "dividendo_mensal": 0.11, "setor": "FII"},
    {"nome": "CPLE6", "preco": 10.20, "dividendo_mensal": 0.08, "setor": "Energia"},
    {"nome": "BBAS3", "preco": 27.50, "dividendo_mensal": 0.35, "setor": "Bancário"},
    {"nome": "KLBN11", "preco": 22.10, "dividendo_mensal": 0.05, "setor": "Papel e Celulose"},
    {"nome": "EGIE3", "preco": 45.00, "dividendo_mensal": 0.38, "setor": "Energia"},
    {"nome": "WEGE3", "preco": 42.15, "dividendo_mensal": 0.04, "setor": "Industrial"},
    {"nome": "HGLG11", "preco": 165.00, "dividendo_mensal": 1.10, "setor": "FII"},
    {"nome": "SBSP3", "preco": 82.30, "dividendo_mensal": 0.15, "setor": "Saneamento"},
    {"nome": "SANB11", "preco": 28.90, "dividendo_mensal": 0.18, "setor": "Bancário"},
    {"nome": "TRPL4", "preco": 25.40, "dividendo_mensal": 0.22, "setor": "Energia"}
]

investimento_mensal = 1000 #investimento total
investimentos_bons = analise_dados(investimento_mensal, ativos_brutos, 0.8)

for investimento in investimentos_bons: #acessar a lista de investimentos
    print(investimento)
