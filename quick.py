# Micro RPG text-based game
# Import section
import random
import time
import sys
# Variables
charStrenght = 0
charSpeed = 0
monsterStrenght = 0
monsterSpeed = 0
charHP = 0
monsterHP = 0
charAttack = 0
monsterAttack = 0
def fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed):
	charHP = 50
	monsterHP = 50
	charPower = 0
	charHits = 0
	avgCharPower = 0
	monsterHits = 0
	monsterPower = 0
	avgMonsterPower = 0
	while charHP or monsterHP <= 0:
		charAttack = random.randint(1, 3)
		charSpeed = random.randint(1,5)
		monsterAttack = random.randint(1, 3)
		monsterSpeed = random.randint(1,5)
		if monsterAttack == charAttack:
			print('You and monster landed with same attack power.\nNothing happened.')
			time.sleep(1)
			
		if charSpeed > monsterSpeed and charAttack > monsterAttack:
			charHits = charHits + 1
			charPower = charPower + charAttack
			monsterHP = monsterHP - charAttack
			print(f'You hit the monster with {charAttack}.\nMonster have {monsterHP} HP',end='\r')
			time.sleep(1)
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
			print(f'You try to hit monster with {charAttack}, but monster strikes you back with {monsterAttack}\nYou have {charHP} HP')
			time.sleep(1)
			if charHP <= 0:
				avgMonsterPower = monsterPower / monsterHits
				avgMP = "{:.2f}".format(avgMonsterPower)
				print(f'\rYou lost the battle!\nMonster landed {monsterHits} hits.\nAverage power {avgMP}')
				prompt = str(input('Do you want to play again? (Y/N) ')).lower()
				if prompt == 'y':
					fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
				else:
					break
		if charSpeed > monsterSpeed and charAttack < monsterAttack:
			print('Monster miss the attack!')
			time.sleep(1)
		elif charSpeed < monsterSpeed and charAttack > monsterAttack:
			print('You miss the attack!')
			time.sleep(1)
fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
