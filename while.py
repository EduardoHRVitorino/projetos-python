digitado = int(input("digite o valor para fazer a tabuada:"))
multiplicador = 1
while(multiplicador <= 10):
    r = digitado * multiplicador
    print("{} x {} = {}".format(digitado, multiplicador, r))
    multiplicador = multiplicador + 1