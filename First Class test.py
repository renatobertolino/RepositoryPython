def square(x):
    return x * x

def cube(x):
    return x * x * x

def print_result(x, func):
    return func(x)

do_square = square
do_cube = cube

res = print_result(5, do_square)
print(res)
res = print_result(5, do_cube)
print(res)