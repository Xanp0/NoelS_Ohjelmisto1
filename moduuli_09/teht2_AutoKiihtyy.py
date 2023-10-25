class Car:
    def __init__(self, regNumber, maxSpeed, velocity =0, travel =0):
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

auto1 = Car("ABC-123", 142)
auto1.kiihdytä(+30)
auto1.kiihdytä(+70)
auto1.kiihdytä(+50)
# lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus
print(f"Tämänhetkinen nopeus: {auto1.velocity} km/h.")
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h
auto1.kiihdytä(-200)
print(f"Tämänhetkinen nopeus: {auto1.velocity} km/h.")

# print(f"Rekisteri: {auto1.regNumber}. Huippunopeus: {auto1.maxSpeed} km/h. "
#      f"Tämänhetkinen nopeus: {auto1.velocity} km/h.")
