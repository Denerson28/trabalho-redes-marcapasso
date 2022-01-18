import random

array_de_nomes = ["Miguel", "Denerson", "Heitor", "Theo", "Gabriel", "Bernardo", "Samuel", "Mairon", "Helena", "Luana", "Laura", "Maria Alice", "Poli", "Luisa", "Maria Clara", "Maria Cecilia", "Maria Julia"]
array_de_sobrenomes = ["Silva", "Azevedo", "Oliveira", "Tobias", "Rodrigues", "Ferreira", "Berudio",  "Pereira", "Lima", "Leal", "Ribeiro"]

for i in range(5):
    vetor = []
    open(f'infos_pessoa{i}.txt', "x")
    document = open(f'infos_pessoa{i}.txt', "w")
    document.write(array_de_nomes[random.randint(0, 16)] + " " + array_de_sobrenomes[random.randint(0, 9)])
    document.write("\n" + f'{random.randint(45, 90)}')

    for i in range(0, 50):
        vetor.append(random.randint(30, 120))

    document.write("\n" + f'{vetor}')