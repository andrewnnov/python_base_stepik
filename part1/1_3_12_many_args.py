def print_ab(a, b, *args):
    print("positional argument a ", a)
    print("positional argument b ", b)
    print("additional arguments: ")
    for arg in args:
        print(arg)


print_ab(10, 20, 30, 40, 50, 60)


def print_cd(c, d, **kwargs):
    print("positional argument c ", c)
    print("positional argument d ", d)
    print("additional arguments: ")
    for key in kwargs:
        print(key, kwargs[key])


print_cd(10, e=30, f=40, jimmi=123, d=20)