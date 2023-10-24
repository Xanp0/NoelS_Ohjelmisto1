class Car:
    def __init__(self, regNumber, maxSpeed, velocity=0, travel=0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.velocity = velocity
        self.travel = travel

    def kiihdytä(self, speed):
        self.velocity += speed

        if self.velocity > 142:
            self.velocity = 142

        elif self.velocity < 0:
            self.velocity = 0
        return

    def kulje(self, travelTime):
        self.travel += self.velocity * travelTime
        return

auto1 = Car("ABC-123", 142, 60, 2000)
auto1.kulje(1.5)

print(f"Rekisteri: {auto1.regNumber}. Huippunopeus: {auto1.maxSpeed} km/h. "
      f"Tämänhetkinen nopeus: {auto1.velocity} km/h. Kuljettu matka: {auto1.travel} km.")
