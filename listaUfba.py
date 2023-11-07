#1° questão:
# Inicialize uma lista vazia para armazenar os números
numeros = []

# Peça ao usuário para inserir 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

# Imprima a lista na mesma linha
print("Lista de números:", numeros)

#2° questão:
# Inicialize uma lista vazia para armazenar os números
numeros = []

# Peça ao usuário para inserir 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

# Peça ao usuário para inserir um número a ser verificado na lista
numero_verificar = int(input("Digite um número para verificar se está na lista: "))

# Verifique se o número está na lista
if numero_verificar in numeros:
    print(f"O número {numero_verificar} está na lista.")
else:
    print(f"O número {numero_verificar} não está na lista.")

#3°questão:
# Inicialize listas vazias para armazenar os números
numeros = []
positivos = []
negativos = []

# Ler 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    numeros.append(numero)

# Calcular a média dos elementos
media = sum(numeros) / len(numeros)

# Encontrar o maior e o menor elemento
maior_elemento = max(numeros)
menor_elemento = min(numeros)

# Contar a quantidade de elementos positivos e negativos
for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)

# Exibir os resultados
print(f"Média dos elementos: {media}")
print(f"Maior elemento: {maior_elemento}")
print(f"Menor elemento: {menor_elemento}")
print(f"Quantidade de elementos positivos: {len(positivos)}")
print(f"Quantidade de elementos negativos: {len(negativos)}")

#4° Questão:

# Inicialize listas vazias para armazenar os nomes, idades e indenizações reajustadas
nomes = []
idades = []
indenizacoes = []

# Função para calcular o reajuste de indenização com base na idade
def calcular_reajuste(idade, valor_base):
    if idade <= 12:
        return valor_base * 1.30
    elif 13 <= idade <= 49:
        return valor_base * 1.10
    elif 50 <= idade <= 65:
        return valor_base * 1.15
    else:
        return valor_base * 1.35

# Solicitar informações dos pacientes ao usuário
while True:
    nome = input("Digite o nome do paciente (ou 'fim' para encerrar): ")
    
    if nome.lower() == 'fim':
        break
    
    idade = int(input("Digite a idade do paciente: "))
    valor_base = float(input("Digite o valor base de indenização: "))
    
    reajuste = calcular_reajuste(idade, valor_base)
    
    nomes.append(nome)
    idades.append(idade)
    indenizacoes.append(reajuste)

# Exibir os resultados
print("\nResultados:")
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Indenização Reajustada: R$ {indenizacoes[i]:.2f}")

#5° questão:a):

# Função para calcular a norma de um vetor
def calcular_norma(vetor):
    norma = 0
    for elemento in vetor:
        norma += elemento ** 2
    return norma ** 0.5

# Função para calcular o vetor soma de três vetores
def calcular_vetor_soma(vetor1, vetor2, vetor3):
    vetor_soma = []
    for i in range(len(vetor1)):
        soma = vetor1[i] + vetor2[i] + vetor3[i]
        vetor_soma.append(soma)
    return vetor_soma

# Pedir ao usuário o tamanho dos vetores
N = int(input("Digite o tamanho dos vetores: "))

# Inicializar os vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Pedir ao usuário os elementos dos três vetores
print("Digite os elementos do primeiro vetor:")
vetor1 = [float(input()) for _ in range(N)]

print("Digite os elementos do segundo vetor:")
vetor2 = [float(input()) for _ in range(N)]

print("Digite os elementos do terceiro vetor:")
vetor3 = [float(input()) for _ in range(N)]

# Calcular as normas dos vetores
norma_vetor1 = calcular_norma(vetor1)
norma_vetor2 = calcular_norma(vetor2)
norma_vetor3 = calcular_norma(vetor3)

# Informar qual vetor tem a maior norma
vetores_normas = [(norma_vetor1, "Vetor 1"), (norma_vetor2, "Vetor 2"), (norma_vetor3, "Vetor 3")]
vetor_maior_norma = max(vetores_normas, key=lambda x: x[0])
print(f"O vetor com maior norma é {vetor_maior_norma[1]} com norma {vetor_maior_norma[0]}.")

