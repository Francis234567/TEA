# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Autor : francis.rios@est.zamorano.edu
# Fecha : 2022.09.22
# Editado : 2022.09.22
from turtle import done


contador=0
sumatoria=0
while True:
    input_str=input("ingrese un numero: ")
    try:
        if (input_str == 'done'):
            break
        else:
            contador = contador + 1
            sumatoria = sumatoria + int(input_str)
            promedio = sumatoria / contador
    except:
        print("Error, debe ingresar un numero")
        continue
print("contador:", contador)
print("Sumatoria:", sumatoria)
print("Promedio:", promedio)