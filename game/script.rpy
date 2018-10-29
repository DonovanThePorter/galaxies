#This script handles this splashscreens, introduction, and personality test.
label splashscreen:
    scene black
    with Pause(1)
    image ok = "ok.png"
    play music "music/firefly.ogg"

    $ randomnum = renpy.random.randint(1, 4) # (randomize between 1 and 4)

    if randomnum ==1:
        show text "Pal Studios Presents" with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum ==2:
        show text "Monika died for this" with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum ==3:
        show text "Attention Gamers..." with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum ==4:
        show ok with dissolve
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
        v "Are you a fan of Salad and Doritoes?"

    if player_name == "Ant":
        $ player_name="Ant"
        v "Squish it!"

    if player_name == "Eli":
        $ player_name="Eli"
        v "That's a cool name!"

    if player_name == "Hunter":
        $ player_name="Hunter"
        v "Praise Lord Cthulhu!"

    if player_name == "Credits":
        $ player_name="Credits"
        jump credits

    if player_name == "Maki":
        $ player_name="Maki"
        v "That's a really pretty name!"

    if player_name == "Umi":
        $ player_name= "Umi"
        v "Thank you for becoming the best waifu to exist"

    if player_name == "Lilina":
        $ player_name= "Lilina"
        v "She's REALLY hot"
    if player_name == "Felicia":
        $player_name= "Felicia"
        v "WE GOT TROUBLE!!!!"
        jump splashscreen

    if player_name == "Restart":
        $ player_name="Restart"
        jump splashscreen

    if player_name == "Monika":
        $ player_name="Monika"
        v "I like that name."
        jump sans1

    v "You know what, I just decided I don't care what your name is."
    v "Just take this cool quiz"
#EVENTUALLY THIS WILL BE REPLACED WITH THE PERSONALITY TEST
label pTest:
    $ personality_type = "?"
    $ personality_points = 0
    define c = Character("Cthulhu")
    image cthulhu = "cthulhu.jpg"

    v "Hey so instead of another script I just put everything in here weeee"
    show cthulhu at truecenter
    with dissolve

    jump q1

label q1:
    menu:
        v "You have a difficult test next week, what do you do?"

        "Prepare by studying.":
            $ personality_points +=1
            v "Responsible are we?"
            jump q2

        "I can study later, I have other priorities":
            v "Time management is important for success."
            jump q2

        "Eh, who cares about some test, I'd rather watch anime!":
            $ personality_points -=1
            v "Good taste."
            jump q2

label q2:
    menu:
        v "What is your favorite color?"

        "Blue":
            $personality_points +=1
            v "Wow, you are so basic."
            jump q3

        "I like them all":
            v "Indecisive are we?"
            jump q3

        "Death":
            $personality_points -=1
            v "Whoa there, we're not even 5 minutes in, what are you trying to do?"
            jump q3

label q3:
    menu:
        v "What type of music is best?"

        "Jazz":
            $personality_points +=1
            v "I'm glad ya like jazz"
            jump q4

        "Pop":
            v "Insert response here"
            jump q4

        "Death Metal":
            $personality_points -=1
            v "aaaa"
            jump q4

label q4:
    menu:
        v "You find a wallet outside of a building, what do you do?"

        "Turn it in, it's probably really important":
            $personality_points +=1
            v "I'm glad ya like jazz"
            jump q5

        "Leave it, I'm sure someone will come back for it.":
            v "Insert response here"
            jump q5

        "Ayyy free spending money":
            $personality_points -=1
            v "aaaa"
            jump q5
label q5:
    menu:
        v "What's your opinion on puns?"

        "Humor is subjective, end quiz please.":
            $personality_points +=1
            v "I'm glad ya like jazz"
            jump score

        "They're punbearable":
            v "Insert response here"
            jump score

        "I don't like where this is going, can I get a refund on this game?":
            $personality_points -=1
            v "aaaa"
            jump score
label score:
    "Your score is:" "[personality_points]"
    if personality_points < 0:
        jump calem
    else:
        jump tiamite
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
        hide image cthulhu
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
