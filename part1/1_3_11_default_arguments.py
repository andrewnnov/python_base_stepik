def print_ab(a, b):
    print(a)
    print(b)


# correct
def print_ab_one_default(a, b=10):
    print(a)
    print(b)


# correct
def print_ab_two_default(a=10, b=10):
    print(a)
    print(b)


# incorrect
# def print_ab_one_default(a=10, b):
#     print(a)
#     print(b)


list_example = [4, 5, 7, 1, 2, 10]
list_example.sort(reverse=True)
print(list_example)