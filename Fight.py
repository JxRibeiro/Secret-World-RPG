import random
import time
import sys
from openpyxl import load_workbook
from time import sleep
from utils import _cls
EnemyChosen = random.randint(1, 3)
book = load_workbook(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
UserStats = book["UserStats"]
UserClass = UserStats['A2'].value
UserHP = UserStats['B2'].value
UserMP = UserStats['C2'].value
UserAttack = UserStats['D2'].value
UserDefense = UserStats['E2'].value
_UserHP = UserHP
_UserAttack = random.randint(1, UserAttack)
_UserDefense = random.randint(1, UserDefense)
EnemyClass = book["EnemyClass"]
EnemyStats = book["EnemyStats"]

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
_EnemyHP = EnemyHP
_EnemyAttack = random.randint(1, EnemyAttack)
_EnemyDefense = random.randint(1, EnemyDefense)
turn = 1
loopx = 0
print(f'A wild {EnemyClass} appears!\nHP: {EnemyHP}\nAttack: {EnemyAttack}\nDefense: {EnemyDefense}\nSelect an action:\n')
while _UserHP >= 0 or _EnemyHP >= 0:
    _UserAttack = random.randint(1, UserAttack)
    _UserDefense = random.randint(1, UserDefense)
    _EnemyAttack = random.randint(1, EnemyAttack)
    _EnemyDefense = random.randint(1, EnemyDefense)
    if turn == 1:
        while loopx == 0:
            move = int(input('[1] Attack\n[2] Defend\n> '))
            if move == 1:
                print(f'{UserClass} try to attack {EnemyClass}')
                sleep(1)
                if _UserAttack > _EnemyDefense:
                    _EnemyHP = _EnemyHP - _UserAttack
                    if _EnemyHP <=0:
                        print('You won')
                        quit()
                    else:
                        print(f'{EnemyClass} suffer {_UserAttack} damage!\n{EnemyClass} HP {_EnemyHP}')
                        loopx = 1
                elif _UserAttack < _EnemyDefense:
                    print(f'{UserClass} miss the attack!')
                    loopx = 1
                else:
                    print(f'Nothing happened')
                    loopx = 1
            elif move == 2:
                print(f'{UserClass} try to defend')
                sleep(1)
                if _UserDefense < _EnemyAttack:
                    _UserHP = _UserHP - _EnemyAttack
                    if _UserHP <= 0:
                        print('You lost')
                        quit()
                    else:
                        print(f'{UserClass} failed to stop {EnemyClass} attack!\nSuffer {_EnemyAttack} damage\nHP {_UserHP}')
                        loopx = 1
                elif _UserDefense > _EnemyAttack:
                    print(f'{UserClass} blocks {EnemyClass} attack')
                else:
                    print('Nothing happened')
                    loopx = 1
        turn = 2
    if turn == 2:
        while loopx == 1:
            AImove = random.randint(1,2)
            if AImove == 1:
                print(f'{EnemyClass} attack!')
                if _EnemyAttack > _UserDefense:
                    _UserHP = _UserHP - _EnemyAttack
                    if _UserHP <= 0:
                        print('You lost')
                        quit()
                    else:
                        print(f'{EnemyClass} hit {UserClass}\nDamage: {_EnemyAttack}\nHP: {_UserHP}')
                        loopx = 0
                elif _EnemyAttack < _UserDefense:
                    print(f'{EnemyClass} miss the attack')
                    loopx = 0
                else:
                    print('Nothing happened')
                    loopx = 0
            elif AImove == 2:
                print(f'{EnemyClass} try to defend')
                sleep(1)
                if _EnemyDefense > _UserAttack:
                    print(f'{EnemyClass} blocks the attack')
                    loopx = 0
                elif _EnemyDefense < _UserAttack:
                    if _EnemyHP <= 0:
                        print('You won')
                        quit()
                    else:
                        _EnemyHP = _EnemyHP - _UserAttack
                        print(f'{EnemyClass} failed to stop {UserClass} attack!\nSuffer {_EnemyAttack} damage\nHP {_EnemyHP}')
                        loopx = 0
                else:
                    print('Nothing happened')
                    loopx = 0
            turn = 1
            continue
