import datetime

from re import split


def calcular_edad(year):
    date = datetime.date.today()
    year_act = round(int(date.strftime("%Y")),0)
    edad = year_act - year
    print(f"Su edad es de {edad} años")
    return edad

def det_adulto(edad):

    tipo = type(edad)

    if(tipo != str) or (edad > 0):
        if(edad >= 18):
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")
    else:
        print("Fecha inválida")

    