
pergunta = int(input("informe o valor da tabuada:"))
for multiplicador in range(10):
    operacao = pergunta * (multiplicador + 1)
    print(f"{pergunta} x {multiplicador} = {operacao}")


enter = input("\npressione <Enter> para encerrar..")