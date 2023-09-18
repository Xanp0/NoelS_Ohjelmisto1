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

def hae_maa_koodilla(iso):
        sql = f"SELECT TYPE, COUNT(*) FROM airport WHERE iso_country = '{iso}' GROUP BY TYPE;"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()

        if kursori.rowcount > 0:
                for tieto in tulos:
                        print(f"Lentoaseman tyyppi on {tieto[0]} ja lkm: {tieto[1]}")
        else:
                print("Ei onnistunut.")

        return

komento = input("Anna ISO-koodi: ")
hae_maa_koodilla(komento)
