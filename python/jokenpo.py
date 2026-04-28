from random import randint
from time import sleep

def Jokenpo():
    joken = ["JO", "KEN", "PO"]
    while True:
        print("||| 0 == pedra |||")
        print("||| 1 == tesoura |||")
        print("||| 2 == papel |||")
        print("||| 3 == sair |||")
        
        escolha = int(input("qual é sua escolha? "))
        
        if escolha == 3:
            break
            
        elif escolha > 3:
            print("numero maior que 3, faça novamente")
            
        else:
            for letra in joken:
                print(letra)
                sleep(0.5)
                
            escolha_maquina = randint(0, 2)
            
            if escolha_maquina == 0 and escolha == 1:
                print("maquina venceu!")
            elif escolha_maquina == 0 and escolha == 2:
                print("parabens, vc venceu!")
            elif escolha_maquina == 1 and escolha == 2:
                print("maquina venceu!")
            elif escolha_maquina == 1 and escolha == 0:
                print("parabens, vc venceu!")
            elif escolha_maquina == 2 and escolha == 0:
                print("maquina venceu!")
            elif escolha_maquina == 2 and escolha == 1:
                print("parabens, vc venceu!")
            elif escolha_maquina == escolha:
                print("empate!")

Jokenpo()