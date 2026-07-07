print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
if idade < 0:
        print("Idade inválida.")
else:
    if idade >= 18:
        print(nome, "é maior de idade.")
    else:
        print(nome, "é menor de idade.")