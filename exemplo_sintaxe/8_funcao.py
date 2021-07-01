#variáveis estáticas
nome = "Fulano"
nascimento = 1987

#Declaração da função escreve_idade
def escreve_idade(nome, ano, nascimento):
    print (nome, "tem", (ano - nascimento), "anos")
    print ("Função Encerrada")

#Chamando a função escreve_idade
#e passando as variáveis como parametros
escreve_idade (nome, 2021, nascimento)