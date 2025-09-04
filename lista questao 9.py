numero = int(input("digite o numero para ver se e primo ou nao: "))
contagem =0
if numero<2:
    print("o numero nao e primo: ")

for i in range(1, numero + 1):

    if numero %i ==0:
        contagem += 1

if contagem ==2:
     print("o nuumero e primo")
else:
    print("o numero nao e primo")


 