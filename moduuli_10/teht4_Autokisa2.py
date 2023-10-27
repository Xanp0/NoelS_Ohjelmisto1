import random

class Competition:
    def __init__(self, compName, raceLength, competitors):
        self.compName = compName
        self.raceLength = raceLength
        self.competitors = competitors

    def timeUsed(self):
        for racers in self.competitors:
            speedChanges = random.uniform(-10, 15)
            racers.kiihdytä(speedChanges)
            racers.kulje(1)
        return

    def compSituation(self):
        for y in self.competitors:
            print(f"Rekisteri: {y.regNumber}. Huippunopeus: {y.maxSpeed:.0f} km/h. "
                  f"Tämänhetkinen nopeus: {y.velocity:.0f} km/h. Kuljettu matka: {y.travel:.0f} km.")
        return

    def compEnded(self):
        kisaLoppu = False
        for z in self.competitors:
            if z.travel >= self.raceLength:
                kisaLoppu = True
                break
        return kisaLoppu

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

autot = []

for i in range(1, 11):
    regNum = f"ABC-{i}"
    newMaxSpeed = random.randint(100, 200)
    raceCar = Car(regNum, newMaxSpeed)
    autot.append(raceCar)

kisa = Competition("Suuri romuralli", 8000, autot)
kisaJatkuu = True
kisaKestänyt = 0

while kisaJatkuu:
    for racer in autot:

        kisa.timeUsed()
        kisaKestänyt += 1

        if kisa.compEnded() == True:
            kisaJatkuu = False

        if kisaKestänyt % 10 == 0:
            print(f"Kisan tilanne {kisaKestänyt} tunnin jälkeen:")
            kisa.compSituation()
            print("")

print(f"Kisa on päättynyt ja siinä kesti {kisaKestänyt} tuntia.")
kisa.compSituation()
