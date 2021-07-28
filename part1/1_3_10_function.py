def print_ab(a, b):
    print(a)
    print(b)


# correct ways to call a function
print_ab(10, 20)
print_ab(a=10, b=20)
# keyword arguments always after non-keyword arguments
print_ab(10, b=20)

list_with_arguments = [40, 50]
print_ab(*list_with_arguments)

map_with_arg = {'a': 60, 'b': 70}
print_ab(**map_with_arg)
