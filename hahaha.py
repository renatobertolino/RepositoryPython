import pickle
import math


class Pessoa(object):
    def __init__(self, name, age, cpf):
        self.name = name
        self.__age = age
        self.__cpf = cpf

    def fazer_aniversario(self):
        self.__age += 1

    def print(self):
        print('[{} , {}, {}]'.format(self.name, self.__age, self.__cpf))

    def to_string(self):
        return '[{}, {}, {}]'.format(self.name, self.__age, self.__cpf)

with open('teste.data', 'w') as file:
    nome = input('Digite o seu nome: ')
    age = int(input('Digite a sua idade: '))
    cpf = input('Digite o cpf: ')
    pessoa = Pessoa(nome, age, cpf).to_string()

    print(pessoa.__getattribute__())

    file.write(pessoa)

pickle.dump(file, 'teste.data')




x = Pessoa.to_string
