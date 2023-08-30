def retorna_un_real(mensaje): #Evita que el usuario ingrese letras.
    while(True): 
        dato = input(mensaje) #Solicita un dato y lo asigna a la variable.
        if dato.isalpha(): #Condición que verifica si el dato consiste en letras.
            print('Por favor ingrese un valor valido...') 
        else:
            break 
    return dato

def retorna_un_entero(mensaje): #Evita que se ingrese un dato diferente a un entero.
    while(True):
        dato = input(mensaje) 
        if dato.isnumeric(): #Condición que solo sean caracteres númericos
            break 
        else:
            print('Por favor ingrese un valor valido...')
    return dato

def ingresar_ecuacion_diferencial(mensaje): #Impide que la ecuación tenga variables diferentes a x y y.
    while True:
        ecuacion_diferencial = input(mensaje) 
        caracteres_permitidos = 'xy+-*/() 0123456789.' #Solo estos valores se permiten en la EDO.
        caracteres_validos = True 
        
        for caracter in ecuacion_diferencial: #Bucle de cada caracter en la EDO ingresada.
            if caracter not in caracteres_permitidos: 
                caracteres_validos = False 
                break
        
        if caracteres_validos: 
            break
        else:
            print("La EDO debe contener solo 'x', 'y', '*', '/', '-', '()' y '+'. Inténtalo de nuevo.")
            
    return ecuacion_diferencial

def metodo_euler(ecuacion_diferencial, inicial_x, inicial_y, distancia_del_paso, numero_de_datos):
    #Esta función resuelve la EDO con el método de euler.
    x = float(inicial_x) 
    y = float(inicial_y) 
    print('Iteracion' + ' '*5 + ' x ' + ' '*5 + ' y ') 
    print('0' + ' '*13 + f'{x}' + ' '*5 + f'{y}' ) 
    for i in range(int (numero_de_datos)):
        #entra en un bucle donde el valor de "y" es usado para el método de Euler.
        y = y + (float(distancia_del_paso) * eval(ecuacion_diferencial))  
        x += float(distancia_del_paso) 
        print(f'{i+1}' + ' '*13 + f'{x:.1f}' + ' '*5 + f'{y:.4f}' )

    

inicial_x = retorna_un_real('Ingrese el valor inicial de x (x0): ')
inicial_y = retorna_un_real('Ingrese el valor inicial de y (y0): ')
distancia_del_paso = retorna_un_real('Ingrese el tamaño del paso (h): ')
numero_de_datos = retorna_un_entero('Ingrese el número de pasos (n): ')
ecuacion_diferencial = ingresar_ecuacion_diferencial('Ingresa la EDO en terminos de x y y (por ejemplo: y-x**2+1): ')
metodo_euler(ecuacion_diferencial, inicial_x, inicial_y, distancia_del_paso, numero_de_datos)