# Calcular o vetor soma
vetor_soma = calcular_vetor_soma(vetor1, vetor2, vetor3)
print(f"O vetor soma dos três vetores é: {vetor_soma}")

#b):

import math

# Função para calcular a norma de um vetor
def calcular_norma(vetor):
    soma_quadrados = sum(x ** 2 for x in vetor)
    norma = math.sqrt(soma_quadrados)
    return norma

# Função para calcular o vetor soma dos três vetores
def calcular_vetor_soma(vetor1, vetor2, vetor3):
    vetor_soma = [x + y + z for x, y, z in zip(vetor1, vetor2, vetor3)]
    return vetor_soma

# Tamanho dos vetores (N)
N = int(input("Digite o tamanho dos vetores: "))

# Inicialize os três vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Ler os elementos dos três vetores
print("Digite os elementos do vetor 1:")
for i in range(N):
    elemento = float(input(f"Elemento {i + 1}: "))
    vetor1.append(elemento)

print("Digite os elementos do vetor 2:")
for i in range(N):
    elemento = float(input(f"Elemento {i + 1}: "))
    vetor2.append(elemento)

print("Digite os elementos do vetor 3:")
for i in range(N):
    elemento = float(input(f"Elemento {i + 1}: "))
    vetor3.append(elemento)

# Calcular a norma de cada vetor
norma_vetor1 = calcular_norma(vetor1)
norma_vetor2 = calcular_norma(vetor2)
norma_vetor3 = calcular_norma(vetor3)

# Encontrar o vetor com a maior norma
maior_norma = max(norma_vetor1, norma_vetor2, norma_vetor3)

# Calcular o vetor soma
vetor_soma = calcular_vetor_soma(vetor1, vetor2, vetor3)

# Exibir os resultados
print("\nNormas dos vetores:")
print(f"Norma do vetor 1: {norma_vetor1:.2f}")
print(f"Norma do vetor 2: {norma_vetor2:.2f}")
print(f"Norma do vetor 3: {norma_vetor3:.2f}")

print("\nO vetor com a maior norma é o:")
if maior_norma == norma_vetor1:
    print("Vetor 1")
elif maior_norma == norma_vetor2:
    print("Vetor 2")
else:
    print("Vetor 3")

print("\nVetor Soma dos três vetores:")
print(vetor_soma)

#6° questão:

# Inicialize uma lista para armazenar os dados dos clientes
clientes = []

