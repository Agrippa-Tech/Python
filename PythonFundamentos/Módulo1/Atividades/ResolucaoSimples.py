'''
CÓDIGO GERADO PELO FLOWGORITHM - CARACTERÍSTICAS E LIMITAÇÕES

Este código foi gerado automaticamente a partir de um diagrama de blocos
criado no Flowgorithm, uma ferramenta educacional para ensino de lógica
de programação.

O QUE É O FLOWGORITHM?

O Flowgorithm é um software que permite criar algoritmos usando fluxogramas
(diagramas de blocos) e depois exportar o código para diversas linguagens,
incluindo Python. Ele foi desenvolvido para iniciantes aprenderem lógica
de programação de forma visual.

CARACTERÍSTICAS DO CÓDIGO GERADO:

1) ENTRADA DE DADOS SEPARADA:
   
   No Flowgorithm, existem blocos distintos no diagrama:
   - Bloco "Output" → print("mensagem")
   - Bloco "Input" → variavel = input()
   
   Por isso o código gerado sempre separa a mensagem da captura:
   
   print("\nDigite o valor de n1:")
   n1 = int(input())
   
   Isso é uma tradução LITERAL dos dois blocos separados no fluxograma.

2) ESTRUTURAS CONDICIONAIS ANINHADAS:
   
   O Flowgorithm não possui o conceito de "elif" (else if).
   Ele trabalha apenas com blocos "If/Else" que podem ser aninhados.
   
   Exemplo no Exercício 6:
   
   if media >= 7:
       print("Aprovado")
   else:
       if media <= 7 and media >= 5:  # Novo bloco If dentro do Else
           print("Recuperação")
       else:
           if media <= 5:  # Outro If aninhado
               print("Reprovado")
   
   Essa estrutura reflete a árvore de decisão do diagrama de blocos,
   onde cada "não" de um diamante leva a outro diamante de decisão.

3) CONVERSÕES EXPLÍCITAS DE TIPO:
   
   O Flowgorithm trabalha com tipos de dados bem definidos:
   - Integer (números inteiros)
   - Real (números decimais)
   - String (texto)
   
   Por isso o código gerado é mais explícito nas conversões:
   
   media = float(n1 + n2 + n3 + n4) / 4
   
   Mesmo quando a divisão já resultaria em float, o Flowgorithm
   adiciona a conversão explícita para garantir o tipo correto.

4) FORMATAÇÃO BÁSICA:
   
   O Flowgorithm gera código funcional, mas não otimizado:
   - Pode omitir especificadores de formato como :2.2f
   - Não usa recursos avançados de f-strings
   - Foco na funcionalidade, não na elegância do código

5) VERBOSIDADE:
   
   O código gerado tende a ser mais longo porque:
   - Cada ação no diagrama vira uma linha de código
   - Não combina operações que poderiam estar juntas
   - Prioriza clareza e correspondência direta com o fluxograma

POR QUE ESSAS LIMITAÇÕES EXISTEM?

O Flowgorithm é uma ferramenta EDUCACIONAL, não um compilador profissional.
Seus objetivos são:

✓ Ensinar lógica de programação de forma visual
✓ Gerar código que corresponda LITERALMENTE ao diagrama
✓ Funcionar com múltiplas linguagens (Python, C++, Java, etc.)
✓ Ser simples e compreensível para iniciantes

Não é objetivo do Flowgorithm:
✗ Gerar código otimizado ou seguindo as melhores práticas
✗ Usar recursos avançados específicos de cada linguagem
✗ Produzir código pronto para produção

VANTAGENS DO CÓDIGO GERADO PELO FLOWGORITHM:

+ Correspondência direta com o fluxograma (fácil de debugar)
+ Estrutura clara e previsível
+ Funcionalidade garantida se o diagrama estiver correto
+ Excelente para aprender a traduzir lógica em código

LIMITAÇÕES DO CÓDIGO GERADO:

- Mais verboso que código manual
- Não usa recursos modernos da linguagem
- Pode conter redundâncias (ex: media <= 7 and media >= 5)
- Não segue convenções de estilo (PEP 8 em Python)
- Formatação inconsistente

COMO USAR O FLOWGORITHM CORRETAMENTE:

1. Use o Flowgorithm para PLANEJAR a lógica do seu programa
2. Crie o diagrama de blocos e teste com diferentes valores
3. Exporte o código Python para ter uma BASE funcional
4. REFATORE o código manualmente aplicando boas práticas:
   - Combine print() e input()
   - Substitua if aninhados por elif quando apropriado
   - Adicione formatação adequada
   - Simplifique condições redundantes
   - Siga PEP 8 (guia de estilo Python)

ANALOGIA:

Flowgorithm : Python profissional
    =
Rascunho : Redação final

O diagrama organiza suas ideias (lógica), o código refinado as expressa
de forma elegante e profissional.

CONCLUSÃO:

Este código está CORRETO funcionalmente (resolve os exercícios propostos),
mas não representa as melhores práticas de Python. Use o Flowgorithm e a resolução desses exercícios como
ferramenta de aprendizado de LÓGICA e SINTAXE BÁSICA, mas sempre refine o código gerado
ao implementá-lo em projetos reais.

O verdadeiro aprendizado acontece quando você entende TANTO a lógica
(diagrama) QUANTO as boas práticas da linguagem (código refinado).
'''

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

