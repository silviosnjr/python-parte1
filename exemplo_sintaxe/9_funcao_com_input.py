#Recebendo valores com a função input()
nome = input("Qual o seu nome: ")
ano = input("Qual o ano atual: ")
nascimento = input("Qual o seu nao de nascimento: ")

#O input recebe valores de texto(string),
#Precisamos converter essa valor para número inteiro
ano = int(ano);
nascimento = int(nascimento)

#Declaração da função escreve_idade
def escreve_idade(nome, ano, nascimento):
    print (nome, "tem", (ano - nascimento), "anos")

#Chamando a função escreve_idade
#e passando as variáveis como parametros
escreve_idade (nome, ano, nascimento)
