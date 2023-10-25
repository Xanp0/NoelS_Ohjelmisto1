# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta
# auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja
# +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia

# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia

import random
class Car:
    def __init__(self, regNumber, maxSpeed=random.randint(100, 200), velocity=0, travel=0):
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

#autot[] = Car
auto1 = Car("ABC-1")
auto2 = Car("ABC-2")
#autot.kulje(random.uniform(-10, 15))

print(f"Rekisteri: {auto1.regNumber}. Huippunopeus: {auto1.maxSpeed} km/h. "
      f"Tämänhetkinen nopeus: {auto1.velocity} km/h. Kuljettu matka: {auto1.travel} km.")
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
