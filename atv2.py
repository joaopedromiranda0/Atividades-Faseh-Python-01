#Faça um program que irá receber um nome e um número digitado pelo usuário e mostre ao final uma mensagem informada o nome e o numero que foram digitados pelo usuário

print("Trabalhando com condicionais")
print("Compras de pacotes de viagem")

listas_de_destinos = ["BH", "RJ", "SP"]
idadeComprador = 22 
estaAcompanhada = True
temPassagemComprada = False
destino = "BH"

print("Destinos possíveis")
print(listas_de_destinos)

pode_comprar = idadeComprador >= 18 or estaAcompanhada

contador = 0 
destinoExiste = False 

while contador < len(listas_de_destinos):
    if listas_de_destinos[contador] == destino:
        destino_existe = True
        break
    else:
        print("Destino não existe")
    contador += 1  

print('Destino existe:', destino_existe)

if pode_comprar and destino_existe:
    print("Boa Viagem!!")
else:
    print("Desculpe! Tivemos um erro")

# Loop for para verificar o destino
for cont in range(len(listas_de_destinos)):
    if listas_de_destinos[cont] == destino:
        destino_existe = True
