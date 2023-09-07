import math

luku = int(input("Anna kokonaisluku: "))
onkoAlkuluku = True

for testaus in range(2, int(math.sqrt(luku))):
    if luku % testaus == 0:
        onkoAlkuluku = False
        break

if onkoAlkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")
