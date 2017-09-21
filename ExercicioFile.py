with open('/home/renato/jihad') as file:
    dic = {}

    for linha in file.read().split():
        dic[linha.lower()] = dic.get(linha.lower(), 0) + 1

    l = reversed(sorted(dic.items(), key=lambda x: x[1]))
    print(*l, sep='\n')
