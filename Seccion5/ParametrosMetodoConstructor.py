class Celular:
    variable_ejemplo = "Ejemplo"

    def __init__(self, color):
        self.color = color

    def encender (self, contrasena):
        print(f"Encendiendo Telefono {self.color}  {contrasena}")

    def apagar(self):
        print("Apagando celular")

objeto_celular = Celular("verde")
print(objeto_celular.color)
objeto_celular.encender("12345")