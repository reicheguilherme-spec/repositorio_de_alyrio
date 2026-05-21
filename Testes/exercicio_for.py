nomes = ["Reiche", "Enzo", "Dandj", "Moura"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        for k in range(j + 1, len(nomes)):
            print(nomes[i], nomes[j], nomes[k])
