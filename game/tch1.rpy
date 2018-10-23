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
    t "Oh crap I just got toothpaste all over my shirt"
    t "I was gonna go out in this but I'll change I guess"
    jump dress
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
    i "I mean, we'll be 19 next year, 18 is the only time this can be special."
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
    t "It's not a piano thing! It's actually a very unique instrument"
    i "No it's just a piano with a tube, same thing"
    t "Maybe if you actually listened to me play every once and a while you'd know why it's special."
    i "I'm sorry, I'm always busy with work so I can never make it out to see you."
    t "Well, I have a performance at the festival with INSERT CHARACTERS NAME HERE so you'll have to hear me."
    i "Then I'll be sure to look forward to it, where are they anyway?"
    t "They said that they would meet me by the tree by the parking lot, but I don't see the over there."
    i "Probably forgot about ya"
    t "D-Don't say that! I'd hate them forever if they played without me!!"
    "Phone ringing noises"
    i "Oh hey that's my cousin, he's supposed to be visting with a few of his friends, I'll have to catch up to you."
    t "Oh okay, I'll wait here for the group then. See ya."
    "..."
    #SOME SORT OF PASSAGE OF TIME IDK 
