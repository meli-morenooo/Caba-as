import sys
def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero

def validacionEntero(message='Ingrese un numero entero: ', min=0,max=sys.maxsize):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    validacion = False
    while validacion == False:
        try:  
            numero = inputNumber('entero',message)
            if numero >= min and numero <= max:
                validacion = True
                return numero
            else: 
                print("Ingrese una opcion entre {} y {}".format(min,max))
        except:
            return 'Error, argumento invalido'
