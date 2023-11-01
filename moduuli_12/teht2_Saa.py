# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja
# tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
import json

nimi = input("Anna paikkakunnan nimi: ")
#try:
    #pyynto = "api" + nimi
    #vastaus = requests.get(pyynto)
    #jsonVastaus = vastaus.json()
    #print(jsonVastaus[lämpötila])
#except requests.exceptions.RequestException as e:
    #print ("Hakua ei voitu suorittaa.")
    #print(e)
