#1) Faça um programa que mostre os tipos de variáveis, interios , booleano, String e floats. 

print("Trabalhando com condicionais")

listas_de_destinos = ["BH", "RJ", "SP"]

# Adiciona novas opções de destinos
listas_de_destinos.extend(["PR", "RS"])

idadeComprador = 21
estaAcompanhada = False
temPassagemComprada = False

print("Destinos possíveis")
print(listas_de_destinos)

if idadeComprador >= 18 or estaAcompanhada:  
    print("Comprador maior de idade")
    print("Boa Viagem!!!")
    listas_de_destinos.pop(2)  
elif estaAcompanhada:
    print("Comprador está acompanhado")
    listas_de_destinos.pop(2)
else:
    print("Não é maior de idade e não posso vender")

print("Verificação de Embarque: \n\n")
if idadeComprador > 18 and temPassagemComprada: 
    print("Boa Viagem!!")
else:
    print("Você não pode embarcar")
