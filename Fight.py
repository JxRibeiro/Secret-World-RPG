# Micro RPG text-based game
# Import section
import random
import time
import sys
from openpyxl import load_workbook
import random
from time import sleep
from utils import _cls

# Variables
charStrenght = 0
charSpeed = 0
monsterStrenght = 0
monsterSpeed = 0
charHP = 0
monsterHP = 0
charAttack = 0
monsterAttack = 0

EnemyChosen = random.randint(1, 3)
book = load_workbook(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
UserStats = book["UserStats"]
UserClass = UserStats['A2'].value
UserHP = UserStats['B2'].value
UserMP = UserStats['C2'].value
UserAttack = UserStats['D2'].value
UserDefense = UserStats['E2'].value
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

def fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed):
	charHP = UserHP
	monsterHP = EnemyHP
	charPower = 0
	charHits = 0
	avgCharPower = 0
	monsterHits = 0
	monsterPower = 0
	avgMonsterPower = 0
	while UserHP or EnemyHP <= 0:
		charAttack = random.randint(1, UserAttack)
		charSpeed = random.randint(1, UserDefense)
		monsterAttack = random.randint(1, EnemyAttack)
		monsterSpeed = random.randint(1,EnemyDefense)
        
		if monsterAttack == charAttack:
			print(f'{UserClass} and {EnemyClass} landed same attack power.\nNothing happened.')
			time.sleep(0.5)
			
		if charSpeed > monsterSpeed and charAttack > monsterAttack:
			charHits = charHits + 1
			charPower = charPower + charAttack
			monsterHP = monsterHP - charAttack
			print(f'You hit the monster with {charAttack}.\nMonster have {monsterHP} HP',)
			time.sleep(0.5)
			if monsterHP <= 0:
				avgCharPower = charPower / charHits
				avgCP = "{:.2f}".format(avgCharPower)
				print(f'Congratulations! You win the battle\nYou landed {charHits} hits.\nAverage power {avgCP}')
				prompt = str(input('Do you want to play again? (Y/N)')).lower()
				if prompt == 'y':
					fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
				else:
					break
		elif charSpeed < monsterSpeed and charAttack < monsterAttack:
			monsterHits = monsterHits + 1
			monsterPower = monsterPower + monsterAttack
			charHP = charHP - monsterAttack
			print(f'You try to hit {EnemyClass} with {charAttack}, but {EnemyClass} strikes you back with {monsterAttack}\nYou have {charHP} HP')
			time.sleep(0.5)
			if charHP <= 0:
				avgMonsterPower = monsterPower / monsterHits
				avgMP = "{:.2f}".format(avgMonsterPower)
				print(f'{UserClass} you lost the battle!\n{EnemyClass} landed {monsterHits} hits.\nAverage power {avgMP}')
				prompt = str(input('Do you want to play again? (Y/N) ')).lower()
				if prompt == 'y':
					fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
				else:
					break
		if charSpeed > monsterSpeed and charAttack < monsterAttack:
			print(f'{EnemyClass} miss the attack!')
			time.sleep(0.5)
		elif charSpeed < monsterSpeed and charAttack > monsterAttack:
			print(f'{UserClass} miss the attack!')
			time.sleep(0.5)
fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
