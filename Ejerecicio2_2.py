def codificar(mensaje, desplazamiento):
    #Codifica el mensaje tomando un carácter del mensaje original, lo desplaza en el alfabeto y luego 
    #agrega el carácter final al mensaje codificado. El % 26 calcula el modulo y se asegura de esté dentro del rango de letras del alfabeto.
    mensaje_codificado = "" #Acumula y construye el mensaje a medida que se recorren los caracteres del mensaje original y el desplazamiento.
    for letra in mensaje: 
        mensaje_codificado += chr(((ord(letra)) + (desplazamiento % 26))) #El += se usa para ir acumulando valores.
    return mensaje_codificado

def decodificar(mensaje, desplazamiento):
    #Decodifica el mensaje tomando un carácter del mensaje original, lo desplaza en el alfabeto y luego 
    #agrega el carácter final al mensaje decodificado. El % 26 calcula el modulo y se asegura de esté dentro del rango de letras del alfabeto.
    mensaje_decodificado = "" #Acumula y construye el mensaje a medida que se recorren los caracteres del mensaje original y el desplazamiento.
    for letra in mensaje: 
        mensaje_decodificado += chr(((ord(letra)) - (desplazamiento % 26)))
    return mensaje_decodificado

def ejecutacion_del_programa(opcion, mensaje, desplazamiento):
    if opcion == 1: 
       return codificar(mensaje, desplazamiento) 
    if opcion == 2:
       return decodificar(mensaje, desplazamiento)
   
def menu():
    while(True): #Ciclo infinito
        print("\nMENÚ:\n1 -> Codificar\n2 -> Decodificar\n3 -> Salir\n") #\n se usa para nuevas lineas, los numeros de al lado, enumeran el menú.
        opcion = int (input('Opción deseada del menú: ')) #Recibe un valor para la opción del menú (1, 2, 3).
        if opcion == 3:
            break #Para salir del menú.
        mensaje = input('Ingrese la cadena de texto: ') #Recibe el mensaje a condificar o decodificar.
        desplazamiento = int(input('Ingrese el valor del desplazamiento: '))
        resultado = ejecutacion_del_programa(opcion, mensaje, desplazamiento)
        print("El resultado es: ", resultado)

menu()