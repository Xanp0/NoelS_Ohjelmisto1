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

class ElectricVersion(Car):
    def __init__(self, regNumber, maxSpeed, battery, velocity=0, travel=0):
        super().__init__(regNumber, maxSpeed, velocity, travel)
        self.battery = battery

    def kiihdytä(self, speed):
        super().kiihdytä(speed)
        return

    def kulje(self, travelTime):
        super().kulje(travelTime)
        self.battery -= (self.velocity / 10) * travelTime
        return

class GasVersion(Car):
    def __init__(self, regNumber, maxSpeed, gas, velocity=0, travel=0):
        super().__init__(regNumber, maxSpeed, velocity, travel)
        self.gas = gas

    def kiihdytä(self, speed):
        super().kiihdytä(speed)
        return

    def kulje(self, travelTime):
        super().kulje(travelTime)
        self.gas -= (self.velocity / 10) * travelTime
        return

sähköauto = ElectricVersion("ABC-15", 180, 52.5, 80)
auto = GasVersion("ACD-123", 165, 32.3, 65)

sähköauto.kulje(3)
auto.kulje(3)
print(f"Rekisteri: {sähköauto.regNumber}. Huippunopeus: {sähköauto.maxSpeed} km/h. "
      f"Tämänhetkinen nopeus: {sähköauto.velocity} km/h. Kuljettu matka: {sähköauto.travel} km.")
print(f"3 tunnin ajon jälkeen autoon jäi {sähköauto.battery:.1f} kWh.")
print("")

print(f"Rekisteri: {auto.regNumber}. Huippunopeus: {auto.maxSpeed} km/h. "
      f"Tämänhetkinen nopeus: {auto.velocity} km/h. Kuljettu matka: {auto.travel} km.")
print(f"3 tunnin ajon jälkeen autoon jäi {auto.gas:.1f} l.")
