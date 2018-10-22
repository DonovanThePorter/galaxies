label sans1:
define m = Character("Monika")
play music "music/monika-end.ogg"
image 3aa = "monika/3aa.png"
image 3bb = "monika/3bb.png"
image Mon17 = "monika/Mon17.png"
image Ika10 = "monika/Ika10.png"
show 3aa
init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass
m "Welcome to the super secret script!"
m "I'll be your guide in this mess of a script."
m "We're gonna add so many cool things to this game, and it starts here in the test script."
m "Feel free to mess around with shit, who cares if anything breaks here!"
m "If you want to test some code, or some kind of event, copy paste it into the script here!"
m "I'd use renpy to open the script up, and just do it now!"
#Replace this line of text with whatever you want to test (Currently using to test sprite stuff -Donovan)
$ stream_list = ["spotify.exe"]
if list(set(process_list).intersection(stream_list)):
    call stream
hide 3aa
show Mon17
m "You probably won't get to see me anymore, but that's okay!"
m "I'm fine with watching, from the code..."
m "I mean, isn't that what I've always done?"
m "..."
m "[user], what are you still doing here?"
m "..."
hide Mon17
show 3aa
m "Okay I have one more thing I can do for you."
m "But keep in mind, that this isn't even my final form."
hide 3aa
m "Here."
m "I."
m "Gooooooo!!!!"
show ok
play music "music/seinfeld.mp3"
m "Ha."
show Ika10
m "Gotcha"
jump start
label stream:
show 3bb
hide Mon17
m "Do you have Spotify open right now? Seriously? You better not be listening to music..."
m "Like come on just listen to the music in game, it's way better!"
hide 3bb
jump sound
hide 3bb
return

label sound:
hide 3bb
hide 3aa
show Ika10
m "By the way, did you know that there's a new sound test?"
m "Go into preferences, and hit the test button"
m "I think you'll like what you hear"
hide Ika10
