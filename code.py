print("¡Bienvenido a la Aventura del Bosque Encantado!")

while True:
    print("\nTe encuentras frente a dos caminos: izquierda o derecha.")
    camino = input("¿Cuál eliges? ").lower()

    if camino == "izquierda":
        print("Te encuentras con un río. Puedes nadar o rodear.")
        accion = input("¿Qué haces? nadar/rodear: ").lower()
        if accion == "nadar":
            print("Te arrastra la corriente. ¡Fin del juego!")
        elif accion == "rodear":
            print("Encuentras un tesoro escondido. ¡Ganaste!")
        else:
            print("No hiciste nada y se hace de noche. ¡Fin del juego!")
    elif camino == "derecha":
        print("Te topas con un dragón. Puedes luchar o huir.")
        accion = input("¿Qué haces? luchar/huir: ").lower()
        if accion == "luchar":
            print("El dragón te quema con fuego. ¡Fin del juego!")
        elif accion == "huir":
            print("Escapas sano y salvo. ¡Eres un héroe!")
        else:
            print("Te quedas paralizado y el dragón te ve. ¡Fin del juego!")
    else:
        print("No elegiste un camino válido. El bosque te confunde. ¡Fin del juego!")

    replay = input("\n¿Quieres jugar de nuevo? si/no: ").lower()
    if replay != "si":
        print("¡Gracias por jugar! Hasta la próxima.")
        break

    #ññññññ