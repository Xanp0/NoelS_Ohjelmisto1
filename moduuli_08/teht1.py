# kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja
# tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
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

koodi = input("Lentoaseman ICAO-koodi: ")
kenttä = hae_kentta_icao_koodilla(koodi)
print(f"Kentän nimi on {kenttä[0][1]} ja sijainti kunnassa {kenttä[0][2]}")
