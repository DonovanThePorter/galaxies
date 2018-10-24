label pTest:
    $ personality_type = "?"
    $ personality_points = 0
    define c = Character("Cthulhu")
    image cthulhu = "cthulhu.jpg"

    c "Hello, I am Cthulhu."
    show cthulhu at truecenter
    with dissolve

    jump q1

label q1:
    menu:
        c "What brings you to my domain?"

        "The neverending quest for true friendship":
            $ personality_points +=1
            c "Eww. I don't make friends with puny mortals."
            jump q2

        "Nothing, just browsing":
            c "Oh, you heard about the open house?"
            jump q2

        "I want to kill you!":
            $ personality_points -=1
            c "Ha, you wish!"
            jump q2

label q2:
    menu:
        c "What is your favorite color?"

        "Blue, duh":
            $personality_points +=1
            c "Wow, you are so basic."
            jump score

        "I like them all":
            c "Fukin figget"
            jump score

        "Death":
            $personality_points -=1
            c "Jesus, and people say I'm evil"
            jump score


label score:
    "Your score is:" "[personality_points]"
