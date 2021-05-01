from openpyxl import load_workbook
import random
from time import sleep
from utils import _cls

EnemyChosen = random.randint(1, 3)
book = load_workbook(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
UserStats = book["UserStats"]
EnemyClass = book["EnemyClass"]
EnemyStats = book["EnemyStats"]
UserClass = UserStats['A2'].value
UserHP = UserStats['B2'].value
UserMP = UserStats['C2'].value
UserAttack = UserStats['D2'].value
UserDefense = UserStats['E2'].value
if EnemyChosen == 1:
    EnemyClass = EnemyStats['A2'].value
    EnemyHP = EnemyStats['B2'].value
    EnemyMP = EnemyStats['C2'].value
    EnemyAttack = EnemyStats['D2'].value
    EnemyDefense = EnemyStats['E2'].value
elif EnemyChosen == 2:
    EnemyClass = EnemyStats['A3'].value
    EnemyHP = EnemyStats['B3'].value
    EnemyMP = EnemyStats['C3'].value
    EnemyAttack = EnemyStats['D3'].value
    EnemyDefense = EnemyStats['E3'].value
else:
    EnemyClass = EnemyStats['A4'].value
    EnemyHP = EnemyStats['B4'].value
    EnemyMP = EnemyStats['C4'].value
    EnemyAttack = EnemyStats['D4'].value
    EnemyDefense = EnemyStats['E4'].value
def Actions():
    _UserHP = 1
    _EnemyHP = 1
    while _UserHP or _EnemyHP <= 0:
        print('[1] Attack\n[2] Defend\n[3] Spell\n[4] Run')
        action = int(input('Select an action:\n> '))
        if action > 4:
            print('Invalid option, try again')
            sleep(1)
            _cls()
            return Actions()
        elif action == 1:
            _EnemyDefense = random.randint(1, EnemyDefense)
            _UserAttack = random.randint(1, UserAttack)
            if _EnemyDefense > _UserAttack:
                print(f'You attack {EnemyClass} with {_UserAttack} power, {EnemyClass} defended with {_EnemyDefense}')
            elif _EnemyDefense < _UserAttack:
                _EnemyHP = EnemyHP - _UserAttack
                print(f'You hit {EnemyClass} with {_UserAttack} power!\n{EnemyClass} HP: {_EnemyHP}')
    
                if _EnemyHP <= 0:
                    print('Enemy defeated!')
                    break
            else:
                print(f'{UserClass} attack and {EnemyClass} defense is the same, nothing happened')
        if action == 2:
            _EnemyAttack = random.randint(1, EnemyAttack)
            _UserDefense = random.randint(1, UserDefense)
            if _UserDefense > _EnemyAttack:
                print(f'You defend the attack with {_UserDefense}')
            elif _UserDefense < _UserAttack:
                _UserHP = UserHP - _EnemyAttack
                print(f'You defended {EnemyClass} with {_UserDefense}, but {EnemyClass} hit you with {EnemyAttack}!\nYour HP: {_UserHP}')
                if _UserHP <= 0:
                    print('You died!')
                    break
            else:
                print(f'{UserClass} defense and {EnemyClass} attack is the same, nothing happened')
    
print(f'A wild {EnemyClass} appears!\nHP: {EnemyHP}\nMP: {EnemyMP}\nAttack: {EnemyAttack}\nDefense: {EnemyDefense}\nWhat you will do?')
Actions()
