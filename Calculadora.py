class Calculadora(object):

    def adicao(self, number1, number2):
        return number1 + number2

    def subtracao(self, number1, number2):
        return number1 - number2

    def divisao(self, number1, number2):
        return number1 / number2

    def multiplicacao(self, number1, number2):
        return number1*number2

    def primo(self, number):
        count = 0
        for x in range(1,number):
            if number%x==0:
                count+=1

        if count==1:
            return True
        else:
            return False
c = Calculadora()
print(c.primo(2))