from edad import*
from validar_dui import*

print("INGRESE SU FECHA DE NACIMIENTO SEGÚN EL FORMATO DD/MM/AAAA(use las plecas inclinadas)")

fecha_N = input("Fecha: ")

dui = input("Ingrese su número de DUI (sin guion ni espacios): ")



lista = (split("/",fecha_N))
year = int(lista[2])


edad = calcular_edad(year)

det_adulto(edad)

valid_DUI(dui)

