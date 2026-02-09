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
 
print("\nDigite quantos quilomêtros você percorreu: ")
km = float(input())
print("Digite o volume de combustível gasto por litro: ")
litro = float(input())
print("Digite quantos reais você pagou por litro: ")
valor_combustivel = float(input())

consumo_medio = km / litro
custokm = valor_combustivel / consumo_medio

print(f"\nO consumo médio por quilomêtro é de: {litro:2.2f}")
print(f"O custo por quilomêtro rodado é de: {custokm:2.2f}")   

'''3) Faça um programa que converta uma temperatura em Celsius para Fahrenheit e Kelvin,
   exibindo os resultados com duas casas decimais'''
   
print ("\n", "=" * 15, "EXERCÍCIO 3", "=" * 15)

print("\nDigite o valor da temperatura em Celsius (C°): ")
celsius = float(input())

fahren = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"O valor de {celsius:2.2f} graus Celsius é de {fahren} Fahrenheit e {kelvin:2.2f} kelvin.")

'''4) Elabore um programa que calcule o valor final de uma compra com desconto. 
   O usuário deve informar o preço original e a porcentagem de desconto. O programa deve
   exibir o valor do desconto e o preço final.'''
   
print ("\n", "=" * 15, "EXERCÍCIO 4", "=" * 15)

print("\nDigite o valor original do produto: ")
valor_original = float(input())
print("Digite a porcentagem de desconto: ")
valor_desconto = float(input())

valor_final = valor_original * (1 - valor_desconto / 100)

print(f"\nO valor final da sua compra é de R${valor_final:2.2f}.")