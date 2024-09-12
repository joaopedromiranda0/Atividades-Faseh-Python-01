#: Um programa que calcula as médias das notas de provas etrabalhos e determina se o aluno foi aprovado. Adicione a funcionalidadede calcular médias trimestrais e uma média anual ao final.


nota_primeiro_bi = 8
nota_segundo_bi = 6.3
nota_terceiro_bi = 7


media = (nota_primeiro_bi + nota_segundo_bi + nota_terceiro_bi ) / 4

if media >= 7:
    media += media * 0.1

print(f"A média é {media:.2f}")



