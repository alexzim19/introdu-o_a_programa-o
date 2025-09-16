contagem = 0
somaAltura = 0 
jogadores = int(input("numero de jogadores:"))
while contagem!=jogadores:
    altura = float(input("digite a altura dos jogadores: "))
    somaAltura+=altura
    contagem+=1
print("a media das alturas e: " ,somaAltura/jogadores)