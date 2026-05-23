import random

# Arrancamos asignando valores

dificultad = None
numero = None
cont_facil = 0
cont_media = 0
cont_dificil = 0

# Empezamos con el bucle while para el juego

while dificultad != 4:
    print("Juego del Numero Secreto, Adivinalo!")

    print("-----------------------------------------------------------------------")

    print("Facil: 1\nMedia: 2\nDificil: 3\nSalir: 4")

    print("-----------------------------------------------------------------------")
    dificultad = int(input("Ingrese la dificultad elegida: "))
    # A continuacion empezamos con comparaciones segun la dificultad elegida
    if dificultad == 1:
        print("Elegiste la dificultad facil es adivinar un numero del 0 al 10!!")
        print("-----------------------------------------------------------------------")
        # Asignamos un valor random al numero a adivinar
        numero_secreto = random.randint(0,10)
        numero = None
        cont_facil = 0
        while numero != numero_secreto:
            # Empezamos preguntandole el numero que quiere elegir
            numero = int(input("Ingrese un numero del 0 al 10: "))
            if 0 <= numero <= 10:
                cont_facil += 1
                # Mensaje cuando adivine el numero
                if numero == numero_secreto:
                    print("Pasaste la dificultad facil!!")
                    print(f"Lo hiciste en {cont_facil} intentos!")
                    break
                # Le damos un poco de pistas para que se le haga mas facil
                elif numero > numero_secreto:
                    print("Un numero menor")
                elif numero < numero_secreto:
                    print("Un numero mayor")
            else:
                print("Es solo un numero del 0 al 10!!")
    # Otra vez el mismo ciclo nada mas que con la dificultad media
    elif dificultad == 2:
        print("Elegiste la dificultad media es adivinar un numero del 0 al 50!!")
        print("-----------------------------------------------------------------------")
        numero_secreto = random.randint(0,50)
        numero = None
        cont_media = 0
        while numero != numero_secreto:
            numero = int(input("Ingrese un numero del 0 al 50: "))
            if 0 <= numero <= 50:
                cont_media += 1
                if numero == numero_secreto:
                    print("Pasaste la dificultad media!!")
                    print(f"Lo hiciste en {cont_media} intentos!")
                    break
                elif numero > numero_secreto:
                    print("Un numero menor")
                elif numero < numero_secreto:
                    print("Un numero mayor")
            else:
                print("Es solo un numero del 0 al 50!!")
    elif dificultad == 3:
        print("Elegiste la dificultad dificil es adivinar un numero del 0 al 100!!")
        print("-----------------------------------------------------------------------")
        numero_secreto = random.randint(0,100)
        numero = None
        cont_dificil = 0
        while numero != numero_secreto:
            numero = int(input("Ingrese un numero del 0 al 100: "))
            if 0 <= numero <= 100:
                cont_dificil += 1
                if numero == numero_secreto:
                    print("Pasaste la dificultad dificil!!")
                    print(f"Lo hiciste en {cont_dificil} intentos!")
                    break
                elif numero > numero_secreto:
                    print("Un numero menor")
                elif numero < numero_secreto:
                    print("Un numero mayor")
            else:
                print("Es solo un numero del 0 al 100!!")
    # A continuacion ponemos por si el usuario quiere salir un break para terminar el bucle while asi no imprime nada mas
    elif dificultad == 4:
        break
    # Lo proximo que vemos es por si el usuario no pone las dificultades elegidas o para salir
    else:
        print("Es solo las dificultades elegidas")