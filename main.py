
# inscription :

noms =[]

while True:
    nom = input("Entrez votre nom : ")
    if nom == "":
        break
    noms.append(nom)

print()
print("Nom des personnes : ")
noms.sort()
for nom in noms:
    print(" " + nom)