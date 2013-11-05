# calcule avec une "précision n" racine de de 2
def suite1_ab(n):
    a=3
    b=2
    for i in range(n):
        c = a
        a += 2*b
        b += c
        u = a/b
    return u
    
print(suite1_ab(1))
print(suite1_ab(2))
print(suite1_ab(3))
print(suite1_ab(100))