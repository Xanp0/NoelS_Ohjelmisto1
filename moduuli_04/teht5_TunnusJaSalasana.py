tunnus = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")
yritykset = 0
evätty = 0

while tunnus != "python" and salasana != "rules":
    print("Tiedot ovat väärin")
    if 4 <= yritykset:
        evätty = 1
        break

    yritykset = yritykset + 1
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
else:
    print("Tervetuloa käyttäjä.")

if evätty == 1:
    print("Viisi kertaa meni väärin. Pääsy evätty.")
