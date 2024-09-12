#Um programa que calcula o peso ideal baseado na altura e sexo do usuário. Expanda este programa para incluir a possibilidade de calcular o IMC (Índice de Massa Corporal) e fazer recomendações baseadas no resultado

sexo = input("Qual o sexo? Masculino(M) ou Feminino(F)")
altura = input("Digite tua altura:")

pesoIdealM = (72.7 * float(altura)) - 58
pesoIdealF = (62.1 * float(altura)) - 44.7

if sexo == "M":
    print("O peso ideal e %.2f: " % pesoIdealM)
elif sexo == "F":
    print("O peso ideal e %.2f: " % pesoIdealF)
else:
    print("Sexo não cadastrado")