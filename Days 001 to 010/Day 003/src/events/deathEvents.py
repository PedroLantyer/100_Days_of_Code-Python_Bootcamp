import random
from datetime import *
from events.generateDrawings import *

def landDeath(pissedOffNarator=False):
    random.seed(datetime.now().timestamp())
    deathCause = random.randint(1,100)
    print()
    
    if(pissedOffNarator):
        drawSoldierBoy()
        print("Soldier Boy shows up and bashes your skull in")
        print("GAME OVER")
        exit(0)

    match deathCause:
        case deathCause if deathCause >= 1 and deathCause < 30 :
            gordonRamsay()
            print("You f****** donkey, the meat's f****** raw!")
            print("Gordon Ramsey continues to screen as he chops you into pieces")
        case deathCause if deathCause >= 30 and deathCause < 60:
            drawRheaRipley()
            print("Rhea Ripley is here, prepare your cheeks, because Mami is about to give a whole new meaning to the words Monday Night RAW")
        case deathCause if deathCause >= 60 and deathCause <= 99:
            drawDeathBySnuSnu()
            print("You get captured by the Amazons. DEATH BY SNU SNU")
        case _:
            drawHandsomeJack()
            print("Handsome Jack hit you with a Hyperion Moonshot Cannon")
               
    print("GAME OVER")
    exit(0)

def seaDeath(pissedOffNarator=False):
    random.seed(datetime.now().timestamp())
    deathCause = random.randint(1,100)
    print()

    if(pissedOffNarator):
        drawCthulhu()
        print("Cthulhu drags you into the lost city of R'lyeh")
        print("GAME OVER")
        exit(0)

    match deathCause:
        case deathCause if deathCause >= 1 and deathCause < 30:
            drawShark()
            print("You get mauled by a bull shark")
        case deathCause if deathCause >= 30 and deathCause < 60:
            drawKraken()
            print("You get swallowed by the kraken")
        case deathCause if deathCause >= 60 and deathCause <= 99:
            drawMurmaider()
            print("You get attacked by Murmaider")
        case _:
            drawCthulhu()
            print("Cthulhu drags you into the lost city of R'lyeh")
               
    print("GAME OVER")
    exit(0)

def doorDeath(pissedOffNarator=False):
    random.seed(datetime.now().timestamp())
    deathCause = random.randint(1,100)
    print()

    if(pissedOffNarator):
        drawLoona()
        print("The door is actually the gates of hell. And unfortunately for you dear furry, Loona isn't here")
        print("GAME OVER")
        exit(0)

    match deathCause:
        case deathCause if deathCause >= 1 and deathCause < 30:
            print("It's a room full of fire.")
        case deathCause if deathCause >= 30 and deathCause < 60:
            drawCthulhu()
            print("An eldritch abomination drags you in")
        case deathCause if deathCause >= 60 and deathCause <= 99:
            drawJohnWick()
            print("John Wick is on the other side of the door, and he thinks you killed his dog")
        case _:
            drawLoona()
            print("The door is actually the gates of hell. And unfortunately for you dear furry, Loona isn't here")
               
    print("GAME OVER")
    exit(0)
