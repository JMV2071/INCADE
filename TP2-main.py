#ejercicio 1
def mayor_si(a,b,c):
    if a>b:
        if a>c:
            mayor=a
    else:
        if b>a:
            if b>c:
                mayor = b
            else:
                mayor = c
    return mayor

mayor = mayor_si(1,3,1)
print(mayor)