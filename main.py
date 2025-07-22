import random

def verificar_palabra(palabra_secreta, intento):

    resultado = []

    if intento == palabra_secreta:
        print("Ganaste")
        for i in range(len(palabra_secreta)):
            resultado.append("🟩")
        return resultado  

    for i in range(len(palabra_secreta)):
        if intento[i] == palabra_secreta[i]:
            resultado.append("🟩")

        elif intento[i] in palabra_secreta:
            resultado.append("🟨")

        else:
            resultado.append("⬜️")

    print("".join(resultado))
    return resultado

def play():
    print("🃏 Bienvenido a Wordle!")
    opciones = ['REACT', 'MANGO', 'PATIO', 'CORRAL', 'ARBOL', 'SANCO']
    palabra_secreta = random.choice(opciones)
    longitud_palabra_secreta = len(palabra_secreta)
    intentos = 6

    print(f"La longitud de la palabra misteriosa es {longitud_palabra_secreta} 🙈")

    print("🟩 = Letra correcta y posicion correcta.")
    print("🟨 = Letra correcta y posicion incorrecta.")
    print("⬜️ = Letra incorrecta. (No esta en la palabra).")

    print("-" * 40)

    for intento_numero in range(intentos):

        while True: # No es una mala idea.

            intento = input("\nHola cual es la palabra que quieres probar? 🤠\n")

            if len(intento) != longitud_palabra_secreta:
                print(f"La palabra debe tener {longitud_palabra_secreta} letras.")
                continue

            if not intento.isalpha():
                print("La palabra solo debe contener letras.")
                continue

            intento = intento.upper() # La volvemos mayuscula
            break

        resultado = verificar_palabra(palabra_secreta, intento)

        if all( letra == "🟩" for letra in resultado ):
            print("🎉 Felicitaciones haz ganado!")
            return True
    
    print("Se acabaron los intentos 😭")
    return False

play()