class Pessoa:

    _nome = None
    _idade = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade= idade

    def printa_nome(self):
        print("O nome é " + self.nome)

    def printa_idade(self):
        print(self.idade)

