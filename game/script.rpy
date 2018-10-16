label splashscreen:
    scene black
    with Pause(1)

    show text "Pal Studios Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

    define v = Character("Mysterious Voice", color="#c8ffc8")
    scene black

label start:

    scene bg room

    v "Hello There!"
    v "Welcome to the World of Palopia!!"
    v "Who am I?"
    v "..."
    v "Don't worry about that."
    v "Why don't you tell me who YOU are?"
    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Undecided"

    v "Pleased to meet you, %(player_name)s!"
    v "You know what, I just decided I don't care what your name is."
    v "Just pick someone to play as."
menu:

    v    "Pick your Protagonist"

    "Tiamite":

            jump tiamite

        "Calem":

            jump calem
return

    label tiamite:
        v "Ah yes, Tia, from Honnis!"
        v "Well enjoy the game!!"

        return

    label calem:
        v "Hmmm, Interesting pick..."
        v "Well enjoy the game!!"
