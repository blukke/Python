class Papagaio:

    # atributos da classe
    especie = "pássaro"

    # atributos de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# instanciar a classe Papagaio
azul = Papagaio("Azul", 10)
vermelho = Papagaio("Vermelho", 15)

# acesso aos atributos de classe
print("Azul é uma {}".format(azul.__class__.especie))
print("Vermelho também é umm {}".format(vermelho.__class__.especie))

# acesso aos atributos de instância
print("{} tem {} anos".format(azul.nome, azul.idade))
print("{} tem {} anos".format(vermelho.nome, vermelho.idade))

