

try:
    print(5/0)
    #import matho
except ZeroDivisionError as error_division:
    print(f"Ha ocurrido el error {error_division}")
except ImportError:
    print("Ha ocurrido un error de importacion")
else:
    print("no hubo ningun error")
finally:
    print("Esto siempre se ejecuta haya o no error")
