
'''1) Desenvolva um programa que calcule a média aritmética de 
   quatro números inteiros fornecidos pelo usuário.'''

print ("\n", "=" * 15, "EXERCÍCIO 1", "=" * 15)

n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

media = (n1 + n2 + n3 + n4) / 4

print (f"\nA média aritmética simples dos valores é: {float(media)}")

'''2) Crie um programa que calcule o consumo médio de combustível de um veículo e o valor 
   gasto por quilomêtro. O usuário deve informar a distância percorrida (em km), o
   volume de combustível gasto (em litros) e o valor pago por litro.'''
   
print ("\n", "=" * 15, "EXERCÍCIO 2", "=" * 15)

km = float(input("\nDigite quantos quilomêtros você percorreu: "))
litro = float(input("Digite o volume de combustível gasto em litros de combustível: "))
valor = float(input("Digite quantos reais você pagou por cada litro? "))

consumo_medio = km / litro
custo_km = valor / consumo_medio

print(f"\nO consumo médio do seu veículo por quilomêtros é de: {consumo_medio:2.2f} (km/L).") 
print(f"O custo por quilomêtro rodado é de {custo_km:2.2f} reais.")

'''3) Faça um programa que converta uma temperatura em Celsius para Fahrenheit e Kelvin,
   exibindo os resultados com duas casas decimais'''
   
print ("\n", "=" * 15, "EXERCÍCIO 3", "=" * 15)

c = float(input("\nDigite o valor da temperatura em graus Celsius (C°): "))

f = (c * 9/5) + 32
k = c + 273.15

print(f"\nO valor de {c:2.2f} graus Celsius é de {f:2.2f} Fahrenheit e {k:2.2f} Kelvin")

'''4) Elabore um programa que calcule o valor final de uma compra com desconto. 
   O usuário deve informar o preço original e a porcentagem de desconto. O programa deve
   exibir o valor do desconto e o preço final.'''
   
print ("\n", "=" * 15, "EXERCÍCIO 4", "=" * 15)

vo = float(input("\nDigite o valor original pago: "))
vd = int(input("Digite a porcentagem de desconto aplicado: "))

vf = vo * (1 - vd / 100)

print(f"O valor final da sua compra é de: {vf:2.2f} reais.")

'''5) Desenvolva um programa que calcule o tempo total em horas, minutos e segundos
   a partir de um valor dado apenas em segundos.'''
   
print("\n", "=" * 15, "EXERCÍCIO 5", "=" * 15)

seg_in = float(input("\nInsira a quantidade em segundos para a conversão: "))

hrs = seg_in / 3600
mts = seg_in % 3600 / 60
seg_out = seg_in % 60

rst = f"""\nA quantidade de {seg_in:.1f} convertida para:
        {'Horas é de:':<30} {hrs:>10.2f}
        {'Minutos é de:':<30} {mts:>10.2f}
        {'Segundos é de:':<30} {seg_out:>10.2f}
        """

print(rst)

'''6) Crie um programa que leia três notas de um aluno, calcule a média e
    informe se ele foi aprovado (média ≥ 7), em recuperação (5 ≤ média < 7)
    ou reprovado (média < 5).'''
    
print("\n", "=" * 15, "EXERCÍCIO 6", "=" * 15)

n1 = float(input("\nInsira a primeira nota do aluno: "))
n2 = float(input("Insira a segunda nota do aluno: "))
n3 = float(input("Insira a terceira nota do aluno: "))

ma = (n1 + n2 + n3) /3

if ma >= 7:
    print(f"\n{'Média: ':>15} {ma:2.2f} - Aprovado.")
elif ma >= 5:
    print(f"\n{'Média: ':>15} {ma:2.2f} - Recuperação.")
else:
    print(f"\n{'Média: ':>15} {ma:2.2f} - Reprovado.")
    

'''7) Elabore um programa que converta uma quantia em reais (R$) para dólares (US$),
    considerando uma taxa de câmbio fornecida pelo usuário.'''
    
print("\n", "=" * 15, "EXERCÍCIO 7", "=" * 15)

real = float(input("\nInsira o valor em reais: "))
txc = float(input("Insira o valor da taxa de câmbio atual: "))

usd = real / txc

print(f"\n{'Com':>10} {real:2.2f} reais, você comprará {usd:2.2f} dólares.")


'''8) Faça um programa que calcule a área de um círculo. O usuário deve informar o raio,
   e o programa deve exibir a área com duas casas decimais (use π = 3.14159).'''
   
print("\n", "=" * 15, "EXERCÍCIO 8", "=" * 15)

r = float(input("\nDigite o raio da área calculada: "))

π = 3.14159
A = π * (r**2)

print(f"\nA área do círculo é de: {A:2.2f} cm²")


'''9) Crie um programa que inverta a ordem de dois números fornecidos pelo usuário e,
   em seguida, calcule a diferença absoluta entre eles.'''

print("\n", "=" * 15, "EXERCÍCIO 9", "=" * 15)
   
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

nums = [num1, num2]
nums.reverse()

dif = abs(nums[0] - nums[1])

print(f"\nA ordem dos números invertida é: \n{nums[0]:>15} - {nums[1]}")
print(f"\nA diferença absoluta entre eles é: \n{dif:>15}")

'''10) Desenvolva um programa que calcule o valor do IMC (Índice de Massa Corporal).
   O usuário deve informar peso (kg) e altura (m). O programa deve exibir o IMC com duas
   casas decimais.'''
  
print("\n", "=" * 15, "EXERCÍCIO 10", "=" * 15)
 
kg = float(input("\nDigite quantos quilogramas você pesa: "))
al = float(input("Digite quantos metros você mede: "))

imc = kg / (al ** 2) 

print(f"O seu IMC é de: {imc:2.2f}")

'''11) '''