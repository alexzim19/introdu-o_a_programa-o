jogadores = 0
somaAltura = 0 
jogadores = int(input("numero de jogadores:"))
for i in range(jogadores):
    altura = float(input("digite a altura dos jogadores: "))
    somaAltura+=altura
print("a media das alturas e: " ,somaAltura/jogadores)