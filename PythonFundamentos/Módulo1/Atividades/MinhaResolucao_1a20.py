import secrets
import string
import time
import os 
from datetime import date
import calendar

os.system('cls' if os.name == 'nt' else 'clear')

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
litro = float(input("Digite o volume de combustível gasto em litros: "))
valor = float(input("Digite quantos reais você pagou por cada litro? "))

consumo_medio = km / litro
custo_km = valor / consumo_medio

print(f"\nO consumo médio do seu veículo por quilomêtros é de: {consumo_medio:2.2f} (km/L).") 
print(f"O custo por quilomêtro rodado é de {custo_km:2.2f} reais.")

'''3) Faça um programa que converta uma temperatura em Celsius para Fahrenheit e Kelvin,
   exibindo os resultados com duas casas decimais'''
   
print ("\n", "=" * 15, "EXERCÍCIO 3", "=" * 15)

celsius = float(input("\nDigite o valor da temperatura em graus Celsius (C°): "))

fahren = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\nO valor de {celsius:2.2f} graus Celsius é de {fahren:2.2f} Fahrenheit e {kelvin:2.2f} Kelvin")

'''4) Elabore um programa que calcule o valor final de uma compra com desconto. 
   O usuário deve informar o preço original e a porcentagem de desconto. O programa deve
   exibir o valor do desconto e o preço final.'''
   
print ("\n", "=" * 15, "EXERCÍCIO 4", "=" * 15)

valor_original = float(input("\nDigite o valor original pago: "))
valor_desconto = int(input("Digite a porcentagem de desconto aplicado: "))

valor_final = valor_original * (1 - valor_desconto / 100)

print(f"O valor final da sua compra é de: {valor_final:2.2f} reais.")

'''5) Desenvolva um programa que calcule o tempo total em horas, minutos e segundos
   a partir de um valor dado apenas em segundos.'''

  
print("\n", "=" * 15, "EXERCÍCIO 5", "=" * 15)

seg_input = float(input("\nInsira a quantidade em segundos para a conversão: "))

hrs = seg_input / 3600
mts = seg_input % 3600 / 60
seg_output = seg_input % 60

