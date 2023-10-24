class Car:
    def __init__(self, regNumber, maxSpeed, velocity=0, travel=0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.velocity = velocity
        self.travel = travel

auto1 = Car("ABC-123", 142)
print(f"Rekisteri: {auto1.regNumber}. Huippunopeus: {auto1.maxSpeed} km/h. "
      f"Tämänhetkinen nopeus: {auto1.velocity} km/h. Kuljettu matka: {auto1.travel} km.")
