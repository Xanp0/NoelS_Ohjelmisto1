# TODO luvut 21 ja 2 ei toimi oikein
luku = int(input("Anna kokonaisluku: "))

if luku >= 1:
    for testi in range(2, int(luku // 2) + 1):
        if (luku % testi) == 0:
            print(f"{luku} ei ole alkuluku")
            break
        else:
            print(f"{luku} on alkuluku")
            break

else:
    print(f"{luku} ei ole alkuluku")
