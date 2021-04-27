def selectClass(charClass):
    baseHP = 25
    baseMP = 0
    baseAttack = 10
    baseDefense = 8
    fighterHP = 30
    fighterMP = 0
    fighterAttack = 18
    fighterDefense = 13
    charHP = 0
    charMP = 0
    charAttack = 0
    charDefense = 0
    baseStats = """
    All classes have:
    25 HP
    0 MP
    10 Attack
    8 Defense
    """
    descFighter = f"""
    The Fighter, believe it or not, is usually the most physically strong of all the class groups.
    This class usually specializes in melee attacks, whether with weapons or just plain old fists.
    This class generally has the best armor, and is the most skilled with the largest weapons. 
    High HP, attack, and defense scores.

    Stats:
    {baseHP+5} HP 
    {baseMP+0} MP
    {baseAttack+8} Attack 
    {baseDefense+5} Defense    
    """
    if userInput == 1:
        print(descFighter)
userInput = int(input('Select your class\n[1] Fighter\n> '))
if userInput == 1:
    charClass = 'Fighter'
    charHP = fighterHP
    charMP = fighterMP
    charAttack = fighterAttack
    charDefense = fighterDefense
    selectClass(1)
    print(f'Class: Fighter\n\nStats:\HP: {fighterHP}\nMP: {fighterMP}\nAttack: {fighterAttack}\nDefense: {fighterDefense}')
    satisfied = int(input('Are you satisfied?\n[1] Yes\n[2] No\n> '))