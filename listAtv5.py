#Condicionais Simples: Descrição: O programa avalia notas e determina se o aluno foi aprovado,está em recuperação, ou foi reprovado. Melhore o programa para calcular amédia ponderada, onde a nota de provas tem peso maior que a detrabalhos. Objetivo: Praticar o uso de condicionais e cálculos de médias.
print ('Resultado Final')
def calcularMediaPonderada(notaProvas, notaTrabalhos):
    pesoProvas = 0.7
    pesoTrabalhos = 0.3
    mediaPonderada = (notaProvas * pesoProvas) + (notaTrabalhos * pesoTrabalhos)
    return mediaPonderada

def avaliarAluno(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

# Solicitar as notas do usuário
notaProvas = float(input("Digite a média das provas: "))
notaTrabalhos = float(input("Digite a média dos trabalhos: "))

# Calcular a média ponderada
mediainal = calcularMediaPonderada(notaProvas, notaTrabalhos)

# Avaliar a situação do aluno
situacao = avaliarAluno(mediainal)

# Exibir os resultados
print(f"Média ponderada: {mediainal:.2f}")
print(f"Situação do aluno: {situacao}")