rst = f"""\nA quantidade de {seg_input:.1f} convertida para:
        {'Horas é de:':<30} {hrs:>10.2f}
        {'Minutos é de:':<30} {mts:>10.2f}
        {'Segundos é de:':<30} {seg_output:>10.2f}
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
      vlc = float(input("\nInsira o valor a ser convertido: "))
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
   
print("\n", "=" * 15, "EXERCÍCIO 16", "=" * 15)

print("\n", "=" * 15, "CONVERSOR DE TEMPO", "=" * 15)

try: 
   qtd = int(input("\nDigite uma quantidade de horas: "))

   semanas = qtd / 168
   resto_hrs = qtd % 168
   dias = resto_hrs / 24
   horas = resto_hrs % 24
   tent = 4
   

   print(f"\nDeseja converter para uma medida específica?")
   print(f"Digite [1] para SIM:")
   print(f"Digite [2] para NÃO:")

   opcoes = int(input("\n"))
   
   if opcoes == 1:
      print(f"\nPara qual medida deseja converter a quantidade de horas?")
      print(f"\nPara SEMANAS aperte [1]:")
      print(f"Para DIAS aperte [2]:")
      
      opcoes_if = int(input("\n"))
      
      if opcoes_if == 1:
         print(f"A quantidade de {qtd} horas é equivalente a {semanas:2.2f} semana(s).")
      elif opcoes_if == 2:
         print(f"A quantidade de {qtd} horas é equivalente a {dias:2.2f} dia(s).")
   elif opcoes == 2:
      print(f"\nA quantidade de {qtd} horas é equivalente a: ")
      outp_opcs2 = f"""{'':>15}{semanas:2.2f} {'= semana(s)'} 
               {dias:2.2f} {'= dias(s)'}
               {horas:2.2f} {'= hora(s)'}
                  """
      print(outp_opcs2)
   elif opcoes != 1 or opcoes != 2:
      raise ValueError()
   
except ValueError: 
   os.system('cls' if os.name == 'nt' else 'clear')
   print("\nERRO: Digite apenas [1] ou [2]")
   time.sleep(2)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("\nERRO: Digite apenas [1] ou [2]")
   time.sleep(2)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("\nERRO: Digite apenas [1] ou [2]")
   time.sleep(2)
   os.system('cls' if os.name == 'nt' else 'clear')
   
'''17) Faça um programa que calcule o peso ideal de uma pessoa.
   Para homens: (72.7 * altura) - 58. Para mulheres: (62.1 * altura) - 44.7.
   O usuário deve informar altura e sexo.'''
   
print("\n", "=" * 15, "EXERCÍCIO 17", "=" * 15)

altura = None
tentativas_altura = 4
while tentativas_altura > 0:
    print(f"\nDigite sua altura em metros: ")
    
    try:
        altura = float(input())
        break
    except ValueError:
        tentativas_altura -= 1
        if tentativas_altura == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nA última tentativa será possível em 30 segundos.")
            time.sleep(5)
            for i in range (30, 0, -1):
                print(f"\r {i} segundos.", end = " ", flush = True)
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        if tentativas_altura > 0:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nERRO: Digite apenas números.")
            print(f"Você tem somente {tentativas_altura} tentativas.")
            continue
        else:
            print(f"\nTentativas esgotadas.")
        break
        

if altura is None:
    print(f"\nERRO: Reinicie o programa.")
else:
    tentativas_peso = 4
    while tentativas_peso > 0:
        print(f"\nQual o seu gênero?")
        print(f"\n", " " * 4,"[1] Masculino")
        print(f" " * 5, "[2] Feminino")
        
        try:
            genero = int(input("\n"))
        except ValueError:
            tentativas_peso -= 1
            if tentativas_peso == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nA última tentativa será possível em 30 segundos.")
                time.sleep(5)
                for i in range (30, 0, -1):
                    print(f"\r {i} segundos.", end = " ", flush = True)
                    time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            if tentativas_peso > 0:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\nERRO: Digite apenas [1] ou [2].")
                print(f"Você tem somente {tentativas_peso} tentativas.")
                continue 
            else:
                print("\nTentativas esgotadas.")
            break
        
        if genero == 1:
            peso_ideal = (72.7 * altura) - 58
            print(f"\nConsiderando sua altura de {altura:2.2f} metros,"
                f" seu peso ideal seguindo os critérios de Lorentz é de {peso_ideal:2.2f} kg.")
            break
        elif genero == 2:
            peso_ideal = (62.1 * altura) - 44.7
            print(f"\nConsiderando sua altura de {altura:2.2f} metros,"
                f" seu peso ideal seguindo os critérios de Lorentz é de {peso_ideal:2.2f} kg.")
            break
        else:
            tentativas_peso -= 1
            if tentativas_peso > 0:
                print(f"\nDigite apenas números.")
                print(f"Você tem somente {tentativas_peso} tentativas.")
                continue 
            else:
                print("\nTentativas esgotadas.")
            break

'''18) Desenvolva um programa que calcule o troco mínimo em cédulas e moedas para uma compra.
   O usuário informa o valor da compra e o valor pago.'''
   
print("\n", "=" * 15, "EXERCÍCIO 18", "=" * 15)

dinheiro = (200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05)

tentativa_valor = 4
valor_compra = None
valor_pago = None

while tentativa_valor > 0:
   try:
      valor_compra = float(input("\nDigite o valor da compra: "))
      valor_pago = float(input("Digite o valor pago: "))
      break
   except ValueError:
      tentativa_valor -= 1
      if tentativa_valor == 1:
         os.system('cls' if os.name == 'nt' else 'clear')
         print(f"\nERRO: Digite apenas números ou utilize [.] para separar as casas decimais.")
         print(f"\nA última tentativa será possível em 30 segundos.")
         time.sleep(5)
         for i in range(30, 0, -1):
            print(f"\r{i} segundos.", end = " ", flush = True)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
      if tentativa_valor > 0:
         time.sleep(2)
         os.system('cls' if os.name == 'nt' else 'clear')
         print(f"\nERRO: Digite apenas números ou utilize [.] para separar as casas decimais.")
         print(f"Você tem somente {tentativa_valor} tentativas restantes.")
         continue
      else:
         print(f"\nTENTATIVAS ESGOTADAS")
      break

if valor_compra is not None and valor_pago is not None:
   troco = valor_pago - valor_compra
   
   if troco < 0:
      print("\nValor pago é insuficiente!")
   elif troco == 0:
      print("\nNão há troco a ser dado.")
   else: 
      print(f"\nTroco total: R$ {troco:.2f}")
      print(f"Cédulas e moedas necessárias: ")
      print()
      
      troco_restante = troco
      
      for valor in dinheiro:
         quantidade = 0
         
         if troco_restante >= valor - 0.001:
            quantidade = int(troco_restante // valor)
            troco_restante -= quantidade * valor
            troco_restante = round(troco_restante, 2)
         
         if quantidade > 0:
            if valor >= 1:
               print(f"{'Cédula(s) de R$':>20} {valor:>5.2f} : {quantidade:>10}")
            else:
               print(f"{'Moeda(s) de R$':>20} {valor:>5.2f} : {quantidade:>10}")

'''19) Crie um programa que leia dois números e mostre qual é o maior e qual é o menor,
   ou se são iguais.'''

print("\n", "=" * 15, "EXERCÍCIO 19", "=" * 15)

try:
    sair = False
    while not sair:
        tentativa_num = 4
        while tentativa_num > 0:
            try:
                numero1 = float(input("\nDigite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
            except Exception:
                tentativa_num -= 1
                if tentativa_num == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nA última tentativa será possível em 30 segundos.")
                    time.sleep(5)
                    for i in range (30, 0, -1):
                        print(f"\r {i} segundos", end = " ", flush = True)
                        time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                if tentativa_num > 0:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERRO: Digite apenas números.")
                    print(f"\nVocê tem somente {tentativa_num} tentativas restantes.")
                    continue
                else:
                    print()
                raise Exception
            
            if numero1 > numero2:
                print(f"\nO primeiro número, {numero1}, é o maior do conjunto inserido.")
            elif numero2 > numero1:
                print(f"\nO segundo número, {numero2}, é o maior do conjunto inserido.")
            elif numero1 == numero2:
                print(f"\nAmbos os números, {numero1} e {numero2}, são iguais.")
            else:
                raise ValueError

            tentativa_menu = 4
            while tentativa_menu > 0:
                try:
                    print()
                    print(" " * 5, "Para sair do programa aperte:")
                    print(" " * 10,  "[1] Para encerrar")
                    print(" " * 10, "[2] Para continuar")
                    print()
                            
                    saida = int(input())
                    
                    if saida == 1:
                        print("\nSaindo...")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for i in range (5, 0, -1):
                            print(f"\rO programa será encerrado em {i} segundos.", end = " ", flush = True)
                            time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sair = True
                        break
                    elif saida == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        raise ValueError
                except ValueError:
                    tentativa_menu -= 1
                    if tentativa_menu == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nA última tentativa será possível em 30 segundos.")
                        time.sleep(5)
                        for i in range (30, 0, -1):
                            print(f"\r{i} segundos.", end = " ", flush = True)
                            time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if tentativa_menu > 0:
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nDigite apenas [1] ou [2]")
                        print(f"\nVocê tem somente {tentativa_menu} tentativas restantes.")
                        continue
                    else:
                        raise ValueError 
            if sair == True:
                break         
except Exception as e:
        print("\nERRO: Tentativas esgotadas.")
  
'''20) Faça um programa que calcule a idade de uma pessoa em anos, meses e dias. O usuário deve informar sua data de nascimento,
   e o programa converte para o total de anos, meses e dias.'''
   
print("\n", "=" * 15, "EXERCÍCIO 20", "=" * 15)

while True:
    tentativas_corretas = False
    tentativas_nascimento = 4
    while tentativas_nascimento > 0:
        try:
            print("\n", "=" * 15, "CALCULADORA DE IDADE", "=" * 15)

                #entrada
            dia_nascimento = int(input("\nDigite o dia de seu nascimento: "))
            if not (1 <= dia_nascimento <= 31):
                print("\nInsira um dia válido.")
                raise ValueError
            mes_nascimento = int(input("Digite o mês do seu nascimento: "))
            if not (1 <= mes_nascimento <= 12):
                print("\nInsira um mês válido.")
                raise ValueError
            ano_nascimento = int(input("Digite o ano do seu nascimento: "))
            
            date(ano_nascimento, mes_nascimento, dia_nascimento)
            
            print()
            tentativas_corretas = True
            break
        except ValueError as erro:
            tentativas_nascimento -= 1
            if tentativas_nascimento == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nA última tentativa será possível em 30 segundos.")
                time.sleep(5)
                for i in range(30, 0, -1):
                    print(f"\r {i} segundos.", end = " ", flush = True)
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            if tentativas_nascimento > 0:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nERRO: Digite apenas números válidos.")
                print(f"Você tem somente {tentativas_nascimento} tentativas.")
                continue
            else:
                print("\n⁴⁰⁴ Error ⁴⁰⁴: TENTATIVAS ESGOTADAS.")
                print()
                exit()
            break 

    if tentativas_corretas: 
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

            #definindo as datas
        data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        data_atual = date.today()
        

            #calculos idade total
        anos_user = data_atual.year - data_nascimento.year
        meses_user = anos_user * 12 + (data_atual.month - data_nascimento.month)
        dias_user = (data_atual - data_nascimento).days
        semanas_user = dias_user // 7
        horas_user =  dias_user * 24
        minutos_user = horas_user * 60
        segundos_user = minutos_user * 60

        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            anos_user -= 1
            meses_user -= 1

            #calculos idade exata
        meses_user_rest = data_atual.month - data_nascimento.month
        if data_atual.day < data_nascimento.day:
            meses_user_rest -= 1
        if meses_user_rest < 0:
            meses_user_rest += 12

        mes_atual = data_atual.month
        ano_atual = data_atual.year 
                
        if data_atual.day < data_nascimento.day:
            mes_atual -= 1
            if mes_atual == 0:
                mes_atual = 12
                ano_atual -= 1

        dia_limite_mes = calendar.monthrange(ano_atual, mes_atual)[1]
        dia_atual = min(data_nascimento.day, dia_limite_mes)       
        ultimo_aniversario_mes = date(ano_atual, mes_atual, dia_atual)
        dias_user_restante = (data_atual - ultimo_aniversario_mes).days    

        #animacao 
        terminal_calculando = "C a l c u l a n d o"
        for i in range(1, len(terminal_calculando) + 1):
            print(f"\r{terminal_calculando[:i]}", end = " ", flush = True)
            time.sleep(0.2)

        for i in range(1, 4):
            print(f"\r{terminal_calculando}{'.' * i}", end = " ", flush = True)
            time.sleep(0.3)

        os.system('cls' if os.name == 'nt' else 'clear')

            #print
        anos_user = str(anos_user).zfill(3)  
        meses_user_rest = str(meses_user_rest).zfill(3)
        dias_user_restante = str(dias_user_restante).zfill(2)
        meses_user = str(meses_user).zfill(5)  
        semanas_user = str(semanas_user).zfill(5)
        dias_user = str(dias_user).zfill(6)
        horas_user = str(horas_user).zfill(7)
        minutos_user = str(minutos_user).zfill(8)
        segundos_user = str(segundos_user).zfill(9)
        
        res = f"""{' '}
                {'╭'}{'────' * 25:>12}{'╮'}
                {'│':<10} {'│':>91}
                {'│':<10}{'𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃 CALCULADORA DE IDADE 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃':>60} {'│':>31}
                {'│':<10} {'│':>91}
                {'│'}{'────' * 25}{'│'}
                {'│':<5}{'Data de nascimento: '}{data_nascimento.strftime('%d/%m/%Y')}{'│':>67}
                {'│':<5}{'Data atual: '}{data_atual.strftime('%d/%m/%Y')}{'│':>75}
                {'│':<5}{'Idade: '}{anos_user}{' anos, '}{meses_user_rest}{' meses e '}{dias_user_restante}{' dias':<15}{'│':>51}
                {'│':<10} {'│':>91}
                {'│':<10}{'• ':>5} {anos_user}{' anos'} {meses_user:>15}{' meses'} {semanas_user:>15}{' semanas'} {dias_user:>15}{' dias'} {'│':>10}
                {'│':<10}{'• ':>5} {horas_user}{' horas'} {minutos_user:>15}{' minutos'} {segundos_user:>13}{' segundos'} {'│':>25}
                {'╰'}{'────' * 25}{'╯'}"""
                
        res_aniversario = f"""{' '}
                {'╭'}{'────' * 25:>12}{'╮'}
                {'│':<10} {'│':>91}
                {'│':<10}{'𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃 CALCULADORA DE IDADE 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃':>60} {'│':>31}
                {'│':<10} {'│':>91}
                {'│'}{'────' * 25}{'│'}
                {'│':<5}{'Data de nascimento: '}{data_nascimento.strftime('%d/%m/%Y')}{'│':>67}
                {'│':<5}{'Data atual: '}{data_atual.strftime('%d/%m/%Y')}{'│':>75}
                {'│':<5}{'Idade: '}{anos_user}{' anos, '}{meses_user_rest}{' meses e '}{dias_user_restante}{' dias':<15}{'│':>51}
                {'│':<10} {'│':>91}
                {'│':<5}{'⋆✴︎˚｡⋆  FELIZ ANIVERSÁRIO! ⋆✴︎˚｡⋆':>60}{'│':>39}
                {'│':<10} {'│':>91}
                {'│':<10}{'• ':>5} {anos_user}{' anos'} {meses_user:>15}{' meses'} {semanas_user:>15}{' semanas'} {dias_user:>15}{' dias'} {'│':>10}
                {'│':<10}{'• ':>5} {horas_user}{' horas'} {minutos_user:>15}{' minutos'} {segundos_user:>13}{' segundos'} {'│':>25}
                {'╰'}{'────' * 25}{'╯'}
                {' '}
                """       
                  
        if data_nascimento.month == data_atual.month and data_nascimento.day == data_atual.day:
            print(res_aniversario)
        else:
            print(res)

            #menu saida
        tentativas_saida = 4
        while tentativas_saida > 0:
            try: 
                print()
                print(" " * 5, "Para sair do programa aperte:")
                print(" " * 10,  "[1] Para encerrar")
                print(" " * 10, "[2] Para continuar")
                print()
                
                escolha = int(input())
                
                if escolha == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    terminal_saindo = "Saindo"
                    for i in range(1, len(terminal_saindo) + 1):
                        print(f"\r{terminal_saindo[:i]}", end = " ", flush = True)
                        time.sleep(0.3)
                    for i in range(1, 4):
                        print(f"\r{terminal_saindo}{'.' * i}", end = " ", flush = True)
                        time.sleep(0.3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exit()
                elif escolha == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    raise ValueError
            except ValueError as e:
                tentativas_saida -= 1
                if tentativas_saida == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nA última tentativa será possível em 30 segundos.") 
                    time.sleep(5)
                    for i in range(30, 0, -1):
                        print(f"\r{i} segundos.", end = " ", flush = True)
                        time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                if tentativas_saida > 0:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERRO: Digite apenas [1] ou [2].")
                    print(f"\nVocê tem somente {tentativas_saida} tentativas restantes.")
                    continue
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERRO: Digite apenas [1] ou [2].")
                    print()
                    exit()
   
   