somavalor=0
contnegativo=0
for i in range(20):
    valor=int(input("digite o valor: "))
    if valor>=0:
        somavalor+=valor
    else:
        contnegativo+=1
print("a soma dos valores positivos e: ",somavalor) 
print("a quantidade de valores negativos e: ",contnegativo)           