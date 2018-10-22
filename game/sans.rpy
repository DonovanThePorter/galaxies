label sans1:
define m = Character("Monika")
play music "music/monika-end.ogg"
image 3aa = "monika/3aa.png"
image 3bb = "monika/3bb.png"
image Mon17 = "monika/Mon17.png"
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
$ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
if list(set(process_list).intersection(stream_list)):
    call stream
hide 3aa
show Mon17
m "You probably won't get to see me anymore, but that's okay!"
m "I'm fine with watching, from the code..."
m "I mean, isn't that what I've always done?"
m "..."
m "[player_name], what are you still doing here?"

label stream:
show 3bb
hide Mon17
m "Penis breath"
