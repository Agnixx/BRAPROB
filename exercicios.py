#Exercício 1:Crie três variáveis que armazenem o nome de um aluno, a idade dele e a nota final de um curso. Exiba essas informações na tela.
#Resolução:

nome_aluno = "Agnes Souza"
idade_aluno = 23
nota_final = 9.5

print(f"Aluno: {nome_aluno}")
print(f"Idade: {idade_aluno} anos")
print(f"Nota Final: {nota_final}")

#Exercício 2: Crie uma variável que armazene um número inteiro, uma variável que armazene um número decimal e uma variável que armazene uma string. Exiba o tipo de cada variável usando a função `type()`.
#Resolução:

numero_inteiro = 10
numero_decimal = 3.14
texto = "Hey, Jessie"

print(f"Tipo de numero_inteiro: {type(numero_inteiro)}")
print(f"Tipo de numero_decimal: {type(numero_decimal)}")
print(f"Tipo de texto: {type(texto)}")

#Exercício 3: Crie uma variável que armazene um número inteiro e exiba sua parte inteira e resto na divisão por 2.
#Resolução:

numero = 20

parte_inteira = numero // 2
resto = numero % 2

print(f"Parte inteira da divisão por 2: {parte_inteira}")
print(f"Resto da divisão por 2: {resto}")

#Exercício 4: Atribua a uma variável o valor 10. Em seguida, altere o valor dessa variável para 20 e imprima o novo valor.
#Resolução:

numero = 10

numero = 20

print(f"Novo valor da variável: {numero}")

#Exercício 5: Crie duas variáveis, `a` e `b`, e atribua a elas os valores 5 e 10, respectivamente. Troque os valores das variáveis utilizando uma técnica de atribuição em Python e imprima os valores trocados.
#Resolução:

a = 5
b = 10

a, b = b, a

print(f"Valor de a: {a}")
print(f"Valor de b: {b}")

#Exercício 6: Peça ao usuário para digitar dois números inteiros. Realize as operações de soma, subtração, multiplicação e divisão e exiba os resultados.
#Resolução:

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}") 


#Exercício 7: Crie duas variáveis, `x` e `y`, e faça uma verificação condicional que compare essas variáveis usando os operadores relacionais. Exiba se `x` é maior, menor ou igual a `y`.
#Resolução:

x = 10
y = 20

if x > y:
    print("x é maior que y")
elif x < y:
    print("x é menor que y")
else:
    print("x é igual a y")


#Exercício 8: Crie uma variável booleana `is_admin` e uma variável `age` para armazenar se o usuário é administrador e sua idade, respectivamente. Usando operadores lógicos, verifique se o usuário é administrador E tem mais de 18 anos.
#Resolução:

is_admin = True
age = 25

if is_admin and age > 18:
    print("Acesso permitido: Usuário é administrador e maior de 18 anos.")
else:
    print("Acesso negado.")

#Exercício 9: Implemente um programa que leia a idade de uma pessoa e imprima se ela é maior de idade ou menor de idade. Use operadores lógicos para fazer a verificação.
#Resolução:

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


#Exercício 10: Utilize um operador lógico para verificar se o número digitado pelo usuário está entre 10 e 20 (inclusive) e imprima a mensagem apropriada.
#Resolução:

num = int(input("Digite um número: "))

if 10 <= num <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número está fora do intervalo de 10 a 20.")
