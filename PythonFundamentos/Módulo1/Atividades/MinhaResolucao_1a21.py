import os
import time

'''21) Desenvolva um programa que leia números inteiros até que o usuário digite 0. 
   Ao final, mostre:
    - A soma de todos os números positivos
    - A média dos números pares
    - O maior e o menor número digitado
    - Quantos números negativos foram digitados
'''
print("\n", "=" * 15, "EXERCÍCIO 21", "=" * 15)

try:
    numeros = []
    pares = []
    numeros_negativos = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n", "= " * 15, "LEITOR DE NÚMEROS INTEIROS", "= " * 15)
        print()
        numero = None
        tentativas_user = 5
        while tentativas_user > 0:
            try:
                
                print("\rDigite um número inteiro ou pressione [0] para sair: ", end= "", flush =True)
                numero = int(input())
                break
                
            except ValueError:
                tentativas_user -= 1
                if tentativas_user > 0:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERRO: DIGITE APENAS NÚMEROS INTEIROS")
                    continue
                else:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    erro = "ERRO: REINICIE O PROGRAMA"
                    for i in range(1, 15):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"\r{erro}", end = " ", flush = True)
                        time.sleep(0.5)
                break
        
        if numero is None:
            break 
            
        if numero != 0:
            numeros.append(numero)
            
            somar = 0
            for num in numeros:
                if num > 0:
                    somar += num
            
            if numero % 2 == 0:
                pares.append(numero)
                somar_pares = 0
                for num in pares:
                    somar_pares += num
                    media_pares = (somar_pares) / len(pares) 
        
                
            if numero < 0:
                numeros_negativos.append(numero)
                len(numeros_negativos)
            
        else:
            print()
            print(" " * 3, f"→ A soma total de todos os números é: {somar}")
            if pares:
                print(" " * 3, f"→ A soma de todos os números pares é: {somar_pares}")
                print(" " * 3,f"→ A média aritmética simples dos números pares é: {media_pares}")
            else:
                print(" " * 3, "→ Não há números pares.")
            print(" " * 3, f"→ O maior número do conjunto é: {max(numeros)}")
            print(" " * 3, f"→ O menor número do conjunto é: {min(numeros)}")
            if numeros_negativos:
                print(" " * 3, f"→ A quantidade de números negativos no conjunto é: {len(numeros_negativos)}")
            else:
                print(" " * 3, "→ Não há números negativos.")
            print()
            break
            
except NameError:
    print()       
        
       
    
    