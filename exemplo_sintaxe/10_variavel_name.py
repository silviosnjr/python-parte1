# A variável __ name __ representa o nome do módulo.
# Entretanto, quando o módulo é executado por si só como um programa __name__ é definido para main
# diferente de quando o módulo é importado, no qual o valor fica de fato igual ao nome do módulo

def testa_name() :
    print("Variável name contém:", __name__)

# O if é muito utilizado quando seu programa é todo executado através de funções
if(__name__ == "__main__"):
    testa_name()