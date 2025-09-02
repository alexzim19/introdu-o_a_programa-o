numero = int(input("digite numero para fatorar: "))
fat = 1 
for i in range(1, numero+1):
    fat *= i
print("o resultado do numero fatorado e: ", fat)