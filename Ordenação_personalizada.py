numeros = []
prompts = [
    "Digite o 1 número: \n (um deles deve ser seu número da chamada) ",
    "Digite o 2 número: ",
    "Digite o 3 número: ",
    "Digite o 4 número: ",
    "Digite o 5 número: ",
    "Digite o 6 número: ",
    "Digite o 7 número: ",
    "Digite o 8 número: ",
    "Digite o 9 número: ",
    "Digite o 10 número: "
]

for texto_prompt in prompts:
    numero_digitado = int(input(texto_prompt))
    numeros.append(numero_digitado)

print("\nlista original:", numeros)
ordenada = sorted(numeros)
print("\nlista em ordem crescente:", ordenada)
sem_repetidos = list(set(numeros))
print("\nlista sem repetidos:", sem_repetidos)
