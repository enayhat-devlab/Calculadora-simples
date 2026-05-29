#Fazendo uma calculadora simples que armazena varios numeros 

numeros = [] #criando uma lista vazia

while True:
    num = input('Digite um numero (0 para sair): ')

    if num == '0':
        break

    numeros.append(float(num)) #armazena na lista os núm. digitados


operador = input('Escolha o operador (+)(-)(*)(/): ')

#pega o primeiro núm. da lista como resultado inicial
resultado = numeros[0]


#percorre todos os núm. da lista 
for n in numeros[1:]:

    if operador == '+':
        resultado += n
    elif operador == '-':
        resultado -= n
    elif operador == '*':
        resultado *= n
    elif operador == '/':
        resultado /= n

print(f'Resultado: {resultado}')

