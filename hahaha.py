import pickle
class Pessoa(object):
    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    def fazer_aniversario(self):
        self.__age += 1

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getCpf(self):
        return self.__cpf

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setCpf(self, cpf):
        self.__cpf = cpf

    def print(self):
        print('[{} , {}, {}]'.format(self.__name, self.__age, self.__cpf))

    def to_string(self):
        return '[{}, {}, {}]'.format(self.__name, self.__age, self.__cpf)

with open('C:\\Users\\johnN\\Desktop\\teste.data', 'w') as file:
    nome = input('Digite o seu nome: ')
    age = int(input('Digite a sua idade: '))
    cpf = input('Digite o cpf: ')
    pessoa = Pessoa(nome, age, cpf).to_string()

    file.write(pessoa)

pickle.dump(file, 'C:\\Users\\johnN\\Desktop\\teste.data')




x = Pessoa.to_string
