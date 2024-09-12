#Faça um programa para realizar as operações matemática de soma, subtração, multiplicação, divisão, resto da divisão e exponencial e ao final mostre os resultados

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando as operações matemática
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
resto_divisao = numero1 % numero2
exponencial = numero1 ** numero2

# Exibindo os resultados
print(f"\nResultados das operações entre {numero1} e {numero2}:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da Divisão: {resto_divisao}")
print(f"Exponencial: {exponencial}")
