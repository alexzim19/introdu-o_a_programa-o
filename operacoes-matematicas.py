import os 
print("********** operacoes matematicas **********")
print("escollha uma das opecoes abaixo. para encerrar digiti sair!!:")
print("1 - soma")
print("2 - subitracao")
print("3 - multiplicacao")
print("4 - divisao")
print("5 - par ou impar")
print("6 - primo")
print("7 - fatorial")
opcao=input("digite a opcao desejada ou <sair> para encerrar:")
opcaoMaiusc=opcao.upper()
while opcaoMaiusc!="SAIR":
    if opcao=="1":
        numero1=int(input("digite o primeiro valor:"))
        numero2=int(input("digite o segundo valor:"))
        print("o resultado da soma entre ",numero1,"e",numero2,"e",numero1+numero2,)
    input("presione ENTER para voltar ao menu!")
    if opcao=="2":
        numero1=int(input("digite o primeiro valor:"))
        numero2=int(input("digite o segundo valor:"))
        print("o resultado da subtracao entre ",numero1,"e",numero2,"e",numero1-numero2,)
    if opcao=="3":
        numero1=int(input("digite o primeiro valor:"))
        numero2=int(input("digite o segundo valor:"))
        print("o resultado da produto entre ",numero1,"e",numero2,"e",numero1*numero2,)
    if opcao=="4":
        numero1=int(input("digite o primeiro valor:"))
        numero2=int(input("digite o segundo valor:"))
        print("o resultado da divisao entre ",numero1,"e",numero2,"e",numero1/numero2,)
    if opcao=="5":
        numero=int(input("digite um numero para saber se ele e par ou impar: "))
        if numero%2==0:
            print("o numero", numero,"e par!!!")
        else:
            print("o numero", numero,"e impar!!!")
    
    
    
    
    
    input("presione ENTER para voltar ao menu! : ")
    os.system("cls")
    print("escollha uma das opecoes abaixo. para encerrar digiti sair!!:")
    print("1 - soma")
    print("2 - subitracao")
    print("3 - multiplicacao")
    print("4 - divisao")
    print("5 - par ou impar")
    print("6 - primo")
    print("7 - fatorial")




