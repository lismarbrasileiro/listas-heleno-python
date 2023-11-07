#questão01:
# Inicializa a variável de contagem de valores negativos
contagem_negativos = 0

# Loop para ler 5 valores
for i in range(5):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    
    # Verifica se o valor é negativo
    if valor < 0:
        contagem_negativos += 1

# Imprime o número de valores negativos
print(f"Total de valores negativos: {contagem_negativos}")
#questão 02
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def calcular_e(n):
    e = 1.0
    for i in range(1, n + 1):
        e += 1 / fatorial(i)
    return e

# Solicita ao usuário que insira um valor N inteiro e positivo
n = int(input("Digite um valor N inteiro e positivo: "))

# Verifica se o valor de N é positivo
if n < 0:
    print("N deve ser um valor inteiro positivo.")
else:
    resultado_e = calcular_e(n)
    print(f"O valor de E com N = {n} é aproximadamente {resultado_e:.4f}")
#questão 03
# Inicialize variáveis
soma_salario = 0
soma_filhos = 0
maior_salario = 0
pessoas_com_salario_ate_100 = 0
total_pessoas = 0

# Comece o loop de entrada de dados
while True:
    salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))
    
    # Verifique se o salário é negativo (condição de saída do loop)
    if salario < 0:
        break
    
    # Atualize as variáveis
    soma_salario += salario
    total_pessoas += 1
    numero_filhos = int(input("Digite o número de filhos: "))
    soma_filhos += numero_filhos
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 100:
        pessoas_com_salario_ate_100 += 1

# Verifique se pelo menos uma pessoa foi inserida
if total_pessoas > 0:
    media_salario = soma_salario / total_pessoas
    media_filhos = soma_filhos / total_pessoas
    percentual_salario_ate_100 = (pessoas_com_salario_ate_100 / total_pessoas) * 100

    print(f"Média do salário da população: R${media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário: R${maior_salario:.2f}")
    print(f"Percentual de pessoas com salário até R$100.00: {percentual_salario_ate_100:.2f}%")
else:
    print("Nenhum dado foi inserido.")

#questão 04
chico_altura = 1.50  # Altura inicial de Chico em metros
ze_altura = 1.10  # Altura inicial de Zé em metros
anos = 0  # Inicializa o contador de anos

while chico_altura > ze_altura:
    chico_altura += 0.02  # Chico cresce 2 centímetros por ano (0.02 metros)
    ze_altura += 0.03  # Zé cresce 3 centímetros por ano (0.03 metros)
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")
#questão 05
soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou um valor negativo para encerrar): "))
    
    if valor < 0:
        break  # Encerra o loop quando um valor negativo é inserido
    else:
        soma += valor
        contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos valores é: {media}")
else:
    print("Nenhum valor positivo foi inserido.")
#questão 06
# Inicialize as variáveis para contar os votos de cada candidato, votos nulos e votos em branco
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_em_branco = 0

# Comece o loop para a entrada de votos
while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar): "))
    
    if voto == 0:
        break  # Encerra o loop quando 0 é inserido
    elif voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    else:
        print("Código inválido. Por favor, insira um código válido.")

# Exiba os resultados
print(f"Total de votos para o Candidato 1: {votos_candidato1}")
print(f"Total de votos para o Candidato 2: {votos_candidato2}")
print(f"Total de votos para o Candidato 3: {votos_candidato3}")
print(f"Total de votos para o Candidato 4: {votos_candidato4}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")
#questão 07
soma_notas = 0
contador_alunos = 0

while True:
    codigo_aluno = int(input("Digite o código do aluno (ou 0 para encerrar): "))
    
    if codigo_aluno == 0:
        break  # Encerra o loop quando o código do aluno for 0
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: ")
    
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média do aluno de código {codigo_aluno}: {media:.2f}")
    
    soma_notas += media
    contador_alunos += 1

if contador_alunos > 0:
    media_turma = soma_notas / contador_alunos
    print(f"Média aritmética da turma: {media_turma:.2f}")
else:
    print("Nenhuma nota foi inserida.")
#questão 08
soma_pares = 0
contador_pares = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop quando o número for 0
    
    if numero % 2 == 0:
        soma_pares += numero
        contador_pares += 1

if contador_pares > 0:
    media_pares = soma_pares / contador_pares
    print(f"A média dos números pares é: {media_pares:.2f}")
