from abc import ABC, abstractmethod
from builtins import super


class Celular(ABC):
    @abstractmethod
    def __init__(self, color , almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento

    @abstractmethod
    def informacion (self):
        print(f"Color {self.color}")
        print(f"Almacenamiento {self.almacenamiento} GB")

    @abstractmethod
    def encender(self):
        print("encendiendo el Celular")

    @abstractmethod
    def apagar(self):
        print("Apagando Celular")


class Android(Celular):

    def __init__(self, color , almacenamiento):
        super(Android, self).__init__(color, almacenamiento)

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")

    def encender(self):
        super(Android, self).encender()
        print("Mostrando logo Android")

    def apagar(self):
        super(Android, self).apagar()

    def informacion(self):
        super(Android, self).informacion()

class Iphone(Celular):

    def __init__(self, color , almacenamiento):
        super(Iphone, self).__init__(color, almacenamiento)

    def transferir_archivo(self):
        print("Transfiriendo Archivos a la computadora")

    def encender(self):
        super(Iphone,self).encender()
        print("Monstrando logo Iphone")

    def apagar(self):
        super(Iphone, self).apagar()

    def informacion(self):
        super(Iphone, self).informacion()

celular_android = Android("Rojo",128)
celular_android.encender()

celular_iphone = Iphone ("Blanco",128)
celular_iphone.encender()

celular_iphone.informacion()
celular_iphone.apagar()