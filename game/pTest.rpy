label pTest:
    $ personality_type = "?"
    $ personality_points = 0
    define c = Character("Cthulhu")
    image cthulhu = "cthulhu.jpg"

    v "Hello, I am Cthulhu."
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
