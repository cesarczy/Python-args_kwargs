# - Faça a soma das pontuações
# Para isso, usamos uma função:

def soma_pontos(num1, num2):
    total = num1 + num2
    return total


print(soma_pontos(10, 20))


# ou
print("------------------------------------------")


pontos = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0]

soma_pontos = sum(pontos)
print(soma_pontos)
