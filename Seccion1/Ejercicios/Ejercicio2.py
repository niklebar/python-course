# ejercicio 2
# Escribe un programa que le pida al usuario el numero de horas de trabajo diarias y una taria por hora para calcular el salario
# Al final imprimir el salario
numero_horas = input("Introduzca Numero de hora de trabajo diarias ")
tarifa = input("Introduzca Tarifa por Hora ")
numero_horas = float(numero_horas)
tarifa = float(tarifa)
salario = numero_horas * tarifa
salario = salario *5*4
print(f"El salario mensual es de: {salario}")