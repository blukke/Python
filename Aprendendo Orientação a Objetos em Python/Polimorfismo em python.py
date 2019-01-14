class Papagaio:

    def voa(self):
        print("Papagaio pode voar. Papagaio fugiu.")

    def nada(self):
        print("Papagaio morreu afogado. Parabéns.")


class Pinguim:

    def voa(self):
        print("Pinguins não voam. Pinguim está triste")

    def nada(self):
        print("Pinguins nadam. Tentativa de auto afogamento falhou. Pinguim continua triste.")


# área em comum
def testando_voo(passarinhos):
    passarinhos.voa()
    

#instanciando os objetos
azul = Papagaio()
pingu = Pinguim()

#testando o objeto
testando_voo(azul)
testando_voo(pingu)


