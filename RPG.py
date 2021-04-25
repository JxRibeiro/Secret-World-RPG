from time import sleep
import sys
def gameStart():
    worldDescription = """
You move forward through the unfamiliar portal formed by two bended trees.
You're immediately met by a fascinating world.
Waterfalls pour into the lagoon you're standing in from high above.
Light from the orange sun peeks over and warms you gently.
The terrain's treacherous to walk on.
Who knows what dangers await to those who fall.
Even though this world's harsh you're at ease and you feel secure in this world.
This world is peaceful beyond a doubt, but with so much to discover you can't help but explore.
Not far into the distance you see parts of creatures of a literally and figuratively different world.
Even though they seem good natured, you try to avoid getting too close.
It's obvious there are lean creatures, feathered creatures, and what you think might be muscular creatures of some sort.
With some rationing your supplies should last for a while as discovery after discovery is waiting to be made.
But, with a great sense of adventure, a good sense of direction, and some resourcefulness, you know you can fulfill this opportunity with everything you have.

Welcome to The Secret World

"""
    for line in worldDescription:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0)
def charClass():
    baseStats = """
All classes have:
25 HP
0 MP
10 Attack
8 Defense
    """
    descFighter = """
    The Fighter, believe it or not, is usually the most physically strong of all the class groups.
    This class usually specializes in melee attacks, whether with weapons or just plain old fists.
    This class generally has the best armor, and is the most skilled with the largest weapons.
    High HP, attack, and defense scores.

    Stats:
    +5 HP
    +8 Attack
    +5 Defense
    """
    descMage = """
    Mages are generally typified by their lack of traditional weaponry, foregoing steel in favor of fire, ice, and other spell use.
    Mages usually wear the weakest of armor, many times clad in nothing but robes, but can also cast shield, healing, and regeneration spells.

    Stats:
    +3 HP
    +5 Attack
    +4 Defense
    +25 MP
    """
    descNecromancer = """
    This subclass, descending from a mage and warrior respectively, is dedicated to the blight and death arts.
    In games where they have their own unique identities, these classes excel at spreading disease and debuffs, while also contributing respectable DPS numbers.
    Necromancers often rely on similar stats to mages.

    Stats:
    +2 HP
    +7 Attack
    +2 Defense
    +20 MP
    """
    print('[1] Fighter')
    print('[2] Mage')
    print('[3] Necromancer')
    print(baseStats)
    userChar = int(input('Choose your class: '))
    if userChar == 1:
        print(descFighter)
        userChoice = str(input('Are going to be a fighter? (Y/N) ')).upper()
        if userChoice == 'Y':
            userChar = 'Fighter'
            cHP = 30
            cMP = 0
            cAttack = 18
            cDefense = 13
            adventure(userChar,cHP, cMP, cAttack, cDefense)
        elif userChoice == 'N':
            charClass()
            userChar = int(input('Choose your class: '))
    if userChar == 2:
        print(descMage)
        userChoice = str(input('Are going to be a mage? (Y/N) ')).upper()
        if userChoice == 'Y':
            userChar = 'Mage'
            cHP = 28
            cMP = 25
            cAttack = 15
            cDefense = 14
            adventure(userChar,cHP, cMP, cAttack, cDefense)
        elif userChoice == 'N':
            charClass()
            userChar = int(input('Choose your class: '))
    if userChar == 3:
        print(descNecromancer)
        userChoice = str(input('Are going to be a necromancer? (Y/N) ')).upper()
        if userChoice == 'Y':
            userChar = 'Necromancer'
            cHP = 27
            cMP = 20
            cAttack = 17
            cDefense = 10
            adventure(userChar,cHP, cMP, cAttack, cDefense)
        elif userChoice == 'N':
             charClass()
             userChar = int(input('Choose your class: '))
def adventure(userChar,cHP, cMP, cAttack, cDefense):
    print(f'Welcome {userChar}. Take a look on your stats:')
    print(f'HP {cHP}\nMP {cMP}\nAttack {cAttack}\nDefense {cDefense}')
gameStart()
charClass()
