'''1) Desenvolva um programa que calcule a média aritmética de 
   quatro números inteiros fornecidos pelo usuário.'''
   
print ("\n", "=" * 15, "EXERCÍCIO 1", "=" * 15)
   
print("\nDigite o valor de n1:")
n1 = int(input())
print("\rDigite o valor de n2:")
n2 = int(input())
print("\rDigite o valor de n3:")
n3 = int(input())
print("\rDigite o valor de n4:")
n4 = int(input())

media = float(n1 + n2 + n3 + n4) / 4

print("\rA média dos quatro números é: ")
print(media)

'''2) Crie um programa que calcule o consumo médio de combustível de um veículo e o valor 
   gasto por quilomêtro. O usuário deve informar a distância percorrida (em km), o
   volume de combustível gasto (em litros) e o valor pago por litro.'''
  
print ("\n", "=" * 15, "EXERCÍCIO 2", "=" * 15)
 
print("Digite quantos quilomêtros você percorreu: ")
km = float(input())
print("Digite o volume de combustível gasto por litro: ")
litro = float(input())
print("Digite quantos reais você pagou por litro: ")
valor_combustivel = float(input())

consumo_medio = km / litro
custokm = valor_combustivel / consumo_medio

print("\nO consumo médio por quilomêtro é de: " + str(litro))
print("O custo por quilomêtro rodado é de: " + str(custokm))   
