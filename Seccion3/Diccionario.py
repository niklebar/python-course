# crear un diccionario vacio
diccionario = {}
print(diccionario)
print(type(diccionario))

# Asignar valores a nuestro diccionario
diccionario["nombre"] = "Elkin"
diccionario["edad"] = 46
print(diccionario)


# obtener el valor vinculado a una llave
print(diccionario["edad"])
print(diccionario.get("edad"))

# Crear diccionario asignando valores desde el principio

diccionario2 = {5.1:10, "vocales":["a","e","i","o","u"], (7,2):50}
print(diccionario2)

# Len
print(len(diccionario2))

# del
del(diccionario2[(7,2)])
print(diccionario2)

# propiedad keys, llaves que contiene el diccionario
print(diccionario2.keys())


# Propiedad values
print(diccionario2.values())

# PopItem
print(diccionario2)
clave_valor = diccionario2.popitem()
print(diccionario2)
print(clave_valor)

# Combinar diccionarios
print(diccionario)
print(diccionario2)


diccionario.update(diccionario2)
print(diccionario)

# propiedad pop
diccionario.pop("nombre")
print(diccionario)