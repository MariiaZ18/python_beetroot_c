# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def fun(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add


func = fun(4)
print(func(4))
