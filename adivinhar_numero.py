import random

numero_aleatorio = random.randint(1, 50)
pergunta = int(input("tente adivinhar o numero de 1 a 50:"))
tentativas = 0
while (pergunta != numero_aleatorio):
    if pergunta < numero_aleatorio:
        print("muito baixo")
    else:
        print("muito alto")
    pergunta = int(input("tente novamente: "))
    tentativas += 1
print(f"meus parabéns você ganhou em {tentativas} tentativas")