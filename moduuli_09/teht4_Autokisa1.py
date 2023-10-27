import random
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
