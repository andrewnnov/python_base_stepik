def function_name(arg1, arg2):
    return arg1 + arg2


x = function_name(2, 8)
y = function_name(x, 21)

print(type(x))
print(type(y))
print(type(function_name(1, 2)))

print(type(function_name))
print(id(function_name))
