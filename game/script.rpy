label splashscreen:
    scene black
    with Pause(1)

    show text "aaaah" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

    define v = Character("Mysterious Voice", color="#c8ffc8")
    define t = Character("Tiamite")
    define i = ("Io")
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

#If player inputs a certain name, it'll trigger a funny message
label name:

    if player_name == "":
        $ player_name="xXCoolPal123Xx"
        v "Too lazy to put something in? Fine, I could come up with a name for ya."

    if player_name == "Donovan":
        $ player_name="Donovan"
        v "That's a cool name!"

    if player_name == "Anthony":
        $ player_name="Anthony"
        v "That's a cool name!"

    if player_name == "Ant":
        $ player_name="Ant"
        v "That's a cool name!"

    if player_name == "Eli":
        $ player_name="Eli"
        v "That's a better name than Donovan!"

    if player_name == "Hunter":
        $ player_name="Hunter"
        v "That's a cool name!"

    if player_name == "Maki":
        $ player_name="Maki"
        v "That's a really pretty name!"

    v "You know what, I just decided I don't care what your name     is."
    v "Just pick someone to play as."
#EVENTUALLY THIS WILL BE REPLACED WITH THE PERSONALITY TEST
menu:

        "Pick your Protagonist"

        "Tiamite":

            jump tiamite

        "Calem":

            jump calem

        "sans":

            jump sans
label sans:
        v "Wanna have a bad time?"
        return

label tiamite:
        v "Ah yes, Tia, from Honnis!"
        v "Well enjoy the game!!"
        jump tiamite1
label calem:
        v "Hmmm, Interesting pick..."
        v "Well enjoy the game!!"
#Need a transition from Intro to both protagonists. Also need to decide when to split scripts
#We want more than one script so the game doesn't take ages too load. A la DDLC
label tiamite1:
        i "Tia?"
        i "...Tia?"
        i "WAKE UP"
        t "H-Huh?"
        i "Tia it's time for the festival! We're gonna be late."
        t "ahHH"
        "Today was the day of the annual Honnis Festival."
        "People from all over the city would gather around downtown Honnis for food and drinks with their loved ones in celebration of the anniversary of Honnis' founding."
        i "If you could wake up on time, I wouldn't have to wake you up every day..."
        t "I-I'm sorry, give me 5 minutes I'll be ready in a second."
