image Home= im.Scale("forest.png", 1280, 720)

define b = Character("Azule")
 
define g = Character("Alex", who_color="#498bf4") 

image Azule= im.Scale("Azule.png", 380, 630)

define pov = Character('[player]', who_color="#00600b")



label start:

    play music "Noise.mp3"

    scene Home

    #show Azule

    "{size=+20}Welcome,{/size}"

    "{size=+20}{cps=20}This is Azule....{/cps}{/size}"

    "{size=+20}{cps=20}Your new home...{/cps}{/size}"

    with fade

    g "{size=+10}{cps=30}Hi, I'm Alex, the owner of this here village{/cps}{/size}"

    g "{size=+10}{cps=20}what's your name?{/cps}{/size}"

    python:
        while True:
            player = renpy.input(_('enter your name'))
            player = player.strip()

            if player:
                break

    pov "[player]"

    g "Nice!..."

    g ""

    g "cool..."
    g "cool..."
#498bf4


    return
