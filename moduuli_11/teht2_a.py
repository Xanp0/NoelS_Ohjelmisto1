# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita
# aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun
# asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa
# luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123,
# 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja
# ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat
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
