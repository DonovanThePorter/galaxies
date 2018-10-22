label splashscreen:
    scene black
    with Pause(1)

    play music "music/firefly.ogg"

    show text "secret script is now enabled by typing your name as Monika" with dissolve
    with Pause(2)

    hide text with wipeleft
    with Pause(1)

    return

    define v = Character("Mysterious Voice", color="#c8ffc8")
    define t = Character("Tiamite")
    define i = ("Io")
    scene black

label start:

    scene bg room

    play music "music/reality.mp3"

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
        v "Wow I bet you think you're so funny not putting in a name..."
        v "Try again bub."
        jump start2

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
        v "That's a cool name!"

    if player_name == "Hunter":
        $ player_name="Hunter"
        v "That's a cool name!"

    if player_name == "Maki":
        $ player_name="Maki"
        v "That's a really pretty name!"

    if player_name == "Monika":
        $ player_name="Monika"
        v "I like that name."
        jump sans1

    v "You know what, I just decided I don't care what your name is."
    v "Just pick someone to play as."
#EVENTUALLY THIS WILL BE REPLACED WITH THE PERSONALITY TEST
label menu1:
menu:

        "Pick your Protagonist"

        "Tiamite":

            jump tiamite

        "Calem":

            jump calem
label sans:
        v "Wanna have a bad time?"
        jump sans1
        return

label tiamite:
        v "Ah yes, Tia, from Honnis!"
        v "Well enjoy the game!!"
        jump tch1
label calem:
        stop music fadeout 5.0
        v "Hey I wrote some of Calems story, ya wanna see?"
        v "Here it comes..."
        image ok = "ok.png"
        show ok
        play music "music/seinfeld.mp3"
        v "Gotcha."
        return
#Need a transition from Intro to both protagonists. Also need to decide when to split scripts
#We want more than one script so the game doesn't take ages too load. A la DDLC

label start2:

    scene bg room

    v "Hello There!!"
    v "Welcome to the World of Palopia!!"
    v "Who am I?"
    v "..."
    v "Don't worry about that."
    v "Why don't you tell me who YOU are?"
    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()
label name2:

    if player_name == "":
        $ player_name="xXCoolPal123Xx"
        play music "music/reality-flat.ogg"
        v "Okay seriously???"
        v "Don't do that again, or else!"
        jump start3

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
        v "That's a cool name!"

    if player_name == "Hunter":
        $ player_name="Hunter"
        v "That's a cool name!"

    if player_name == "Maki":
        $ player_name="Maki"
        v "That's a really pretty name!"

    if player_name == "Monika":
        $ player_name="Monika"
        v "I like that name."
        jump sans1

    v "You know what, I just decided I don't care what your name is."
    v "Just pick someone to play as."
    jump menu1

label start3:

    scene bg room

    v "..."
    v "Why don't you just tell me your name..."
    v "I mean, I already have a feeling it's [user]"
    v "I'm just giving you a chance to go by something else"
    $ player_name = renpy.input("TELL ME YOUR NAME ALREADY")

    $ player_name = player_name.strip()
label name3:

    if player_name == "":
        $ player_name="dummy dum dum"
        v "You know what, I just decided I don't care what your name is."
        v "Just pick someone to play as."
        jump menu1

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
        v "That's a cool name!"

    if player_name == "Hunter":
        $ player_name="Hunter"
        v "That's a cool name!"

    if player_name == "Maki":
        $ player_name="Maki"
        v "That's a really pretty name!"

    if player_name == "Monika":
        $ player_name="Monika"
        v "I like that name."
        jump sans1

    v "You know what, I just decided I don't care what your name is."
    v "Just pick someone to play as."
    jump menu1
