label tch1:
define t = Character("Tiamite")
define i = ("Io")
with dissolve
i "Tia?"
i "...Tia?"
i "WAKE UP"
t "H-Huh?"
i "Tia it's time for the festival! We're gonna be late."
t "ahHH"
"Today was the day of the annual Honnis Festival."
"People from all over the city would gather around Central Honnis for food and drinks with their loved ones in celebration of the anniversary of Honnis' founding."
i "If you could wake up on time, I wouldn't have to wake you up every day..."
t "I-I'm sorry, give me 5 minutes I'll be ready in a second."
menu:

        "What should I do first"

        "Get dressed":

            jump dress

        "Brush teeth":

            jump teeth

        "Eh, who needs to get ready, I'm already late!":

            jump lazy

label dress:
    "I walk over to my closet"
#Scene change to another angle of room? Probably not unless Eli is game
    "I have a variety of shirts to wear"
    "And by that I mean 2"
menu:

        "What should I wear to the Honnis Festival? An event very important to my culture"

        "A nice button down top":

            jump classy

        "WEEABOO SHIRT":

            jump weeb

label classy:
    "I put on the shirt and prepare an entire matching outfit, it takes a while, but I manage to make it look nice."
    t "Io! I'm ready to go!"
    i "Wow, you look really nice!"
    jump festival

label weeb:
    "Who needs class when I could just wear a shirt with a bunch of chicks from my favorite moe anime."
    t "Io! I'm ready to go!"
    i "You weeb."
    jump festival
label teeth:
    t "brushy brush"

label lazy:
    t "Io wait, I'll just go in what I'm wearing now!"
label festival:
    "We walk outside, I instantly feel the heat of late spring"
#This is where I got stuck, I want different dialogue depending on what she's wearing"
