from events.deathEvents import *
import random


def getNarratorWrongPath(iterCount: int, stage: int):
    if(iterCount == 50):
        print("Bloody hell I'm sick of you, you know what how about this")
        match stage:
            case 1:
                landDeath(pissedOffNarator=True)
            case 2:
                seaDeath(pissedOffNarator=True)
            case _:
                doorDeath(pissedOffNarator=True)
    
    random.seed(datetime.now().timestamp())
    deathCause = random.randint(1,100)
    print()

    match deathCause:
        case deathCause if deathCause >= 1 and deathCause < 20:
            print("Yeah buddy, that's not a valid option, how about we try again")
        case deathCause if deathCause >= 20 and deathCause < 30:
            print("Not exactly the smart type are ya kid? Try something else")
        case deathCause if deathCause >= 30 and deathCause < 50:
            print("Hm, nope can't do mate")
        case deathCause if deathCause >= 50 and deathCause < 70:
            print("Oi, that's not a valid option")
        case deathCause if deathCause >= 70 and deathCause < 90:
            print("NOPE")
        case deathCause if deathCause >= 90 and deathCause <= 99:
            print("What about no?")
        case _:
            print("You know kid, I was going to say you are the dumbest person I've ever met, but I've worked with Vince Russo")