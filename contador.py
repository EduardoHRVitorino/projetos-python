
for contador in range(1, 101):
    verificar = contador % 2
    if verificar == 0:
        print(f"{contador} = esse número é par")
    else:
        print(f"{contador} = esse número é ímpar")