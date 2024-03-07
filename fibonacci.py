nbr_max=int(input("Entrez votre nombre max\n"))
nbr_max=nbr_max+1
tab_fibo=[0,1]
for i in range(2,nbr_max):
    tab_fibo.append(tab_fibo[i-1]+tab_fibo[i-2])
print(tab_fibo)

nombre=int(input("entrez le nombre pour lequel vous recherchez la valeur dans la suite de fibonacci\n"))
print(tab_fibo[nombre])