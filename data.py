class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


hoje = Data(22, 4, 2023).formatada()


# Classe abstrata Animal
class Animal:
    def andar(self):
        pass


# Mixin para animais que voam
class Voador:
    def voar(self):
        print("Voando...")


# Mixin para animais que nadam
class Nadador:
    def nadar(self):
        print("Nadando...")


# Classe final para um pássaro que voa e anda
class PassaroVoador(Animal, Voador):
    def andar(self):
        print("Andando com as pernas...")


# Classe final para um pato que voa, nada e anda
class Pato(Animal, Voador, Nadador):
    def andar(self):
        print("Andando com as pernas...")


Pato().andar()
PassaroVoador().andar()

# Função que recebe um objeto Animal e chama seus métodos "andar" e "comer"
def realizar_acao(animal):
    animal.andar()
    animal.comer()


# Classe que representa um cachorro
class Cachorro:
    def andar(self):
        print("Andando com as patas...")

    def comer(self):
        print("Comendo ração...")


# Classe que representa um gato
class Gato:
    def andar(self):
        print("Andando com as patas...")

    def comer(self):
        print("Comendo ração para gatos...")


# Instâncias de Cachorro e Gato
meu_cachorro = Cachorro()
minha_gata = Gato()

# Chamando a função com as instâncias de Cachorro e Gato
realizar_acao(meu_cachorro)
realizar_acao(minha_gata)
