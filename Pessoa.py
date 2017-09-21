class Pessoa:

    def __init__(self, nome, age, gender):
        self.nome = nome
        self.age = age
        self.gender = gender


class Funcionario(Pessoa):

    def __init__(self, salary):
        self.salary = salary



