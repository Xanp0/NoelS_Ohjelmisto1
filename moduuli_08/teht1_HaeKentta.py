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

        if kursori.rowcount > 0:
                for rivi in tulos:
                        print(f"Lentokentän nimi on {rivi[0]} ja sijainti on kunnassa {rivi[1]}")
        else:
                print("Ei onnistunut.")

        return

koodi = input("Lentoaseman ICAO-koodi: ")
hae_kentta_icao_koodilla(koodi)
