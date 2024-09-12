#Entrada de Dados: Descrição: O programa solicita que o usuário insira um nome e número. Melhore o programa para realizar as seguintes tarefas:
#Verificar se o numero digitado é par ou ímpar. #Validar se nome contém mais de 3 caracteres. Se não, peça para o usuário digitar novamente

# Solicitar que o usuário insira um nome
while True:
    nome = input("Digite seu nome (O nome deve conter mais de 3 caracteres): ")
    if len(nome) > 3:
        break
    print("Nome muito curto. Por favor, insira um nome com mais de 3 caracteres.")

# Solicitar que o usuário insira um número
numero = int(input("Digite um número: "))

# Verificar se o número digitado é par ou ímpar
if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

# Exibir os resultados
print(f"Meu é , {nome}!")
print(f"O meu número da sorte é {numero} é {paridade}.")
