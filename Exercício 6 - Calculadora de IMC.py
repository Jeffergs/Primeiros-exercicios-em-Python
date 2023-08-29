peso = float(input("Escreva o seu peso atual: "))
altura = float(input("Escreva a sua altura: "))

IMC = peso / (altura**2) #altura ao quadrado --> **2

print(f"seu IMC é de {IMC:.1f}")