else:
    print("Nenhum número par foi inserido.")
#questão 09
# Inicialize as variáveis para o maior e o menor valor
maior_valor = float('-inf')  # Inicialize como o menor valor possível
menor_valor = float('inf')   # Inicialize como o maior valor possível

# Faça um loop para ler os 50 valores
for i in range(1, 51):
    valor = float(input(f"Digite o {i}º valor: "))
    
    # Atualize o maior e o menor valor, se necessário
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

# Exiba o resultado
print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
#questão 10
while True:
    codigo_aluno = int(input("Digite o código do aluno (ou um valor negativo para encerrar): "))
    
    if codigo_aluno < 0:
        break  # Encerra o loop quando um código negativo é inserido
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    
    maior_nota = max(nota1, nota2, nota3)
    
    media_ponderada = (4 * maior_nota + 3 * (nota1 + nota2 + nota3 - maior_nota)) / 10
    
    print(f"Código do aluno: {codigo_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média ponderada: {media_ponderada:.2f}")
    
    if media_ponderada >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
#questão 11
n = int(input("Digite o número de termos da progressão aritmética (n): "))
a1 = float(input("Digite o primeiro termo (a1): "))
r = float(input("Digite a razão (r): "))

termos = []  # Lista para armazenar os termos da progressão
soma = 0

for i in range(n):
    termo = a1 + i * r  # Cálculo do i-ésimo termo
    termos.append(termo)  # Adicione o termo à lista
    soma += termo

print(f"Termos da progressão aritmética:")
for termo in termos:
    print(termo, end=" ")

print(f"\nSoma dos termos: {soma}")
#questão 12
for _ in range(20):
    n = int(input("Digite um valor para n: "))
    print(f"Tabuada de 1 até {n}:")

    for i in range(1, n + 1):
        resultado = i * n
        print(f"{i} x {n} = {resultado}")

    print()  # Linha em branco para separar as tabuadas
#questão 13
# Função para calcular o fatorial de um número
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        fat = 1
        for i in range(1, numero + 1):
            fat *= i
        return fat

n = int(input("Digite o número de valores a serem lidos: "))

for _ in range(n):
    valor = int(input("Digite um número: "))
    resultado_fatorial = fatorial(valor)
    print(f"Valor lido: {valor}, Fatorial: {resultado_fatorial}")
#questão 14
soma_valores = 0
qtd_valores = 0
qtd_positivos = 0
qtd_negativos = 0

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    
    if valor == 0:
        break  # Encerra o loop quando o valor for igual a zero
    
    soma_valores += valor
    qtd_valores += 1
    
    if valor > 0:
        qtd_positivos += 1
    elif valor < 0:
        qtd_negativos += 1

