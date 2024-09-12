#Faça um programa para calcular o peso ideal, para pessoa levando em consideração a altura da pessoa. Para homens o cálculo é (altura*72.7)-58 para mulheres (altura*62.1)-44.7

#1)_ Para homenens: (altura*72.7)-58
#2)_ Para mulheres: (altura*62.1)-44.7
#3)_ Entrada de dados da pessoa

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