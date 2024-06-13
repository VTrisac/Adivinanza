def adivina(intento=1):
    respuesta = input("¿De qué color es el caballo blanco de Santiago? ")
    if respuesta != "blanco":
        if intento < 3:
            print("Fallaste! Inténtalo de nuevo")
            intento += 1
            adivina(intento)  # Llamada recursiva
        else:
            print("Perdiste! Se acabaron las oportunidades")
    else:
        print("Ganaste! Acertado en " + str(intento) + " intento(s)")


adivina()