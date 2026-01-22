import lmp  
import secrets
import string
import time
import os  

lmp.limpar_terminal()

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
nums.reverse() #inverte os valores da lista

dif = abs(nums[0] - nums[1]) #transforma os números para int indepedente do resultado

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

'''11) Desenvolva um programa que calcule o valor do juros simples de uma aplicação financeira.
   O usuário deve informar o capital inicial, a taxa de juros mensal e o tempo em meses.'''
   
print("\n", "=" * 15, "EXERCÍCIO 11", "=" * 15)

cpt = float(input("\nInsira o valor aplicado em reais: "))
txj = float(input("Insira a porcentagem da taxa de juros mensal da aplicação: "))
tm = int(input("Insira a quantidade de meses que deseja realizar o resgaste: "))

txj_dec = txj / 100

js = cpt * txj_dec * tm
mnt = cpt + js

rst1 = f"""\n{'Aplicando R$':>15} {cpt:2.2f} por {tm} meses você terá: 
            {'Um lucro de R$':>10} {js:2.2f}
            {'Um montante de R$':>10} {mnt:2.2f}
         """
            
print(rst1)

'''12) Crie um programa que converta uma velocidade de km/h para m/s e vice-versa.
   O usuário deve escolher qual conversão deseja fazer e informar o valor.
'''

print("\n", "=" * 15, "EXERCÍCIO 12", "=" * 15)

print("\nDeseja converter para qual medida de velocidade?")
print(f"\n{'Aperte [1] para converter Km/h para M/s':>30}")
print(f"{'Aperte [2] para converter M/s para Km/h':>30}")

try:
   ops = int(input("\n"))

   if ops == 1:
      vlc = float(input("Insira o valor a ser convertido: "))
      ms = vlc / 3.6
      print(f"\nA velocidade de {vlc:2.2f} km/h convertida para m/s é: {ms:2.2f}")
   elif ops == 2:
      vlc = float(input("Insira o valor a ser convertido: "))
      km = vlc * 3.6
      print(f"\nA velocidade de {vlc:2.2f} m/s convertida para km/h é: {km:2.2f}")
   else: 
      print("\nOpção inválida!")

except ValueError:
   print("\nERRO: Digite apenas números.")
   
'''13) Faça um programa que calcule a quantidade de tinta necessária para pintar uma parede.
   O usuário deve informar a altura e largura da parede (em metros) e o programa deve calcular
   a área e a quantidade de tinta (cada litro pinta 3m²).'''
   
print("\n", "=" * 15, "EXERCÍCIO 13", "=" * 15)

alt = float(input("\nDigite a altura da parede em metros: " ))
lag = float(input("Digite a largura da parede em metros: "))
area_p = alt * lag

print("\nHá alguma área não pintável?")
print(f"\n{'Aperte [1] para SIM:':>30}")
print(f"{'Aperte [2] para NÃO:':>30}")

opcs = int(input("\n")) 

if opcs == 1:
   alt_np = float(input("\nDigite a altura da área não pintável: "))
   lag_np = float(input("Digite a largura da área não pintável: "))
   area_liq = area_p - (alt_np * lag_np)
   tinta_liq = area_liq / 3
   print(f"\nPara pintar a área líquida da sua parede será necessário {tinta_liq:2.2f} litros de tinta para cada demão.")
elif opcs == 2:
   tinta_brt = area_p / 3
   print(f"\nPara pintar a área da sua parede será necessário {tinta_brt:2.2f} litros de tinta para cada demão.")
   
'''14) Desenvolva um programa que leia três números diferentes e exiba-os em ordem crescente.'''

print("\n", "=" * 15, "EXERCÍCIO 14", "=" * 15)

try:
   nm1 = float(input("\nDigite o primeiro número: "))
   nm2 = float(input("Digite o segundo número: "))
   nm3 = float(input("Digite o terceiro número: "))
   
   if nm1 == nm2 or nm2 == nm3 or nm3 ==nm1:
      raise ValueError ("ERRO: Digite números diferentes.")
   
   nms = [nm1, nm2, nm3]
   nms.sort()  #ordena a lista de forma crescente
   
   print(f"\nNúmeros ordenados de forma crescente: ")
   print(nms) 

except ValueError: 
   print("ERRO: Digite números diferentes.")

'''15) Crie um programa que calcule o valor da conta de energia elétrica.
   O usuário deve informar o consumo em kWh e o programa deve calcular o valor considerando
   R$ 0,75 por kWh mais uma taxa fixa de R$ 25,00.'''

print("\n", "=" * 15, "EXERCÍCIO 15", "=" * 15)

try:
   print("\n", " " * 10, "CALCULADORA ENERGIA", " " * 10)
   
   comp_senh = string.digits #números de 0 a 9
   tam_senh = 6
   senh = ''.join(secrets.choice(comp_senh) for _ in range(tam_senh))
   tent = 4
   
   print(f"\nSua senha de acesso é: {senh}")
   time.sleep(10)
   os.system('cls' if os.name == 'nt' else 'clear')
   
   
   while tent > 0:
    teste_senh =(input("Digite sua senha de acesso: "))
    if teste_senh == senh:
        break
    else:
        tent -= 1
        if tent > 0:
            print(f"\nSenha incorreta. Faltam apenas {tent} tentativas.")
        else:
            print("\nERRO: Tentativas esgotadas.")
    if tent == 0:  
        raise Exception ()
      
   
   ckwh = float(input("\nDigite o consumo elétrico em kWh: "))

   custo_ele = (ckwh * 0.75) + 25

   if ckwh <= 100:
      nvl = 'Ótimo'
   elif ckwh <= 200:
      nvl = 'Bom'
   elif ckwh <= 350:
      nvl = 'Ok'
   elif ckwh <= 500:
      nvl = 'Ruim'
   else:
      nvl = 'Péssimo'

   blt = f"""
            {'= '* 15} {'CONTA DE ENERGIA'} {'= ' * 15}
            {'Consumo kWh:':>15} {ckwh:2.2f}
            {'Tarifa por kWh:':>18} {'R$ 0.75'}
            {'Tarifa fixa:':>15} {'R$: 25.00'}
            {'= ' * 39}
            {'CUSTO TOTAL:':>15} {'R$'}{custo_ele:2.2f}
            {'CLASSIFICAÇÃO:':>17} {nvl}
         """
            
   print(blt)

except ValueError:
   print("\nERRO: Digite apenas números.")
except Exception as e:
    print()
    
'''16) Elabore um programa que converta uma quantidade de horas em semanas, dias e horas.
   Exemplo: 500 horas = 2 semanas, 6 dias e 20 horas.''' 
