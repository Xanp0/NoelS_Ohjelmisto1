import random
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja
# asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se
# on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False
class Competition:
    def __init__(self, compName, raceLength, competitors):
        self.compName = compName
        self.raceLength = raceLength
        self.competitors = competitors

    def timeSpent(self):
        return

    def compSituation(self):
        return

    def compEnded(self):
        return

class Car:
    def __init__(self, regNumber, maxSpeed, velocity=0, travel=0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.velocity = velocity
        self.travel = travel

    def kiihdytä(self, speed):
        self.velocity += speed

        if self.velocity > self.maxSpeed:
            self.velocity = self.maxSpeed

        elif self.velocity < 0:
            self.velocity = 0
        return

    def kulje(self, travelTime):
        self.travel += self.velocity * travelTime
        return

# pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin
# aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
# toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan
# kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan
# tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
autot = []

for i in range(1, 11):
    regNum = f"ABC-{i}"
    newMaxSpeed = random.randint(100, 200)
    raceCar = Car(regNum, newMaxSpeed)
    autot.append(raceCar)

kisaJatkuu = True
kisaKestänyt = 0

while kisaJatkuu:
    for racer in autot:
        speedChanges = random.uniform(-10, 15)
        racer.kiihdytä(speedChanges)
        racer.kulje(1)

        if racer.travel >= 10000:
            kisaJatkuu = False

    kisaKestänyt += 1
print(f"Kisa on kestänyt {kisaKestänyt} tuntia.")

for racers in autot:
    print(f"Rekisteri: {racers.regNumber}. Huippunopeus: {racers.maxSpeed:.0f} km/h. "
          f"Tämänhetkinen nopeus: {racers.velocity:.0f} km/h. Kuljettu matka: {racers.travel:.0f} km.")
