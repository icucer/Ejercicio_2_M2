# Encabezado y nombre del programa.
print ("\n ********************")
print ("*  Juego de numeros  *\n")
print (" ********************\n")

# Creación de variables y asignación de valores.
num_inicial = 0
num_secuencial = 0
var_apoyo = 1

# Ciclo while que controlara la recepción del número inicial. 
while num_inicial < 1 or num_inicial > 9:
    num_inicial = int(input("Ingresa un numero entero de 1 a 9:\n"))

    # 1) para el funcionamiento revisar README.md
    if num_inicial < 1 or num_inicial > 9:
        print ("\nError, ingrese un numero valido de 1 a 9\n")

    # 2) para el funcionamiento revisar README.md
    elif num_inicial == 1:
        print (f"\nJuego termino ya que todos los números son múltiplo de {num_inicial}.")
    
    # 3) para el funcionamiento revisar README.md
    else:
        print ("\nIngresa números secuenciales partiendo por el 1 evitando")
        print ("ingresar los múltiplos del número seleccionado en el principio.")

        # 4) para el funcionamiento revisar README.md
        while 0 < var_apoyo < 10:
            num_secuencial = int(input("\nIngresa número secuencial:\n"))

            # Con el if controlaremos que el usuario no se salte los números
            # y también que no ingrese los múltiplos del número seleccionado al inicio.
            if num_secuencial == var_apoyo and num_secuencial % num_inicial != 0:
                var_apoyo += 1

                # con el if a continuación controlamos que se salte el múltiplo.
                if var_apoyo % num_inicial == 0:
                    var_apoyo += 1 # la siguiente variable es un contador para el while
            
            # En el else se quedan las excepciones:
            else:
                
                # 5) para el funcionamiento revisar README.md
                if num_secuencial % num_inicial == 0:
                    print(f"\nError, el numero {num_secuencial} es multiplo de {num_inicial} debes ingresar {var_apoyo}.\n")

                # De otra forma queda que el usuario se equivocó de número se saltó alguno
                # en este caso se imprimirá por pantalla un mensaje de error y el número que tenía que ingresar.
                else:
                    print (f"\nError, tienes que ingresar el numero: {var_apoyo}.\n")
                break # Es la instrucción que si llega a este punto que se salga din el ciclo while.

# Y sin importar el caso de toda forma se imprimirá en pantalla
# la invitación que lo intente nuevamente y agradecimientos.
print (f"\nIntenta nuevamente, gracias por preferirnos\n")