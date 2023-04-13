

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.get_saldo()} do titular {self.titular}")

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_solicitado):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return  valor_solicitado <= valor_disponivel_para_saque

    def saque(self, valor):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor de {valor} excedeu seu limite, que é de {valor_disponivel_para_saque}")

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def titular(self):
        return self.__titular


    def get_saldo(self):
        return self.__saldo


    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}