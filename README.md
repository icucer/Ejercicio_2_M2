# Crear programa en Python que solicite al usuario:
## 1) Ingresar un numero entero cualquiera del 1 al 9.
## 2) Luego solicitar que ingrese números secuenciales partiendo por 1 pero saltándose aquellos que sean múltiplos del valor ingresado al comienzo, en caso de ingresar un valor erróneo, enviar un mensaje indicando el error y el número que correspondería ingresar.
***
## A continuacion dejare algunos fragmentos del codigo donde se explica el funccionamiento ya que los commentarios complica mucho la lectura del codigo:
***
- 1) Dentro del ciclo 'while', insertaremos una estructura 'if' para verificar que el número ingresado no sea menor que 1 ni mayor que 9. Si alguna de las dos condiciones se cumple, imprimirá un mensaje de error.
```
    if num_inicial < 1 or num_inicial > 9:
        print ("\nError, ingrese un numero valido de 1 a 9\n")
```
***
- 2) Con la estructura condicional elif, verificaremos si el número ingresado es igual a 1. En este caso, mostraremos un mensaje en pantalla indicando que el juego ha terminado, ya que el 1 es múltiplo de todos los demás números.
```
    elif num_inicial == 1:
        print (f"\nJuego termino ya que todos los números son múltiplo de {num_inicial}.")
```
***
- 3) Y, por último, si no se cumple ninguna de las condiciones anteriores, con la estructura 'else' le pediremos al usuario que ingrese los números secuenciales comenzando por el 1, evitando ingresar los múltiplos del número seleccionado al inicio.
```
    else:
        print ("\nIngresa números secuenciales partiendo por el 1 evitando")
        print ("ingresar los múltiplos del número seleccionado en el principio.")
```
***
- 4) Con el siguiente ciclo 'while', le pedimos al usuario que ingrese el número secuencial, y además, con las estructuras condicionales dentro del bucle, controlaremos los números secuenciales ingresados.
```
        while 0 < var_apoyo < 10:
            num_secuencial = int(input("\nIngresa número secuencial:\n"))
```
***
- 5) Si el usuario ingresa algún múltiplo del número seleccionado al principio, con la estructura 'if' haremos que se imprima por pantalla un mensaje. Le diremos que ha cometido un error y que el número que ingresó es un múltiplo del número seleccionado al principio. Además, le indicaremos que debe ingresar otro número e indicaremos cuál es ese número.
```
                if num_secuencial % num_inicial == 0:
                    print(f"\nError, el numero {num_secuencial} es multiplo de {num_inicial} debes ingresar {var_apoyo}.\n")
```