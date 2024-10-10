#ejercicio 1
def mayor_si(a,b,c):
     if a==b:
          print("error")
    

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

