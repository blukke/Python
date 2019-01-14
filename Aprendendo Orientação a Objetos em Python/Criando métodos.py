class Papagaio:

    # atributos de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # instanciando métodos
    def cantar(self, musica):
        return "{} está cantando {}".format(self.nome, musica)

    def dancar(self):
        return "Agora {} está dançando!".format(self.nome)

# instanciando o objeto
azul = Papagaio("Azul", 10)

# chamando os métodos da instância
print(azul.cantar("Happy, por Pharrell Williams"))
print(azul.dancar())