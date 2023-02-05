def division(a, b):
    return a / b


def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)
