mot=input("Entrez votre mot\n")
verification=False
for lettre,_ in enumerate(mot,1):
    if mot[lettre-1]==mot[-lettre]:
        verification=True
    else:
        verification=False

if verification==True:
    print("le mot {} est un palyndrome" .format(mot))
else:
    print("le mot {} n'est pas un palyndrome" .format(mot))
