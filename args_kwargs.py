# Usando args e kwargs

def pontuacao_total(num1, num2, *args, **kwargs):
    #    usando args
    pontos = num1 + num2
    for arg in args:
        pontos += arg

# usando kwargs
    pontos_bonus = kwargs.get('bonus')
    pontos_multiplicador = kwargs.get('multiplicador')
    if pontos_bonus:
        pontos += pontos_bonus
    if pontos_multiplicador:
        pontos = pontos * (pontos_multiplicador)
    return pontos

pontuacao_final = pontuacao_total(100.0, 200.0, 200.0, bonus=500.0, multiplicador=2)

print(pontuacao_final)
