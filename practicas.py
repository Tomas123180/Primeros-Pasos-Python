import math
# Vamos a importar math para tener variables mas precisas, como el numero pi que sea mas preciso
nombre = input("Cual es tu nombre?: ")
# Pedimos al usuario que diga cual es su nombre
# A continuacion voy a ensamblar una serie de preguntas utilizando el if
nombre = nombre.title()
# Aca usamos el nombre.title para hacer que la primera letra del nombre sea mayuscula y asi sea mas presentable
print(f"Hola {nombre}")
numero_radio = float(input("Indique un radio en cm para calcular el area: "))
# Aca le pedimos al usuario que diga un numero para calcular el area
area = numero_radio ** 2 * math.pi
# Se este es el calculo del area del circulo
print(f"El area calculada es = {area:.2f}cm²")
# Aca imprimimos el resultado para que el usuario pueda ver
# Para el input usamos el float para que el usuario pueda introducir decimales
# Tambien al final del {Area} podemos escribir :.2f que es para que muestre solo 2 decimales de resultado y el numero no sea tan largo
# Uno de los ejercicios pedidos de la unidad 
pregunta = input("Quieres calcular tambien el perimetro? (Si/No): ")
# Le preguntamos al usuario si quiere calcular el perimetro
if pregunta.lower() == "no":
    print("Esta bien que tengas un lindo dia")
# Aca vemos que respuesta tiene el usuario, siempre ponemos el .lower para ponerlo todo en minuscula en caso de que escriba "NO" en mayuscula se lo toma igual}
elif pregunta.lower() == "si":
    perimetro = 2 * math.pi * numero_radio
    print(f"El Perimetro es: {perimetro:.2f}cm")
# El elif es para calcular otra respuesta de la variable
else:
    print("Por favor Indique Si/No")
# Como ya pusimos todas las respuesta el else sirve que en caso de que no ponga la respuesta del Si/No, el usuario no se quede con la duda de porque no funciono
pregunta = input("Quieres hacer otras preguntas? (Si/No): ")
# Vamos a armar una serie de preguntas por si quiere saber mas cosas, porque uso el mismo nombre?, simple la variable se reemplaza por lo que responda
pregunta = pregunta.lower()
if pregunta == "si":
    print("A continuacion tenes estas opciones")
# Podes usar dentro del print \n para separar entre lineas pero yo simplemente voy a repetir el print
    print("1 = Preguntar sobre si sos mayor de edad en argentina")
    print("2 = Preguntar sobre que hacer en caso de lluvia")
    print("3 = Preguntar como hacer fideos")
    print("4 = Preguntar la suma de dos numeros")
# Aca ya terminamos de poner opciones
    opcion = int(input("Que opcion queres efectuar?: "))
# Aca ponemos int para que solo sea un numero entero ya que no se necesita poner decimales
    if opcion == 1:
        edad = int(input("Coloque su edad: "))
        if edad >= 18:
            print("Eres mayor de edad")
        elif edad < 0:
            print("Pon una edad en numeros positivos")
        else:
            print("Eres menor")
# Aca explicare una por una basicamente al principio pregunta la edad y despues compara la edad con valores.
# Al poner >= explica que si la edad es mayor o igual a 18 es mayor de edad
# Al poner elif edad < 0 indica que si pueden poner numeros negativos pero esta mal
# Al ya descartar todas las opciones posible el else significa que si o si es menor
    elif opcion == 2:
        lluvia = input("Llueve? (Si/No): ")
        if lluvia.lower() == "no":
            print("Entonces puede salir")
        elif lluvia.lower() == "si":
            print("Llevar paraguas")
        else:
            print("Indicar Si/No")
# Aca mas o menos es lo mismo que lo anterior
    elif opcion == 3:
        print("Preparar la masa\nEstirar la masa\nCortar los fideos\nDejar secar\nCocinarlos")
    elif opcion == 4:
        numero1 = float(input("Elija un numero: "))
        numero2 = float(input("Elija el otro numero: "))
        suma = numero1 + numero2
        print(f"La suma entre estos numeros es {suma}")
    else:
        print("Por favor elija la opcion correcta")
# Y por aca vemos bien como se hace una serie de preguntas
elif pregunta == "no":
    print("Entiendo, siga con su dia")
else:
    print("Por favor colocar Si/No")