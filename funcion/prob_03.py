
def max_de_tres(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

a = 3
b = 2
c = 5
print(max_de_tres(a, b, c))

