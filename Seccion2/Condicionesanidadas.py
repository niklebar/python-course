numero = int(input("escribe un numero "))



if numero>10:
    print("El numero es mayor a 10")
    if numero > 30:
        print("Ademas, el numero es mayor a 30 ")
    elif numero >20:
        print("el numero es mayor a 20")
        if True:
            print("Linea ejemplo")
    else:
        print("Ademas el numero es menor que 21")
else:
    print("El numero no es mayor a 10")