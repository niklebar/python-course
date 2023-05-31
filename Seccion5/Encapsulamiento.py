from abc import ABC, abstractmethod
from builtins import super


class Celular(ABC):
    @abstractmethod
    def __init__(self, color , almacenamiento):
        self.__color = color
        self.__almacenamiento = almacenamiento
        self.__volumen = 5

    @abstractmethod
    def informacion (self):
        print(f"Color {self.__color}")
        print(f"Almacenamiento {self.__almacenamiento} GB")
        print(f"Nivel volumen: {self.__volumen}")

    @abstractmethod
    def encender(self):
        print("encendiendo el Celular")

    @abstractmethod
    def apagar(self):
        print("Apagando Celular")

    def subir_volumen(self):
        self.__volumen +=1
        print(f"El volumen actual es : {self.__volumen}")

    def __bajar_volumen(self):
        self.__volumen -= 1
        print(f"El volumen actual es : {self.__volumen}")

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
# celular_android.color = "Azul"
# celular_android.volumen = 15
celular_android.informacion()
celular_android.subir_volumen()
celular_android.subir_volumen()
# celular_android.bajar_volumen()

celular_iphone = Iphone ("Blanco",128)
celular_iphone.encender()

celular_iphone.informacion()
celular_iphone.apagar()