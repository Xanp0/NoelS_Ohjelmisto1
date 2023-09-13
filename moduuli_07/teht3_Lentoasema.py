# lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
# ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
# tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
# ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
# monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan
# lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla)
lentoasemat = {"Helsinki-Vantaa": "EFHK",
               "Helsinki-Malmi": "EFHF",
               "Stockholm-Arlanda": "ESSA",
               "Batman": "LTCJ"}
lopeta = False

while lopeta != True:
    print("Jos et ole tekemässä toimintoa jätä vastaus tyhjäksi")
    komento1 = input("Haluatko syöttää uuden lentoaseman: ")

    if komento1 != "":

        komento2 = input("Haetko jo syötettyä lentoaseman teitoja: ")
        if komento2 != "":

            komento3 = input("Jos haluat lopettaa kirjoita vaan jotakin: ")
            if komento3 != "":
                lopeta = True
