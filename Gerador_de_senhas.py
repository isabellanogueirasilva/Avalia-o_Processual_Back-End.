import random
print("gerador de senha")
nome = input("digite seu nome: ")
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*,?"
tamanho = 25
antes = (tamanho - len(nome)) // 2
depois = tamanho - len(nome) - antes
parte1 = ""
for i in range(antes):
    parte1 += random.choice(caracteres)

parte2 = ""
for i in range(depois):
    parte2 += random.choice(caracteres)

senha = parte1 + nome + parte2

print("senha gerada:", senha)
