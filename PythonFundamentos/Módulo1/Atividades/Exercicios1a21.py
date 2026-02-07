import os

'''21) Desenvolva um programa que leia números inteiros até que o usuário digite 0. 
   Ao final, mostre:
    - A soma de todos os números positivos
    - A média dos números pares
    - O maior e o menor número digitado
    - Quantos números negativos foram digitados
'''

numeros = []
pares = []
numeros_negativos = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\rDigite um número inteiro ou pressione [0] para sair: ", end= "", flush =True)
    numero = int(input())
    
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
        else:
            somar_pares = f"""Não há nenhum número par"""
            media_pares = f"""Não há nenhum número par"""
            
        if numero < 0:
            numeros_negativos.append(numero)
            len(numeros_negativos)
        
    else:
        print(somar)
        print(somar_pares)
        print(media_pares)
        print(max(numeros))
        print(min(numeros))
        print(len(numeros_negativos))
        break
        
    
    
       
    
    