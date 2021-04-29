from openpyxl import load_workbook
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
print('Avalaible classes:')
print(f'{cFighter}\nHP: {HPFighter}\nMP: {MPFighter}\nAttack: {AttFighter}\nDefense: {DefFighter}\n')
print(f'{cMage}\nHP: {HPMage}\nMP: {MPMage}\nAttack: {AttMage}\nDefense: {DefMage}\n')
print(f'{cNecro}\nHP: {HPNecro}\nMP: {MPNecro}\nAttack: {AttNecro}\nDefense: {DefNecro}\n\n') 
print('Please, choose your class:\n')
userClass = int(input('> '))
if userClass == 1:
    sheet = book.get_sheet_by_name("UserStats")
    sheet['A2'].value = cFighter
    sheet['B2'].value = HPFighter
    sheet['C2'].value = MPFighter
    sheet['D2'].value = AttFighter
    sheet['E2'].value = DefFighter
    book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
    print('Welcome Fighter!')
if userClass == 2:
    sheet = book.get_sheet_by_name("UserStats")
    sheet['A2'].value = cMage
    sheet['B2'].value = HPMage
    sheet['C2'].value = MPMage
    sheet['D2'].value = AttMage
    sheet['E2'].value = DefMage
    book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
    print('Welcome Mage!')
if userClass == 3:
    sheet = book.get_sheet_by_name("UserStats")
    sheet['A2'].value = cNecro
    sheet['B2'].value = HPNecro
    sheet['C2'].value = MPNecro
    sheet['D2'].value = AttNecro
    sheet['E2'].value = DefNecro
    book.save(filename="/home/joao/00-Dev/Python/Secret-World-RPG/data.xlsx")
    print('Welcome Necromancer!')
