contagem = 0
maiormedia = 0
menormedia = 9999
qtdeaprov = 0
qtderep = 0
while contagem!=3:
    contagem+=1
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))  
    n3 = float(input("Digite a nota 3: "))
    media = (n1+n2+n3) / 3  
    if media>maiormedia:
       maiormedia = media
    if media<menormedia:
       menormdia=media
    if media>=6:
       qtdeaprov+=1
    else: 
       qtderep+=1
print("a maior media e",maiormedia)
print("a menor media e",menormedia)
print("a quantidade de alunos aprovados e",qtdeaprov)     
print("a quantidade de alunos reprovados e",qtderep)  