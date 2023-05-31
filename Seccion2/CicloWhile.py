# x = 0
# while x <= 5:
#     print(f"Hola mundo {x}")
#     x += 1
x= 0
texto = ""
while texto != "salir":
    x = 0
    print("La condición sigue siendo verdadera")
    texto = input("Escribe salir para terminar ")
    while x < 5:
        print(x)
        x += 1
else:
    print("la variable texto = salir")