teste = int
#estrutura for variavel in "range"(opcional)(começo, fim, de quanto em quanto)
for teste in range(1, 11):
    print("{}".format(teste))


pergunta = input("voce quer continuar? s ou n")
if(pergunta == "S" or pergunta == "s" or pergunta == "sim"):
    for teste in range(10, 21):
        print("{}". format(teste))
    print("programa finalizado")
else:
    print("programa finalizado")
