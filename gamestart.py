from time import sleep
import sys
import os
def _cls():
    os.system('cls' if os.name=='nt' else 'clear')
_cls()
WelcomeMessage = """
Welcome to Secret World!
Do you want to go in a quick or a normal adventure? 
"""
for line in WelcomeMessage:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0)
userInput = int(input('[1] Quick\n[2] Normal\nSelect:\n> '))
if userInput == 1:
    _cls()
    import quick
else:
    _cls()
    import normal