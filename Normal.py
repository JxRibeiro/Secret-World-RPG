from time import sleep
import sys
from openpyxl import load_workbook
from utils import _cls

book = load_workbook(filename="data.xlsx")
sheet = book.get_sheet_by_name("UserStats")
userClass = sheet['A2'].value
itemReceived = sheet['F2'].value
welcomeMessage = f"""
Nuzzac:
This world changed so much since you have left.
Nodre, protector of the forest have been murdered by Tekoa, the mysterious in behalf of Favrut, bringer of the death.
You have to travel in time to save Nodre and our world!
It's too dangerous to go alone, take this
"""

deepForestMessage = f"""
{userClass} you're walking into a deep forest,
"""

for line in welcomeMessage:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0)
sleep(1)
print(f'{itemReceived} equipped!')
sleep(1)
_cls()

import Fight

