#MAXIMUM D'UN TABLEAU
tableau=[[0,18],[1,55],[45,48],[-3,2]]
max=tableau[0][0]
for i in range(1,4):
    for j in range(1,2):
        if tableau[i][j]>max:
            max=tableau[i][j]
print("Le maximum du tableau est {}".format(max))