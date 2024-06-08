# Solicitar ao usuario para digitar dois números
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

#Operações Aritmeticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisaoInteira = num1 / num2 
modulo = num1 % num2
potencia = num1 ** num2

# Exibir os resultados
print('\nO resultado das operaçoes aritmeticas é: ')
print('Soma', soma)
print('subtracao', subtracao)
print('multiplicacao', multiplicacao)
print('divisao', divisaoInteira)
print('modulo', modulo)
print('potencia', potencia)

# Comparações com operadores
print('\nResultado das operações de comparação: ')
print('igualdade', num1 == num2)
print('diferenca', num1 != num2)
print('maior', num1 > num2)
print('Maior ou Igual', num1 >= num2)
print('Menor', num1 < num2)
print('Menor ou igual', num1 <= num2)

#Operadores de atribuição
print('\n Resultados dos Operadores de atribuição: ')
num1 += 5
print('num1 += 5: ', num1)
num2 /= 2
print('num2 /= 2: ', num2)

#Verificar presença na lista de elementos 
listaNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in listaNumbers:
    print(f'O numero {num1} esta na lista de números')
else: 
    print(f'O numero {num1} não esta na lista de números')

#Compare a identidade de objetos 
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print('\n Resultados das operações de identidade de objetos: ')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)

