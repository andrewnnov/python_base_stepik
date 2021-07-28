def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res



print("__Variant1__")
print(s(11, b=20))

print("__Variant2__")
print(s(5, 5, 5, 5, 1))

# print("__Variant3__")
# s(b=31)

print("__Variant4__")
print(s(11, 10, 10))

print("__Variant5__")
print(s(0, 0, 31))

print("__Variant6__")
print(s(11, 10))

# print("__Variant7__")
# s(b=31, 0)

print("__Variant8__")
print(s(21))

print("__Variant9__")
print(s(11, 10, b=10))