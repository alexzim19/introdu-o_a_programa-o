numero = int(input("digite numero para fatorar: "))
cont=1
divisor=1
while cont<=numero:
    if numero%divisor==0:
        cont+=1 
    divisor+=1
if cont==2:
    print("o numero e primo!")
else:
    print("o numero nao e primo!")