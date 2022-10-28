def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key, value)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)