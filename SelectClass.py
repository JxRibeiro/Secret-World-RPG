from openpyxl import load_workbook
from time import sleep
import os
def _cls():
    os.system('cls' if os.name=='nt' else 'clear')

book = load_workbook(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
sheet = book.get_sheet_by_name("UserClass")
cFighter = sheet['A2'].value
cMage = sheet['A3'].value
cNecro = sheet['A4'].value
HPFighter = sheet['B2'].value
HPMage = sheet['B3'].value
HPNecro = sheet['B4'].value
MPFighter = sheet['C2'].value
MPMage = sheet['C3'].value
MPNecro = sheet['D3'].value
AttFighter = sheet['D2'].value
AttMage = sheet['D3'].value
AttNecro = sheet['D4'].value
DefFighter = sheet['E2'].value
DefMage = sheet['E3'].value
DefNecro = sheet['E4'].value
FighterDescription = f"""
Fighter

The Fighter, believe it or not, is usually the most physically strong of all the class groups.
This class usually specializes in melee attacks, whether with weapons or just plain old fists.
This class generally has the best armor, and is the most skilled with the largest weapons.
High HP, attack, and defense scores.

Stats:
HP: {HPFighter}
MP: {MPFighter}
Attack: {AttFighter}
Defense: {DefFighter}
"""
MageDescription = f"""
Mage

Mages are generally typified by their lack of traditional weaponry, foregoing steel in favor of fire, ice, and other spell use.
Mages usually wear the weakest of armor, many times clad in nothing but robes, but can also cast shield, healing, and regeneration spells.

Stats:
HP: {HPMage}
MP: {MPMage}
Attack: {AttMage}
Defense: {DefMage}
"""
NecromancerDescription = f"""
Necromancer
This subclass, descending from a mage and warrior respectively, is dedicated to the blight and death arts.
In games where they have their own unique identities, these classes excel at spreading disease and debuffs, while also contributing respectable DPS numbers.
Necromancers often rely on similar stats to mages.

Stats:
HP: {HPNecro}
MP: {MPNecro}
Attack: {AttNecro}
Defense: {DefMage}
"""
def SelectClass():
    print('Available classes:\n[1] Fighter\n[2] Mage\n[3] Necromancer')
    userClass = int(input('Please, choose your class:\n> '))
    if userClass > 3:
        print('Invalid option, try again')
        sleep(1)
        _cls()
        return SelectClass()
    if userClass == 1:
        print(FighterDescription)
        confirmed = int(input('Are you satisfied?\n[1] Yes\n[2] No\n> '))
        if confirmed == 2:
            _cls()
            return SelectClass()
        if confirmed == 1:
            sheet = book.get_sheet_by_name("UserStats")
            sheet['A2'].value = cFighter
            sheet['B2'].value = HPFighter
            sheet['C2'].value = MPFighter
            sheet['D2'].value = AttFighter
            sheet['E2'].value = DefFighter
            sheet['F2'].value = 'Sword'
            book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
            import Normal
        elif confirmed > 2:
            print('Invalid option, try again')
            sleep(1)
            _cls()
            return SelectClass()
    elif userClass == 2:
        print(MageDescription)
        confirmed = int(input('Are you satisfied?\n[1] Yes\n[2] No\n> '))
        if confirmed == 2:
            _cls()
            return SelectClass()
        if confirmed == 1:
            sheet = book.get_sheet_by_name("UserStats")
            sheet['A2'].value = cMage
            sheet['B2'].value = HPMage
            sheet['C2'].value = MPMage
            sheet['D2'].value = AttMage
            sheet['E2'].value = DefMage
            sheet['F2'].value = 'Stave'
            book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
            import Normal
        if confirmed == 2:
            _cls()
            return SelectClass()
    else:
        print(NecromancerDescription)
        confirmed = int(input('Are you satisfied?\n[1] Yes\n[2] No\n> '))
        if confirmed == 2:
            _cls()
            return SelectClass()
        if confirmed == 1:
            sheet = book.get_sheet_by_name("UserStats")
            sheet['A2'].value = cNecro
            sheet['B2'].value = HPNecro
            sheet['C2'].value = MPNecro
            sheet['D2'].value = AttNecro
            sheet['E2'].value = DefNecro
            sheet['F2'].value = 'Scythe'
            book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
            import Normal
        if confirmed == 2:
            _cls()
            return SelectClass()
SelectClass()