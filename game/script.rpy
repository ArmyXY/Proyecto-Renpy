# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("1")
define b = Character("2")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #Variables aquí abajo.
    default clown = False

    "Así empezo mi historia..." #No variable = pensamientos o el sistema...
    a "¡Demonios mi cabeza!"
    "Algo te golpeo tan fuerte que te tiro al suelo"
    b "¡Menuda ostia te diste!"
    "El desconocido te ayuda"
    a "Te lo agradezco..."
    b "No pasa nada, después de todo estamos encerrados..."
    "¡Mierda es verdad!"
    "Te colocas en posición defensiva"
    $ clown = False

menu:
    "¿Qué quieres de mi pervertido?":
        jump angy

    "Demonios... nunca pense que me salvaria un payaso...":
        jump clown

label angy:
    b "¡Yo no fui!"
    a "Joder..."
    a "Entonces... quien fue?"
    jump continue1

label clown:
    b "¿Cómo supistes que estaba haciendome el master de payaso?"
    "¿Existe ese puto master?"
    $ clown = True
    jump continue1

label continue1:
    if clown:
        a "¡De que cojones va esa mierda de master de payaso!"
        b "Bro... siempre quise ser payaso..."
        "..."
        jump continue2
    else:
        a "¿Y ahora que?"
        b "La verdad es que no se..."
        jump continue2
label continue2:
    "Debemos de observar nuestro entorno... ¿verdad?"
    "Esta el payaso, una cama, un hueco y una puerta cerrada..."
    $ closedd1 = True

menu:
    "Payaso":
        jump payaso
    "Cama":
        jump cama
    "Hueco en la pared":
        jump hueco
    "Puerta Cerrada":
        jump doorc

label payaso:
    b "Hey!"
    jump continue3

label cama:
    "La cama esta vacia..."
    jump continue3

label hueco:
    "El hueco esta vacio..."
    jump continue3

label doorc:
    if closedd1:
        "La puerta esta cerrada..."
        jump continue3
    else:
        "La puerta esta... abierta?"
        jump continue3

label continue3:
    return

    # This ends the game.
    #return
