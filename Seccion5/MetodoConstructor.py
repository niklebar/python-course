class Celular:
    variable_ejemplo = "Ejemplo"

    def __init__(self):
        self.color = "Rojo"

    def encender (self):
        print("Encendiendo Telefono")

    def apagar(self):
        print("Apagando celular")

objeto_celular = Celular()
print(objeto_celular.color)
objeto_celular.encender()