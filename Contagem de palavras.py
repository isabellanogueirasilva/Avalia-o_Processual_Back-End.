from collections import Counter
texto = input("digite um texto: ")
palavras = texto.split()
quantidade = len(palavras)
palavramaislonga = max(palavras, key=len)
contagem = Counter(palavras)
palavramaiscomum = contagem.most_common(1)[0][0]

print("\nNúmero de palavras:", quantidade)
print("\nPalavra mais longa:", palavramaislonga)
print("\nPalavra que mais aparece:", palavramaiscomum)
