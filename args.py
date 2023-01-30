# - Uso de *args possibilita multiplos argumentos a serem recebidos em uma função.
# - Não precisamos mais montar a lista de antemão: os argumentos adicionais dentro do *args são armazenados automaticamente
# em uma tupla dentro da função.

def soma_pontos(*args):
    pontos = 0
    for arg in args:
        pontos += arg
    return pontos


print(soma_pontos(10, 20, 30, 40))

print("------------------------------------------")

# Obrigando o usuário digitar ao menos 2 parametros para fazer a soma_pontos


def soma_pontos(num1, num2, *args):
    pontos = num1 + num2
    for arg in args:
        pontos += arg
    return pontos


print(soma_pontos(10, 20))
