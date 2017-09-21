

for n in range (2,30):
    for x in range(2,n):
        if n % x == 0:
            break
    else:
        print ('{:3} é um número  primo'.format(n))