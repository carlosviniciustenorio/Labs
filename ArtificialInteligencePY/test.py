from functools import reduce

nomes = ["Carlos", "Ana", "Pedro", "Beatriz"]

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(i, nomes[i])
    
for i, nome in enumerate(nomes):
    print(i, nome)
    
quadrados = [x ** 2 for x in range(10)]
print(quadrados)

soma = lambda a,b: a + b
print(soma(1,2))

numeros = [1,3,5]
dobrados = list(map(lambda x: x ** 2, numeros))

pares = list(filter(lambda x: x % 2 == 0, range(11)))
print(pares)

print(list(filter(lambda x: x == "Carlos", nomes)))

print(reduce(lambda acc, nome: acc + ", " + nome, nomes))
print(reduce(lambda acc, x: acc * x ** 2, [1,3,5]))

idade = 18
print("maior" if idade >= 18 else "menor")

idades = [27, 30, 22, 28, 30]
for nome, idade in zip(nomes, idades):
    print(nome, idade)
    
if "Carlos" in nomes:
    print("Encontrado")
    
# Criar dicionários com compreensão
print({x: x**2 for x in range(5)})