if qtd_valores > 0:
    media = soma_valores / qtd_valores
    percentual_positivos = (qtd_positivos / qtd_valores) * 100
    percentual_negativos = (qtd_negativos / qtd_valores) * 100
    
    print(f"Média aritmética dos valores: {media:.2f}")
    print(f"Quantidade de valores positivos: {qtd_positivos}")
    print(f"Quantidade de valores negativos: {qtd_negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
    print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
else:
    print("Nenhum valor foi inserido.")
#questão 15
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while True:
    numero = float(input("Digite um número (ou um número negativo para encerrar): "))
    
    if numero < 0:
        break  # Encerra o loop quando um número negativo é inserido
    
    if 0 <= numero < 25:
        intervalo_1 += 1
    elif 25 <= numero <= 50:
        intervalo_2 += 1
    elif 51 <= numero <= 75:
        intervalo_3 += 1
    elif 76 <= numero <= 100:
        intervalo_4 += 1

print(f"Quantidade de números no intervalo [0, 25]: {intervalo_1}")
print(f"Quantidade de números no intervalo [26, 50]: {intervalo_2}")
print(f"Quantidade de números no intervalo [51, 75]: {intervalo_3}")
print(f"Quantidade de números no intervalo [76, 100]: {intervalo_4}")
#questão 16
linha_atual = 0

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    
    if valor == 0:
        break  # Encerra o loop quando 0 é inserido
    
    if linha_atual % 20 == 0:
        print("Valor   Quadrado   Cubo   Raiz Quadrada")
    
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = valor ** 0.5
    
    print(f"{valor:.2f}   {quadrado:.2f}   {cubo:.2f}   {raiz_quadrada:.2f}")
    
    linha_atual += 1
#questão 17
while True:
    m = int(input("Digite o valor de m (ou um valor negativo para encerrar): "))
    if m < 0:
        break  # Encerra o loop quando um valor negativo é inserido
    
    n = int(input("Digite o valor de n: "))
    
    if n < 0:
        print("O valor de n deve ser positivo.")
        continue  # Volta para o início do loop se n for negativo
    
    soma = 0
    
    for i in range(n):
        soma += m + i
    
    print(f"A soma dos inteiros consecutivos a partir de {m} até {m + n - 1} é {soma}")
#questão 18
import math

while True:
    m = int(input("Digite um valor inteiro e positivo (ou um valor negativo para encerrar): "))
    
    if m < 0:
        break  # Encerra o loop quando um valor negativo é inserido
    
    if m % 2 == 0:
        # Verifica divisores se m for par
        divisores = [d for d in range(1, m + 1) if m % d == 0]
        print(f"O número {m} é par e possui {len(divisores)} divisores.")
    elif m % 2 != 0 and m < 10:
        # Calcula o fatorial se m for ímpar e menor que 10
        fatorial = math.factorial(m)
        print(f"O número {m} é ímpar e seu fatorial é {fatorial}.")
    elif m % 2 != 0 and m >= 10:
        # Calcula a soma dos inteiros de 1 até m se m for ímpar e maior ou igual a 10
        soma = sum(range(1, m + 1))
        print(f"O número {m} é ímpar e a soma dos inteiros de 1 até {m} é {soma}.")
#questão 19
qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop quando 0 é inserido
    
    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    
    soma_geral += numero

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
else:
    media_pares = 0

if qtd_pares > 0:
    media_geral = soma_geral / (qtd_pares + qtd_impares)
else:
    media_geral = 0

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
print(f"Média de valores pares: {media_pares:.2f}")
print(f"Média geral: {media_geral:.2f}")
#questão 20
somatorio_negativos = 0

while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop quando 0 é inserido
    
    if numero < 0:
        somatorio_negativos += numero

print(f"O somatório dos números negativos é: {somatorio_negativos}")
#questão 21
produtorio_pares = 1  # Inicialize o produtório como 1

while True:
    numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop quando 0 é inserido
    
    if numero > 0 and numero % 2 == 0:
        produtorio_pares *= numero

print(f"O produtório dos números pares é: {produtorio_pares}")
#questão 22
soma_salarios = 0
total_pessoas = 0
maior_idade = -1
menor_idade = float('inf')
qtd_mulheres_salario_ate_100 = 0

while True:
    idade = int(input("Digite a idade (ou um valor negativo para encerrar): "))
    
    if idade < 0:
        break  # Encerra o loop quando uma idade negativa é inserida
    
    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: "))
    
    soma_salarios += salario
    total_pessoas += 1
    
    if idade > maior_idade:
        maior_idade = idade
    
    if idade < menor_idade:
        menor_idade = idade
    
    if sexo == 'F' and salario <= 100:
        qtd_mulheres_salario_ate_100 += 1

if total_pessoas > 0:
    media_salario = soma_salarios / total_pessoas
else:
    media_salario = 0

print(f"Média de salário do grupo: R${media_salario:.2f}")
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Menor idade do grupo: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$100.00: {qtd_mulheres_salario_ate_100}")
#questão 23
# Inicialize as variáveis de contagem
qtd_homens = 0
qtd_mulheres = 0
qtd_olhos_azuis = 0
qtd_olhos_verdes = 0
qtd_olhos_castanhos = 0
qtd_cabelos_louros = 0
qtd_cabelos_castanhos = 0
qtd_cabelos_pretos = 0
soma_idades = 0

while True:
    # Coleta os dados de um habitante
    sexo = input("Sexo (M/F): ")
    olhos = input("Cor dos olhos (azuis/verdes/castanhos): ")
    cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ")
    idade = int(input("Idade: "))
    
    # Verifica se os dados são válidos
    if sexo not in ('M', 'F') or olhos not in ('azuis', 'verdes', 'castanhos') or cabelos not in ('louros', 'castanhos', 'pretos') or idade < 0:
        print("Dados inválidos. Tente novamente.")
        continue  # Volta para o início do loop
    
    # Atualiza as variáveis de contagem e soma das idades
    if sexo == 'M':
        qtd_homens += 1
    else:
        qtd_mulheres += 1
    
    if olhos == 'azuis':
        qtd_olhos_azuis += 1
    elif olhos == 'verdes':
        qtd_olhos_verdes += 1
    else:
        qtd_olhos_castanhos += 1
    
    if cabelos == 'louros':
        qtd_cabelos_louros += 1
    elif cabelos == 'castanhos':
        qtd_cabelos_castanhos += 1
    else:
        qtd_cabelos_pretos += 1
    
    soma_idades += idade

    continuar = input("Deseja coletar dados de outro habitante? (S/N): ")
    if continuar.upper() != 'S':
        break  # Encerra o loop se a resposta não for 'S'

# Calcula a média de idade
if qtd_homens + qtd_mulheres > 0:
    media_idade = soma_idades / (qtd_homens + qtd_mulheres)
else:
    media_idade = 0

# Exibe os resultados
print(f"Total de habitantes: {qtd_homens + qtd_mulheres}")
print(f"Total de homens: {qtd_homens}")
print(f"Total de mulheres: {qtd_mulheres}")
print(f"Total de olhos azuis: {qtd_olhos_azuis}")
print(f"Total de olhos verdes: {qtd_olhos_verdes}")
print(f"Total de olhos castanhos: {qtd_olhos_castanhos}")
print(f"Total de cabelos louros: {qtd_cabelos_louros}")
print(f"Total de cabelos castanhos: {qtd_cabelos_castanhos}")
print(f"Total de cabelos pretos: {qtd_cabelos_pretos}")
print(f"Média de idade: {media_idade:.2f} anos")
#questão 24
maior_idade = -1
qtd_mulheres = 0

while True:
    idade = int(input("Digite a idade do habitante (ou -1 para encerrar): "))
    
    if idade == -1:
        break  # Encerra o loop quando -1 é inserido
    
    sexo = input("Digite o sexo do habitante (M/F): ")
    olhos = input("Digite a cor dos olhos do habitante (azuis/verdes/castanhos): ")
    cabelos = input("Digite a cor dos cabelos do habitante (louros/castanhos/pretos): ")
    
    if idade > maior_idade:
        maior_idade = idade
    
    if sexo == 'F' and 18 <= idade <= 35 and olhos == 'verdes' and cabelos == 'louros':
        qtd_mulheres += 1

print(f"A maior idade entre os habitantes é: {maior_idade} anos")
print(f"Quantidade de mulheres com idade entre 18 e 35, olhos verdes e cabelos louros: {qtd_mulheres}")
#questão 25
soma_precos_com_aumento = 0
soma_precos_sem_aumento = 0
qtd_produtos = 0

while True:
    codigo = int(input("Digite o código do produto (ou um código negativo para encerrar): "))
    
    if codigo < 0:
        break  # Encerra o loop quando um código negativo é inserido
    
    preco_custo = float(input("Digite o preço de custo do produto: "))
    
    preco_novo = preco_custo * 1.2  # Aumento de 20%
    
    soma_precos_com_aumento += preco_novo
    soma_precos_sem_aumento += preco_custo
    qtd_produtos += 1
    
    print(f"Código do produto: {codigo}, Novo preço: R${preco_novo:.2f}")
    
if qtd_produtos > 0:
    media_precos_com_aumento = soma_precos_com_aumento / qtd_produtos
    media_precos_sem_aumento = soma_precos_sem_aumento / qtd_produtos
else:
    media_precos_com_aumento = 0
    media_precos_sem_aumento = 0

print(f"Média dos preços com aumento: R${media_precos_com_aumento:.2f}")
print(f"Média dos preços sem aumento: R${media_precos_sem_aumento:.2f}")
#questão 26
for numero in range(1000, 2000):
    if numero % 11 == 5:
        print(numero)
#questão 27
maior_valor = float('-inf')
menor_valor = float('inf')
soma_valores = 0

for i in range(500):
    valor = int(input(f"Digite o {i+1}º valor inteiro e positivo: "))
    
    if valor < 0:
        print("O valor deve ser positivo. Tente novamente.")
        continue  # Continue o loop sem atualizar i
    
    if valor > maior_valor:
        maior_valor = valor
    
    if valor < menor_valor:
        menor_valor = valor
    
    soma_valores += valor

media_valores = soma_valores / 500

print(f"O maior valor lido é: {maior_valor}")
print(f"O menor valor lido é: {menor_valor}")
print(f"A média dos valores lidos é: {media_valores:.2f}")
#questão 28
n = int(input("Digite um valor inteiro e positivo (n): "))

if n <= 0:
    print("O valor de n deve ser um número inteiro e positivo.")
else:
    S = 0  # Inicialize a variável S
    termo = 0

    for i in range(1, n + 1):
        termo = 1 / i  # Calcule o termo atual
        S += termo  # Adicione o termo à soma
        print(f"Termo {i}: {termo:.4f}")

    print(f"O valor final de S é: {S:.4f}")
#questão 29
soma = 0  # Inicialize a variável para a soma dos números
contador = 0  # Inicialize o contador de números

for numero in range(14, 73):  # Comece a partir de 14 para incluir 13 e vá até 72
    soma += numero
    contador += 1

media = soma / contador

print(f"A média aritmética dos números entre 13 e 73 é: {media:.2f}")
#questão 30
for numero in range(101, 200, 2):
    print(numero)
#questão 31
dentro_intervalo = 0
fora_intervalo = 0

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    
    if valor >= 10 and valor <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Quantidade de valores dentro do intervalo [10, 20]: {dentro_intervalo}")
print(f"Quantidade de valores fora do intervalo [10, 20]: {fora_intervalo}")
#questão 32
for _ in range(5):
    a = int(input("Digite o valor de 'a' (inteiro positivo): "))
    b = int(input(f"Digite o valor de 'b' maior que 'a' (inteiro positivo): "))

    if a < b and a % 2 == 0:
        print(f"Inteiros pares entre {a} e {b} (inclusive):")
        for numero in range(a, b + 1):
            if numero % 2 == 0:
                print(numero)
    else:
        print("Valores não atendem aos critérios.")

    print()  # Adiciona uma linha em branco para separar os pares de valores
#questão 33
#a
n = int(input("Digite o valor de N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
#b
aluno_mais_alto = None
altura_mais_alta = 0
aluno_mais_baixo = None
altura_mais_baixa = float('inf')

for i in range(5):
    numero_aluno = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno (em cm): "))

    if altura > altura_mais_alta:
        aluno_mais_alto = numero_aluno
        altura_mais_alta = altura

    if altura < altura_mais_baixa:
        aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura

print(f"Aluno mais alto: Número {aluno_mais_alto}, Altura: {altura_mais_alta} cm")
print(f"Aluno mais baixo: Número {aluno_mais_baixo}, Altura: {altura_mais_baixa} cm")
#c
maior_altura = 0
menor_altura = float('inf')
soma_altura_mulheres = 0
total_altura_turma = 0
total_mulheres = 0

for i in range(50):
    altura = float(input("Digite a altura da pessoa (em cm): "))
    sexo = int(input("Digite o código do sexo (1 - masculino, 2 - feminino): "))

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

    total_altura_turma += altura

    if sexo == 2:
        soma_altura_mulheres += altura
        total_mulheres += 1

media_altura_mulheres = soma_altura_mulheres / total_mulheres
media_altura_turma = total_altura_turma / 50

print(f"Maior altura da turma: {maior_altura} cm")
print(f"Menor altura da turma: {menor_altura} cm")
print(f"Média de altura das mulheres: {media_altura_mulheres} cm")
print(f"Média de altura da turma: {media_altura_turma} cm")
#questão 36
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

n = int(input("Digite o valor de N: "))

for i in range(n):
    valor = int(input(f"Digite o {i+1}º valor: "))
    fatorial = calcular_fatorial(valor)
    print(f"Valor: {valor}, Fatorial: {fatorial}")
#questão 37
x = int(input("Digite o valor de X: "))

for i in range(1, 21):
    resultado = x ** i
    print(f"Termo {i}: {resultado}")
#questão 38
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

produto_primos = 1

for num in range(92, 1479):
    if is_prime(num):
        produto_primos *= num

print(f"O produto dos números primos entre 92 e 1478 é: {produto_primos}")
#questão 39
def is_perfect_number(num):
    divisors = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return num == sum(divisors)

contagem = 0
numero = 2

while contagem < 5:
    if is_perfect_number(numero):
        print(f"Número perfeito {contagem + 1}: {numero}")
        contagem += 1
    numero += 1
#questão 40
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

n = int(input("Digite o valor de N: ")

for i in range(n):
    m = int(input(f"Digite o {i+1}º valor inteiro e positivo (M): "))
    
    if m <= 0:
        print("O valor de M deve ser inteiro e positivo. Tente novamente.")
        continue
    
    soma = sum(range(1, m + 1))
    fatorial_m = calcular_fatorial(m)
    
    print(f"Valor lido: {m}, Somatório de 1 até M: {soma}, Fatorial de M: {fatorial_m}")
#questão 41
# Inicialize uma lista para armazenar as médias ponderadas
medias_ponderadas = []

# Loop para ler as notas de 50 alunos
for i in range(50):
    n1 = float(input(f"Digite a primeira nota do aluno {i + 1}: "))
    n2 = float(input(f"Digite a segunda nota do aluno {i + 1}: "))
    n3 = float(input(f"Digite a terceira nota do aluno {i + 1}: "))

    # Calcule a média ponderada para o aluno atual
    media_ponderada = (n1 * 2 + n2 * 4 + n3 * 3) / 10
    medias_ponderadas.append(media_ponderada)

# Exiba as médias ponderadas de todos os alunos
for i, media in enumerate(medias_ponderadas):
    print(f"Média ponderada do aluno {i + 1}: {media:.2f}")
#questão 42
n = int(input("Digite o valor de n (inteiro e positivo): "))
if n <= 0:
    print("O valor de n deve ser inteiro e positivo.")
else:
    h = 10 * n
    print(f"O resultado de H = 10 + 10 + 10 + ... + 10 para n = {n} é: {h}")
#questão 43
# Inicialize uma lista para armazenar os grupos
grupos = []

# Loop para ler os grupos
for i in range(5):
    grupo = []
    for j in range(4):
        valor = int(input(f"Digite o valor {j+1} do grupo {i+1}: "))
        grupo.append(valor)
    grupos.append(grupo)

# Exiba os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Ordene os grupos em ordem decrescente
grupos_ordenados = sorted(grupos, key=lambda x: sum(x), reverse=True)

# Exiba os grupos ordenados em ordem decrescente
print("Grupos ordenados em ordem decrescente:")
for grupo in grupos_ordenados:
    print(grupo)
#questão 44
# Inicialize as variáveis para o maior e menor índice de acidentes
maior_indice = 0
menor_indice = float('inf')
cidade_maior_indice = ''
cidade_menor_indice = ''

# Inicialize as variáveis para a soma de veículos e acidentes no RS
soma_veiculos_rs = 0
soma_acidentes_rs = 0
cidades_rs = 0

# Inicialize a lista para armazenar as cidades e seus índices de acidentes
cidades = []

# Loop para coletar dados das cidades
for _ in range(200):
    codigo_cidade = input("Digite o código da cidade: ")
    estado = input("Digite o estado da cidade (RS, SC, PR, SP, RJ, ...): ")
    veiculos_passeio = int(input("Digite o número de veículos de passeio (em 1992): "))
    acidentes_vitimas = int(input("Digite o número de acidentes de trânsito com vítimas (em 1992): "))

    # Calcula o índice de acidentes e verifica maior e menor índice
    indice_acidentes = acidentes_vitimas / veiculos_passeio
    if indice_acidentes > maior_indice:
        maior_indice = indice_acidentes
        cidade_maior_indice = f"{codigo_cidade}, {estado}"
    if indice_acidentes < menor_indice:
        menor_indice = indice_acidentes
        cidade_menor_indice = f"{codigo_cidade}, {estado}"
    
    # Adiciona os dados da cidade à lista
    cidades.append({
        "codigo": codigo_cidade,
        "estado": estado,
        "veiculos": veiculos_passeio,
        "acidentes": acidentes_vitimas
    })

    # Verifica se a cidade pertence ao estado do RS
    if estado == "RS":
        soma_veiculos_rs += veiculos_passeio
        soma_acidentes_rs += acidentes_vitimas
        cidades_rs += 1

# Calcula a média de veículos e acidentes no RS
media_veiculos_rs = soma_veiculos_rs / cidades_rs
media_acidentes_rs = soma_acidentes_rs / cidades_rs

# Exibe os resultados
print(f"Maior índice de acidentes: {maior_indice:.2f}, Cidade: {cidade_maior_indice}")
print(f"Menor índice de acidentes: {menor_indice:.2f}, Cidade: {cidade_menor_indice}")
print(f"Média de veículos nas cidades brasileiras: {media_veiculos_rs:.2f}")
print(f"Média de acidentes com vítimas no Rio Grande do Sul: {media_acidentes_rs:.2f}")
#questão 45
# Inicialize as variáveis para as estatísticas
soma_idade = 0
soma_altura_mulheres = 0
soma_idade_homens = 0
contador_habitantes = 0
contador_idade_18_35 = 0

# Repetição para coletar informações
while contador_habitantes < 1000:
    sexo = int(input("Digite o sexo (0-feminino, 1-masculino): ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    
    soma_idade += idade
    
    if sexo == 0:
        soma_altura_mulheres += altura
    else:
        soma_idade_homens += idade

    if 18 <= idade <= 35:
        contador_idade_18_35 += 1
    
    contador_habitantes += 1

# Calcular as médias
media_idade = soma_idade / 1000
media_altura_mulheres = soma_altura_mulheres / 1000
media_idade_homens = soma_idade_homens / (1000 - soma_idade_homens)
percentual_idade_18_35 = (contador_idade_18_35 / 1000) * 100

# Exibir as estatísticas
print(f"Média da idade do grupo: {media_idade:.2f} anos")
print(f"Média da altura das mulheres: {media_altura_mulheres:.2f} metros")
print(f"Média da idade dos homens: {media_idade_homens:.2f} anos")
print(f"Percentual de pessoas com idade entre 18 e 35 anos: {percentual_idade_18_35:.2f}%")
#questão 46
# Inicialize as variáveis para as estatísticas
maior_idade = 0
quantidade_mulheres_verdes_louros = 0

# Repetição para coletar informações de 500 pessoas
for _ in range(500):
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")
    cor_olhos = input("Digite a cor dos olhos (A para azuis, V para verdes, C para castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (L para louros, C para castanhos, P para pretos): ")
    idade = int(input("Digite a idade: "))

    # Verifica a maior idade
    if idade > maior_idade:
        maior_idade = idade

    # Verifica se a pessoa é do sexo feminino, com olhos verdes, cabelos louros e idade entre 18 e 35 anos
    if sexo == "F" and cor_olhos == "V" and cor_cabelos == "L" and 18 <= idade <= 35:
        quantidade_mulheres_verdes_louros += 1

# Exibe as estatísticas
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Quantidade de mulheres com olhos verdes, cabelos louros e idade entre 18 e 35 anos: {quantidade_mulheres_verdes_louros}")
#questão 47
# Inicialize uma lista para armazenar os nomes dos clientes e o valor de suas compras
clientes = []

# Loop para coletar os dados dos 150 clientes
for _ in range(150):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras no ano passado: "))

    # Calcula o bônus com base no valor das compras
    if compras < 500000:
        bonus = 0.10 * compras
    else:
        bonus = 0.15 * compras

    # Armazena o nome do cliente e o valor do bônus na lista
    clientes.append((nome, bonus))

# Exibe o valor do bônus de cada cliente
for nome, bonus in clientes:
    print(f"Cliente: {nome}, Bônus: R${bonus:.2f}")
#questão 48
# Inicialize uma lista para armazenar os conceitos finais dos alunos
conceitos_finais = []

# Loop para coletar dados dos 75 alunos
for _ in range(75):
    matricula = input("Digite o número de matrícula do aluno: ")
    nota_final = float(input("Digite a nota numérica final do aluno: "))

    # Determina o conceito com base na nota
    if 0 <= nota_final <= 4.9:
        conceito = "D"
    elif 5.0 <= nota_final <= 6.9:
        conceito = "C"
    elif 7.0 <= nota_final <= 8.9:
        conceito = "B"
    elif 9.0 <= nota_final <= 10.0:
        conceito = "A"
    else:
        conceito = "Nota inválida"

    # Armazena o número de matrícula e o conceito final na lista
    conceitos_finais.append((matricula, conceito))

# Exibe os conceitos finais de cada aluno
for matricula, conceito in conceitos_finais:
    print(f"Aluno de matrícula {matricula}: Conceito final {conceito}")
#questão 49
# Função para calcular o fatorial de um número
def calcular_fatorial(N):
    if N == 0:
        return 1
    else:
        return N * calcular_fatorial(N - 1)

# Solicita ao usuário que insira um valor inteiro e positivo
N = int(input("Digite um valor inteiro e positivo para calcular o fatorial: "))

# Verifica se o valor é positivo
if N < 0:
    print("O valor deve ser positivo.")
else:
    # Chama a função para calcular o fatorial
    resultado = calcular_fatorial(N)
    print(f"{N}! = {resultado}")
#questão 50
# Solicita ao usuário que insira dois valores inteiros positivos, X e Y
X = int(input("Digite o valor de X (inteiro positivo): "))
Y = int(input("Digite o valor de Y (inteiro positivo): "))

# Verifica se os valores são positivos
if X < 0 or Y < 0:
    print("Ambos os valores devem ser inteiros positivos.")
else:
    # Calcula a potência X^Y e exibe o resultado
    resultado = X ** Y
    print(f"{X} elevado a {Y} é igual a {resultado}")
#questão 51
# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Solicita ao usuário que insira um número inteiro não negativo
n = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número é não negativo
if n < 0:
    print("O número deve ser não negativo.")
else:
    # Chama a função para calcular o fatorial e exibe o resultado
    resultado = calcular_fatorial(n)
    print(f"{n}! = {resultado}")
#questão 52
# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Função para calcular combinações (C(n, p))
def calcular_combinacao(n, p):
    if 0 <= p <= n:
        combinacao = calcular_fatorial(n) / (calcular_fatorial(p) * calcular_fatorial(n - p))
        return int(combinacao)
    else:
        return 0

# Função para calcular arranjos (A(n, p))
def calcular_arranjo(n, p):
    if 0 <= p <= n:
        arranjo = calcular_fatorial(n) / calcular_fatorial(n - p)
        return int(arranjo)
    else:
        return 0

# Solicita ao usuário que insira os valores de N e p
N = int(input("Digite o valor de N (tamanho do conjunto): "))
p = int(input("Digite o valor de p (tamanho dos subconjuntos): "))

# Calcula e exibe as combinações e arranjos
combinacoes = calcular_combinacao(N, p)
arranjos = calcular_arranjo(N, p)

print(f"Combinações (C({N}, {p})) = {combinacoes}")
print(f"Arranjos (A({N}, {p})) = {arranjos}")
#questão 53
# Função para verificar se um número é primo
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Inicialize uma lista para armazenar os números primos
primos = [1, 2, 3]

# Inicialize um contador para acompanhar quantos números primos foram encontrados
contador = 3

# Enquanto não encontrarmos os 20 primeiros números primos
while contador < 20:
    # Tenta encontrar o próximo número primo
    numero = primos[-1] + 2  # Comece com o próximo número ímpar
    while not is_prime(numero):
        numero += 2  # Verifique apenas números ímpares
    primos.append(numero)
    contador += 1

# Exibe os 20 primeiros números primos
print("Os 20 primeiros números primos são:")
print(primos)
#questão 54
# Solicita ao usuário que insira os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais
if num1 == num2:
    print("Os números de entrada são iguais. Por favor, insira números diferentes.")
else:
    # Ordena os números em ordem crescente
    menor_numero = min(num1, num2)
    maior_numero = max(num1, num2)

    # Calcula os três pontos de divisão
    divisao1 = menor_numero + (maior_numero - menor_numero) / 3
    divisao2 = menor_numero + 2 * (maior_numero - menor_numero) / 3

    # Exibe os três pontos de divisão
    print(f"Os pontos de divisão são: {menor_numero:.2f}, {divisao1:.2f}, {divisao2:.2f}, {maior_numero:.2f}")
#questão 55
from datetime import datetime

# Solicita ao usuário que insira as duas datas no formato "dd/mm/aaaa"
data1 = input("Digite a primeira data (dd/mm/aaaa): ")
data2 = input("Digite a segunda data (dd/mm/aaaa): ")

# Converte as datas para objetos datetime
data1_obj = datetime.strptime(data1, '%d/%m/%Y')
data2_obj = datetime.strptime(data2, '%d/%m/%Y')

# Calcula a diferença entre as datas em dias
diferenca = abs((data2_obj - data1_obj).days)

# Exibe a diferença em dias
print(f"A diferença entre as datas é de {diferenca} dias.")
