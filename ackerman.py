calls = 0



def ackerman (m, n):
    global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman(m - 1, 1)
    else:
        print(calls)
        return ackerman(m - 1, ackerman(m, n - 1))

print(ackerman(5, 3))