print(f"\nO consumo médio por quilomêtro é de: {consumo_medio:2.2f}")
print(f"O custo por quilomêtro rodado é de: {custokm:2.2f}")   

'''3) Faça um programa que converta uma temperatura em Celsius para Fahrenheit e Kelvin,
   exibindo os resultados com duas casas decimais'''
   
print ("\n", "=" * 15, "EXERCÍCIO 3", "=" * 15)

print("\nDigite o valor da temperatura em Celsius (C°): ")
celsius = float(input())

fahren = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"O valor de {celsius:2.2f} graus Celsius é de {fahren:2.2f} Fahrenheit e {kelvin:2.2f} kelvin.")

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

'''5) Desenvolva um programa que calcule o tempo total em horas, minutos e segundos
   a partir de um valor dado apenas em segundos.'''

print("\n", "=" * 15, "EXERCÍCIO 5", "=" * 15)

print("\nInsira a quantidade em segundos para a conversão: ")
segundos_usuario = float(input())

horas = segundos_usuario / 3600
minutos = float(segundos_usuario % 3600) / 60
segundos_saida = segundos_usuario % 60

resposta = f"""{f'A quantidade de {segundos_usuario} segundos, convertida para:'}
{''}
{f'Horas é de: {horas:2.2f}'}
{f'Minutos é de: {minutos:2.2f}'}
{f'Segundos é de: {segundos_saida:2.2f}'}"""

print(resposta)

'''6) Crie um programa que leia três notas de um aluno, calcule a média e
    informe se ele foi aprovado (média ≥ 7), em recuperação (5 ≤ média < 7)
    ou reprovado (média < 5).'''
      
print("\n", "=" * 15, "EXERCÍCIO 6", "=" * 15)

print("\nDigite a primeira nota: ")
nota1 = float(input())
print("Digite a segunda nota: ")
nota2 = float(input())
print("Digite a terceira nota: ")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
   print(f"\nAprovado - A média do aluno foi de: {media:2.2f}")
else:
   if media <= 7 and media >= 5:
      print(f"\nRecuperação - A média foi de: {media:2.2f}")
   else:
      if media <= 5:
         print(f"\nReprovado - A média do aluno foi de: {media:2.2f}")
         
'''7) Elabore um programa que converta uma quantia em reais (R$) para dólares (US$),
    considerando uma taxa de câmbio fornecida pelo usuário.'''
    
print("\n", "=" * 15, "EXERCÍCIO 7", "=" * 15)

print("\nDigite o valor em reais: ")
reais = float(input())
print("Digite o valor da taxa de câmbio atual: ")
taxa_cambio = float(input())

conversao_dolar = reais / taxa_cambio

print(f"\nCom {reais} reais, você comprará {conversao_dolar} dólares.")

'''8) Faça um programa que calcule a área de um círculo. O usuário deve informar o raio,
   e o programa deve exibir a área com duas casas decimais (use π = 3.14159).'''
   
print("\n", "=" * 15, "EXERCÍCIO 8", "=" * 15)

print("\nDigite o raio do círculo: ")
raio = float(input())
pi = 3.14159
area_pi = pi * (raio**2)

print(f"\nA área do círculo é de {area_pi} cm²")

