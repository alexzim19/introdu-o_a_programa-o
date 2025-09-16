soma_positivos = 0 
quantidade_negativa = 0
i = 0
while i < 20:
    num = int(input(f"digite  {i+1} numero: "))
    if num > 0:
        soma_positivos += num
    elif num < 0:
        quantidade_negativa += 1
        i += 1
        print("soma dos positivos:", soma_positivos)
        print("quantidade de negativos:",quantidade_negativa)
          
