def pie(r):
    def circleArea(d):
        return r * (d ** 2)
    return circleArea

c = pie(3.14)
print (c(2))