class Celular:
    variable_ejemplo = "Ejemplo Clase"

variable_contenedora_objeto_celular = Celular()
# print(variable_contenedora_objeto_celular.variable_ejemplo)

objeto2 = Celular()
# print(objeto2.variable_ejemplo)
objeto2.variable_ejemplo = "Objeto numero 2"
print(variable_contenedora_objeto_celular.variable_ejemplo)
print(objeto2.variable_ejemplo)
