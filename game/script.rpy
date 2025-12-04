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

    "Así empezo mi historia" #No variable = pensamientos o el sistema...
    a "¡Demonios mi cabeza!"
    "Algo te golpeo tan fuerte que te tiro al suelo"
    b "Vas ha seguir durmiendo o me pasas la botella"
    a "¡Me golpeaste con una puta botella!"
    b "Sip... estaba haciendo un video trendy..."
    "Puto retrasado mental..."
    default clown = False
menu:
    "¿Eres retrasado o te lo haces?":
        jump angy

    "Puto payaso...":
        jump clown

label angy:
    b "Te me relajas... el retardado eres tu"
    a "Puto retardado..."
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
        "Ya lo eres puto retardado..."
        jump continue2
    else:
        a "Aquí tienes tu botella puta rata..."
        b "Lo agradezco puto quejica"
        jump continue2
label continue2:
    "Fin"
    return
    # This ends the game.

    return
