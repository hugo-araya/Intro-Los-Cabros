def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
def max_de_tres(a, b, c):
    return(max(c, max(a,b)))

a = 3
b = 2
c = 5
print(max_de_tres(a, b, c))

