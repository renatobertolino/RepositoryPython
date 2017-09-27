def write(string):
    file = open('crud.txt', 'r')
    text = file.read() + '\n' + string
    file.close()

    file = open('crud.txt', 'w')
    file.writelines(text)
    file.close()


def delete_line(string):
    file = open('crud.txt', 'r')
    text = file.readlines()
    text.remove(string)
    file.close()

    file = open('crud.txt', 'w')
    file.write(str(text))
    file.close()


x = input('Digite: ')
delete_line(x)
