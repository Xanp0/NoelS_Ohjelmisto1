leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

uudetNaulat = leiviskät*20
uudetLuodit = (uudetNaulat+naulat) * 32
luotienMassa = (luodit+uudetLuodit) * 13.3

massaKg = luotienMassa/1000
massaG = luotienMassa % 1000

print('Massa nykymittojen mukaan:')
print(str(int(massaKg)) + f" kilogrammaa ja {massaG:1.2f} grammaa.")
