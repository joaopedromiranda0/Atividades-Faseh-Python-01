#Faça um jogo de advinhação se o número í igual ao número secreto ou se é diferente ao número secreto. Mostre as mensagens acertou e errou para cada situação

import random

listasDeNumerosSorteados = []
numeroLimite = 10
tentativas = 1

def falar(texto):
    print(texto) 

def exibirTextoNaTela(texto):
    falar(texto)

def exibirMensagemInicial():
    exibirTextoNaTela('Jogo do número secreto')
    exibirTextoNaTela(f'Escolha um número entre 1 e {numeroLimite}')

def verificarChute(chute):
    global tentativas, numeroSecreto
    if chute == numeroSecreto:
        exibirTextoNaTela('Acertou!')
        palavraTentativa = 'tentativas' if tentativas > 1 else 'tentativa'
        mensagemTentativas = f'Você descobriu o número secreto com {tentativas} {palavraTentativa}!'
        exibirTextoNaTela(mensagemTentativas)
        reiniciarJogo()
    else:
        if chute > numeroSecreto:
            exibirTextoNaTela(f'O número secreto é menor que {chute}')
        else:
            exibirTextoNaTela(f'O número secreto é maior que {chute}')
        tentativas += 1

def gerarNumeroAleatorio():
    global listasDeNumerosSorteados

    if len(listasDeNumerosSorteados) == numeroLimite:
        listasDeNumerosSorteados = []

    while True:
        numeroEscolhido = random.randint(1, numeroLimite)
        if numeroEscolhido not in listasDeNumerosSorteados:
            listasDeNumerosSorteados.append(numeroEscolhido)
            print(f"DEBUG: Lista de números sorteados: {listasDeNumerosSorteados}")  
            return numeroEscolhido

def limparCampo():
    pass  # Em uma interface de linha de comando, não há um campo para limpar.

def reiniciarJogo():
    global numeroSecreto, tentativas
    numeroSecreto = gerarNumeroAleatorio()
    tentativas = 1
    exibirMensagemInicial()

# Inicializa o jogo
numeroSecreto = gerarNumeroAleatorio()
exibirMensagemInicial()

# Loop para o jogo (simulação de entrada de usuário)
while True:
    try:
        chute = int(input("Digite seu chute: "))
        verificarChute(chute)
    except ValueError:
        print("Por favor, digite um número válido.")
