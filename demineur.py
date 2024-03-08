import random

ligne=int(input("Entrez le nombre de ligne"))
colonne=int(input("Entrez le nombre de colonne"))
bombe=int(input("Entrez le nombre de bombe"))
tableau=[[0]*colonne for _ in range(ligne)]
compteur_bombe=0

def placer_bombe(nb_bombe,tab):
    verif=0
    while verif<nb_bombe:
        x=random.randint(0,len(tab)-1)
        y=random.randint(0,len((tab[0]))-1)
        while tab[x][y]=='X':
            x=random.randint(0,len(tab)-1)
            y=random.randint(0,len(tab[0])-1)
        tab[x][y]='X'
        verif+=1
'''
def verification(tab):
    for i in range(1,len(tab)-1):
        for j in range(1,len(tab[0])-1):
            if tab[i][j]==0:
                if tab[i-1][j]=='X':
                    tab[i][j]+=1
                if tab[i+1][j]=='X':
                    tab[i][j]+=1
                if tab[i][j-1]=='X':
                    tab[i][j]+=1
                if tab[i][j-1]=='X':
                    tab[i][j]+=1
                if tab[i-1][j-1]=='X':
                    tab[i][j]+=1
                if tab[i+1][j+1]=='X':
                    tab[i][j]+=1
                if tab[i+1][j-1]=='X':
                    tab[i][j]+=1
                if tab[i-1][j+1]=='X':
                    tab[i][j]+=1
'''
def verif_bombe(ligne, colonne):
    for i in range(ligne):
        for j in range(colonne):
            if tableau[i][j]!='X':
                count=0
                for di in range(-1,2):
                    for dj in range(-1,2):
                        if 0<= i+ di<ligne and 0<=j+dj<colonne and tableau[i+ di][j+dj]=='X':
                            count+=1
                tableau[i][j]=count

placer_bombe(bombe,tableau)
verif_bombe(ligne,colonne)
for k in tableau:
    print(k)
