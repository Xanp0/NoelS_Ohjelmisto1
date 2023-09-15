# kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import config

import mysql.connector
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user=config.user,
        password=config.password,
        autocommit=True
        )

def hae_kentta_icao_koodilla(icao):
        sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos
