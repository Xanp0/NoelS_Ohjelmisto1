# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja
# tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import requests

komento = input("Anna paikkakunnan nimi: ")

# Pyynnön malli: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Huom: kun lisäät todellisen hakuehdon, niin poista myös sulut { }, esim. q={city name} => q=helsinki
# Nettiin lähetettävä lopullinen hakulause
pyyntö = "api"

try:
    vastaus = requests.get(pyyntö)

    # tarkistetaan että onnistuiko hakuoperaatio (200 = ok)
    if vastaus.status_code == 200:
        jsonVastaus = vastaus.json()

except requests.exceptions.RequestException as e:
    print("Ei onnistunut.")
