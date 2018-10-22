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
    $ classy = True
    $ weeb = False
    "I put on the shirt and prepare an entire matching outfit, it takes a while, but I manage to make it look nice."
    t "Io! I'm ready to go!"
    i "Wow, you look really nice!"
    jump festival

label weeb:
    $ weeb = True
    $ classy = False
    "Who needs class when I could just wear a shirt with a bunch of chicks from my favorite moe anime."
    t "Io! I'm ready to go!"
    i "You weeb."
    jump festival
label teeth:
    t "brushy brush"
    jump festival
label lazy:
    t "Io wait, I'll just go in what I'm wearing now!"
    i "Pajamas?"
    t "Oh yeah, probably not the best idea"
    i "Especially considering how important this Honnis Festival is, seeing as we're of age"
    t "Yeah... Alright I'll get dressed."
    jump dress
label festival:
    play music "music/seinfeld.mp3"
    "May 14th, it's Honnis Day alright"
    "As we walk outside, I instantly feel the heat of late spring"
    t "Ugh, does this have to be today?"
    i "I mean, we'll be 22 next year, 21 is the only time this can be special."
    t "I know but, I'd rather just stay at home and..."
    if weeb:
        i "Watch anime?"
        t "Yeah! Look at how cute this girl is on my shirt!"
        i "You weeb."
        jump festival2
    if classy:
        i "Look for another job?"
        t "Yeah! I hate serving food, I want to get out there and play music already!"
        jump festival2
label festival2:
    i "Ya still looking for a way to play that piano thing?"
    t "It's not a piano thing!"
#This is where I got stuck, I want different dialogue depending on what she's wearing"