while True:
    nome = input("Digite o nome completo do cliente (ou 'fim' para encerrar): ")
    
    if nome.lower() == 'fim':
        break
    
    rg = input("Digite o RG do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = [nome, rg, cpf, telefone]
    clientes.append(cliente)

# Exibir os resultados
print("\nCadastro de Clientes:")
for cliente in clientes:
    print(f"Nome: {cliente[0]}")
    print(f"RG: {cliente[1]}")
    print(f"CPF: {cliente[2]}")
    print(f"Telefone: {cliente[3]}")
    print()

#7° questão:

# Inicialize uma lista vazia para armazenar os elementos
elementos = []

# Ler 10 elementos inteiros
for i in range(10):
    elemento = int(input(f"Digite o {i + 1}º elemento inteiro: "))
    elementos.append(elemento)

# Contar quantos valores pares existem na lista
valores_pares = 0
for elemento in elementos:
    if elemento % 2 == 0:
        valores_pares += 1

# Exibir a quantidade de valores pares na lista
print(f"A quantidade de valores pares na lista é: {valores_pares}")

#8°questão:

# Inicialize duas listas vazias para armazenar números pares e ímpares
pares = []
impares = []

# Função para exibir as listas e redefini-las
def exibir_e_redefinir_listas():
    if len(pares) > 0:
        print("Números pares:", pares)
        pares.clear()
    if len(impares) > 0:
        print("Números ímpares:", impares)
        impares.clear()

while True:
    valor = int(input("Digite um valor inteiro (ou 0 para encerrar): ")

    if valor == 0:
        break

    if valor % 2 == 0:
        pares.append(valor)
        if len(pares) == 5:
            exibir_e_redefinir_listas()
    else:
        impares.append(valor)
        if len(impares) == 5:
            exibir_e_redefinir_listas()

# Exibir as listas restantes
exibir_e_redefinir_listas()

#9° questão:

# Leitura do gabarito (lista de 20 caracteres)
gabarito = list(input("Digite o gabarito da prova com 20 questões: "))

# Função para calcular a pontuação do aluno
def calcular_pontuacao(aluno, gabarito):
    pontuacao = 0
    for i in range(20):
        if aluno[i] == gabarito[i]:
            pontuacao += 0.5
    return pontuacao

# Inicialize uma lista para armazenar os resultados dos alunos
resultados = []

# Processamento dos alunos
for aluno_num in range(50):
    nome = input(f"Digite o nome do aluno {aluno_num + 1}: ")
    respostas = list(input(f"Digite as respostas do aluno {aluno_num + 1} (20 caracteres): "))
    
    pontuacao = calcular_pontuacao(respostas, gabarito)
    
    if pontuacao >= 6:
        status = "APROVADO"
    else:
        status = "REPROVADO"
    
    resultados.append((nome, pontuacao, status))

# Exibir os resultados
for nome, pontuacao, status in resultados:
    print(f"Aluno: {nome}, Pontuação: {pontuacao:.1f}, Status: {status}")

#10° questão:

# Leitura do gabarito (lista de 20 caracteres)
gabarito = list(input("Digite o gabarito da prova com 20 questões: "))

# Função para calcular a pontuação do aluno
def calcular_pontuacao(aluno, gabarito):
    pontuacao = 0
    for i in range(20):
        if aluno[i] == gabarito[i]:
            pontuacao += 0.5
    return pontuacao

# Inicialize uma lista para armazenar os resultados dos alunos
resultados = []

# Processamento dos alunos
for aluno_num in range(50):
    nome = input(f"Digite o nome do aluno {aluno_num + 1}: ")
    respostas = list(input(f"Digite as respostas do aluno {aluno_num + 1} (20 caracteres): "))
    
    pontuacao = calcular_pontuacao(respostas, gabarito)
    
    resultados.append((nome, pontuacao))

# Exibir os resultados e determinar se o aluno foi aprovado ou reprovado
print("Resultados:")
for nome, pontuacao in resultados:
    nota_final = pontuacao
    if nota_final >= 6:
        status = "APROVADO"
    else:
        status = "REPROVADO"
    print(f"Aluno: {nome}, Nota Final: {nota_final:.1f}, Status: {status}")

#11° questão:

# Inicialize uma lista de 15 posições para armazenar números reais
numeros = []

# Preencha a lista de números reais
for i in range(15):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    numeros.append(numero)

while True:
    codigo = int(input("Digite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))

    if codigo == 0:
        break
    elif codigo == 1:
        print("Lista na ordem direta:")
        for numero in numeros:
            print(numero)
    elif codigo == 2:
        print("Lista na ordem inversa:")
        for numero in reversed(numeros):
            print(numero)
    else:
        print("Código inválido. Use 0, 1 ou 2 para as opções.")

# O programa encerra quando o código for 0
#12° questão :

# Ler os valores de a e b
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Ler o tamanho da lista N
N = int(input("Digite o tamanho da lista: "))

# Inicialize uma lista para armazenar os elementos
lista = []

# Preencher a lista com N elementos
for i in range(N):
    elemento = int(input(f"Digite o {i + 1}º elemento da lista: "))
    lista.append(elemento)

# Inicializar uma variável para contar os elementos no intervalo
contagem = 0

# Verificar quantos elementos da lista estão no intervalo [a, b]
for elemento in lista:
    if a <= elemento <= b:
        contagem += 1

# Exibir a contagem
print(f"A contagem de elementos no intervalo [{a}, {b}] é: {contagem}")
#Final da lista.

