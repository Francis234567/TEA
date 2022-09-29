# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Autor : francis.rios@est.zamorano.edu
# Fecha : 2022.09.22
# Editado : 2022.09.22

def calcularpago(horas,dinero):
  MAX_HORAS=40
  if(horas>MAX_HORAS):
     horas_extras= int(horas)-MAX_HORAS
     calculo=int(horas)*int(dinero)+(horas_extras*(int(dinero)/2))
  return calculo
try:
 horas=float(input("Cuantas horas ha trabajado?"))
 dinero=float(input("Cuanto gana por hora?"))
 pago = calcularpago(horas,dinero)
 print("Usted deberia recibir: ",pago)
except:
    print("Error, valor ingresado no es valido")
   





