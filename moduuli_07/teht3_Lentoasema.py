lentoasemat = {"EFHK": "Helsinki-Vantaa",
               "EFHF": "Helsinki-Malmi",
               "ESSA": "Stockholm-Arlanda",
               "LTCJ": "Batman"}
lopeta = False

while lopeta != True:
    print(" ")  # vain tyhjä rivi
    print("Jos et ole tekemässä toimintoa jätä vastaus tyhjäksi")
    komento1 = input("Haluatko syöttää uuden lentoaseman: ")

    if komento1 == "":
        komento2 = input("Haetko jo syötettyä lentoaseman teitoja: ")

        if komento2 == "":
            komento3 = input("Jos haluat lopettaa kirjoita vaan jotakin: ")

            if komento3 != "":
                lopeta = True
                break

        else:
            icao = input("Anna ICAO-koodi: ")
            if icao in lentoasemat:
                print(f"ICAO-koodi tarkoittaa {lentoasemat[icao]}.")

    else:
        nimi = input("Syötä uusi lentoasema: ")
        koodi = input("Syötä uusi ICAO-koodi: ")
        lentoasemat[koodi] = nimi

print("Toiminnat lopetettu.")
print(lentoasemat)
