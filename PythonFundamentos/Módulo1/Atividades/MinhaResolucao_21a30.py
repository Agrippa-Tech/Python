import os
import time
import secrets


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

input("Pressione Enter para continuar...")

'''22) Crie um programa de adivinhação de número. O programa deve gerar um número 
       entre 1 e 100, e o usuário tem 10 tentativas para acertar. A cada 
       tentativa, o programa deve informar se o palpite é maior ou menor que o número 
       secreto. Se acertar, mostrar quantas tentativas foram usadas. Se esgotar as 
       tentativas, revelar o número.'''    
    
print("\n", "=" * 15, "EXERCÍCIO 22", "=" * 15)


ranking_usuario = {}
usuario_atual = None

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n", "=" * 15, "JOGO DA ADVINHAÇÃO", "=" * 15)
    
    print()
    print("[1] Jogar")
    print("[2] Cadastrar Usuário")
    print("[3] Ranking")
    print("[4] Sair")
    
    try:
        print()
        opcoes_jogo = int(input())
        
        if opcoes_jogo < 1 or opcoes_jogo > 4:
            raise ValueError
        
    except ValueError:
        print("\nDigite apenas números válidos.")
        break
    
    if opcoes_jogo == 1:
        if usuario_atual is None:
            usuario_atual = "Anônimo"
        
        numero_aleatorio = secrets.randbelow(100)
        tentativas_advinhar = 10
        while tentativas_advinhar > 0:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n", "=" * 15, "JOGO DA ADVINHAÇÃO", "=" * 15)
            print()
            
            animacao_escolha =  "Escolhendo o número da sorte entre 0 e 100"
            for i in range (1 , len(animacao_escolha)):
                print(f"\r{animacao_escolha[:i]}", end = " ", flush = True)
                time.sleep(0.1)
            for i in range(1, 4):
                print(f"\r{animacao_escolha}{'.' * i}", end = " ", flush = True)
                time.sleep(0.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nEscolhi! Vamos começar!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                numero_usuario = int(input("\nDigite o número da sorte (0 - 100): "))
            except ValueError:
                print("\nERRO: DIGITE APENAS NÚMEROS INTEIROS")
                continue
            
            if numero_usuario == numero_aleatorio:
                print(f"\nParabéns! Você acertou em {tentativas_advinhar} tentativas!")
                print()
                
                pontuacao = tentativas_advinhar * 10
                
                if usuario_atual in ranking_usuario:
                    ranking_usuario[usuario_atual] += pontuacao
                else:
                    ranking_usuario[usuario_atual] = pontuacao
                
                opcao_acerto = int(input("\nPressione [1] para continuar ou [2] para sair: "))
                if opcao_acerto == 1:
                    numero_aleatorio = secrets.randbelow(100)
                    continue
                elif opcao_acerto == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                
            elif numero_usuario != numero_aleatorio:
                tentativas_advinhar -= 1
                print("\nVocê errou. Tente novamente.")
                print(f"Restam {tentativas_advinhar} tentativas.")
                
                time.sleep(0.8)
                if abs(numero_usuario - numero_aleatorio) <= (numero_aleatorio * 0.10):
                    print("\nVocê chegou muito perto! Quase acertou!")
                    continue
                if numero_usuario > numero_aleatorio:
                    print("\nO número da sorte é um pouco menor...")
                else:
                    print("\nO número da sorte é um pouco maior...")
                time.sleep(4)
                os.system('cls' if os.name == 'nt' else 'clear')

    if opcoes_jogo == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("\n", "=" * 15, "CADASTRO", "=" * 15)
            print()
            nome = input("Digite o nome do usuário: ").strip()
            
            if not nome:
                nome = "Anônimo"
            
            if nome == nome:
                usuario_atual = nome
                print(f"\nBem-vindo {usuario_atual}!")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                break
            
    if opcoes_jogo == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n", "=" * 15, "RANKING", "=" * 15)
        print()
        
        if not ranking_usuario:
            print("Nenhum jogador cadastrado.")
            time.sleep(1)
        else:
            ranking_ordenado = sorted(ranking_usuario.items(), key = lambda x: x[1], reverse = True)

            print(f"{'Posição':<10} {'Nome':<20} {'Pontuação':<10}")
            print("=" * 40)
            
            posicao = 1
            for nome, pontuacao in ranking_ordenado:
                print(f"{posicao:<10} {nome:<20} {pontuacao:<10}")
                posicao += 1
            print()
            input("Pressione Enter para voltar ao menu...")
            os.system('cls' if os.name == 'nt' else 'clear')
                
    if opcoes_jogo == 4:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        opcao_saindo = "Saindo..."
        for i in range(1, len(opcao_saindo) + 1):
            print(f"\r{opcao_saindo[:i]}", end = " ", flush = True)
            time.sleep(0.3) 
        break
