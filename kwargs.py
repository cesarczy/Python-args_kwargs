# - O uso de **kwargs possibilita multiplos argumentos chaves a serem recebidos em uma função.
# - Esses argumentos são adaptados como chaves de um dicionário. Podemos interpretar essas chaves
# independente da orgem em que foram chamadas.

def pontuação_total(pontos, **kwargs):
    pontos_multiplicador = kwargs.get('multiplicador')
    pontos_bonus = kwargs.get('bonus')

    if pontos_bonus:
        pontos += pontos_bonus
    if pontos_multiplicador:
        pontos = pontos * pontos_multiplicador
    return pontos

pontuação_final = pontuação_total(100.0)
print(pontuação_final)

pontuação_final = pontuação_total(100.0, bonus=500.0)
print(pontuação_final)

pontuação_final = pontuação_total(100.0, multiplicador=1.5)
print(pontuação_final)

pontuação_final = pontuação_total(100.0, bonus=500.0, multiplicador=1.5)
print(pontuação_final)