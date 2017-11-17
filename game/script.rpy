init python:
    class Place(object):
        def __init__(self, name, desc, neighbors=[]):
            self.name= name
            self.desc = desc
            self.neighbors = neighbors
            for n in self.neighbors:
                n.addneighbor(self)

        def addneighbor(self, neighbor):
            self.neighbors.append(neighbor)

    class Player(object):
        def __init__(self, name, location):
            self.name = name
            self.location = location
            
        def move(self, location):
            if location in self.location.neighbors:
                self.location = location
            else:
                print ('That Place is to far away!')

    Home = Place('Home','Place You Live')
    Forest = Place('Forest','Place to Find Wood',[Home])
    Mines = Place('Mines','Place You Get Ore',[Home,Forest])

    pc= Player('bob', Home)





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

    g "cool..."


label explore:
    'You are in [pc.location.name]'
    python:
        choice = menu([(p.name, p) for p in pc.location.neighbors])
        pc.move(choice)
        
    jump explore



    return
