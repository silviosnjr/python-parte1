nome = input("Qual o seu nome ?")

#todo input recebe um valor de texto(string)
#se precisar fazer algum cálculo tem que converter para número
#você pode converter no momento da inicialização da variável
data_nascimento = int(input("Em que ano você nasceu?"))

print("Bem vindo {}, você tem hoje {} anos".format(nome, (2021 - data_nascimento)))