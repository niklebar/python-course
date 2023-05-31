class Celular:
    def __init__(self, color , almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento

    def informacion (self):
        print(f"Color {self.color}")
        print(f"Almacenamiento {self.almacenamiento} GB")

    def encender(self):
        print("encendiendo el Celular")

    def apagar(self):
        print("Apagando Celular")


class Android(Celular):

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")

class Iphone(Celular):

    def transferir_archivo(self):
        print("Transfiriendo Archivos a la computadora")

celular_android = Android("Blanco",64)

celular_android.expandir_almacenamiento()
celular_android.informacion()

celular_iphone = Iphone("Verde", 128)
celular_iphone.transferir_archivo()
celular_iphone.informacion()
