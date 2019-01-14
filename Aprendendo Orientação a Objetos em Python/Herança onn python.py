# classe pai/superclasse
class Passaro:

    def __init__(self):
        print("Passaro está pronto")

    def identificador(self):
        print("Passaro")

    def nadar(self):
        print("Nada mais rápido")


# classe filha/subclasse
class Pinguim(Passaro):

    def __init__(self):
        # chama a funçãoa super() para puxar o conteudo do metodo __init__() da classe pai para a classe filha
        super().__init__()
        print("Pinguim está pronto \n")

    def identificador(self):
        print("Pinguim")

    def correr(self):
        print("Corre mais rápido")


pingu = Pinguim()
pingu.identificador()
pingu.nadar()
pingu.correr()



